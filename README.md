# Solar Challenge Week 0

This repository contains the initial setup for the Solar Challenge Week 0 project.

## Project Structure
```
├── .github/
│   └── workflows
│       ├── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
|------ src/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md
```
## Getting Started

1. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   ```
   ```sh
   On Windows:
   venv\Scripts\activate
   ```
   ```sh
   On macOS/Linux:
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```sh
    pip install -r requirements.txt
    ```
## Folders
- **notebooks/**: Contains Jupyter notebooks for data analysis and visualization.
- **tests/**: Contains unit tests for the project.
- **scripts/**: Contains utility scripts for data processing and analysis.
- **.github/workflows/**: Contains GitHub Actions workflows for CI/CD.

## Continuous Integration
This project uses GitHub Actions for continuous integration. The CI workflow is defined in `.github/workflows/ci.yml`.

## Notes
- All dependencies are listed in `requirements.txt`.
- Data files and CSVs are ignored via `.gitignore`.
