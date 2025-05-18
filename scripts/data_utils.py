# scripts/data_utils.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from windrose import WindroseAxes
import os

class SolarDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def summarize(self):
        print("Summary Statistics")
        display(self.df.describe()) # type: ignore
        print("\nMissing Values")
        display(self.df.isna().sum()) # type: ignore
        null_thresh = len(self.df) * 0.05
        display(self.df.isna().sum()[self.df.isna().sum() > null_thresh]) # type: ignore

    def detect_outliers(self, columns):
        # Detects outliers in the specified columns using the Z-score method.
        # Flags rows with any outlier in the given columns.
        z_scores = self.df[columns].apply(zscore)
        outliers = (z_scores.abs() > 3)
        self.df['OutlierFlag'] = outliers.any(axis=1)
        print(f"Outliers per column:\n{outliers.sum()}")
        print(f"Total rows with outliers: {self.df['OutlierFlag'].sum()} / {len(self.df)}")

    def impute_medians(self, columns):
        self.df[columns] = self.df[columns].fillna(self.df[columns].median())

    def save_cleaned(self, out_path):
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        self.df.to_csv(out_path, index=False)

    def plot_time_series(self):
        # Plots time series for GHI, DNI, DHI, and Tamb columns to visualize trends over time.
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
        plt.figure(figsize=(15, 6))
        for col in ['GHI', 'DNI', 'DHI', 'Tamb']:
            plt.plot(self.df['Timestamp'], self.df[col], label=col)
        plt.legend()
        plt.title("Solar & Temp Trends Over Time")
        plt.xlabel("Timestamp")
        plt.ylabel("Value")
        plt.show()

    def plot_cleaning_effect(self):
        # Plots the average ModA and ModB sensor readings before and after cleaning.
        # Useful for visualizing the impact of cleaning on sensor data.
        self.df['Cleaning'] = self.df['Cleaning'].astype(str)
        self.df.groupby('Cleaning')[['ModA', 'ModB']].mean().plot(kind='bar')
        plt.title('ModA & ModB Before/After Cleaning')
        plt.ylabel("Avg Sensor Reading")
        plt.show()

    def plot_correlation_heatmap(self):
        # Plots a heatmap showing the correlation between key solar and temperature variables.
        sns.heatmap(self.df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

    def plot_scatter(self):
        # Plots multiple scatter plots to visualize relationships between wind, humidity, and solar variables.
        sns.scatterplot(x='WS', y='GHI', data=self.df)
        sns.scatterplot(x='WSgust', y='GHI', data=self.df)
        sns.scatterplot(x='WD', y='GHI', data=self.df)
        sns.scatterplot(x='RH', y='Tamb', data=self.df)
        sns.scatterplot(x='RH', y='GHI', data=self.df)
        plt.title("Scatter Plots")
        plt.show()

    def plot_wind_rose(self):
        # Plots a wind rose diagram to visualize the distribution of wind direction and speed.
        ax = WindroseAxes.from_ax()
        ax.bar(self.df['WD'], self.df['WS'], normed=True, opening=0.8, edgecolor='white')
        ax.set_legend()
        plt.title("Wind Rose")
        plt.show()

    def plot_histograms(self):
        self.df[['GHI', 'WS']].hist(bins=30, figsize=(12, 5))
        plt.suptitle("Histograms of GHI and Wind Speed")
        plt.show()

    def plot_bubble_chart(self):
        # Bubble Chart
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df['GHI'], self.df['Tamb'], s=self.df['RH'], alpha=0.5, c='blue')
        plt.xlabel('GHI')
        plt.ylabel('Tamb')
        plt.suptitle('GHI vs Tamb with RH as Bubble Size')
        plt.show()