# Python Data Processing Pipeline

## Visualization Preview

![Correlation Heatmap](outputs/plots/correlation_heatmap.png)
> This visualization shows feature correlations within the dataset, helping identify relationships between variables and supporting model development.

---

## Project Overview

This project implements a complete Python pipeline for loading, cleaning, analyzing, and modeling monitoring data using multivariable linear regression.

The goal is to simulate a real-world data processing workflow, including preprocessing, visualization, and model evaluation.

---

## Features

- Data ingestion from CSV files  
- Data cleaning and preprocessing  
- Handling invalid values (`-200`)  
- Feature scaling (normalization)  
- Correlation analysis and visualization  
- Multivariable linear regression (from scratch)  
- Gradient Descent and Normal Equation  
- Model evaluation using R² and Adjusted R²  
- Data visualization (heatmap, pairplot, loss curve)  
- Modular project structure (production-style)  
- Basic unit testing  

---

## Data Workflow

The pipeline processes monitoring data through the following stages:

1. **Data Ingestion**
   - Load dataset from CSV file
   - Handle dataset-specific formatting issues (e.g., separators, decimal format)

2. **Data Cleaning**
   - Replace invalid values (e.g., -200) with NaN
   - Remove or impute missing values
   - Convert data types to appropriate formats

3. **Data Transformation**
   - Normalize and scale features
   - Select relevant variables for modeling
   - Prepare features and target variables

4. **Feature Engineering**
   - Generate cleaned and structured feature set
   - Ensure compatibility with regression models

5. **Modeling**
   - Implement multivariable linear regression using:
     - Gradient Descent (iterative approach)
     - Normal Equation (analytical solution)

6. **Evaluation**
   - Compute performance metrics:
     - R² score
     - Adjusted R² score
   - Analyze model accuracy and behavior

7. **Visualization**
   - Generate plots for analysis:
     - Correlation heatmap
     - Pairplot for feature relationships
     - Loss curve for model convergence

8. **Output Generation**
   - Save processed dataset to CSV and JSON
   - Save evaluation results and plots

---

## Automation

The pipeline is fully automated:

- A central script (`main.py`) orchestrates the workflow
- Each step is implemented as a reusable module
- The pipeline can be executed with a single command

This design ensures:
- reproducibility
- scalability
- easy maintenance

---

## Technical Approach

- Data preprocessing ensures high-quality input for modeling
- Two regression approaches provide both iterative and analytical solutions
- Visualization supports interpretation of model performance and data relationships

---

## Key Insights

- Data quality significantly impacts model performance
- Feature normalization improves convergence in gradient descent
- Correlation analysis helps identify important relationships between variables

---

## Project Structure

````
python-data-processing-pipeline/
├── data/
│ ├── raw/
│ └── processed/
├── outputs/
│ ├── plots/
│ └── metrics/
├── src/
├── tests/
├── notebooks/
├── main.py
├── requirements.txt
└── README.md

````

---

## Installation

```bash
git clone https://github.com/oumaimabnz/python-data-processing-pipeline
cd python-data-processing-pipeline
python -m venv .venv
```
Activate the virtual environment:

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
macOS/Linux
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Run the Pipeline:
```bash
python main.py
```
This will:

- Clean the dataset
- Train regression models
- Generate visualizations
- Save evaluation metrics

## Run Tests 
```bash
pytest
```

---

## Outputs

The pipeline generates:

- Cleaned dataset (CSV & JSON)
- Correlation heatmap
- Pairplot visualization
- Loss curve
- Evaluation metrics (R², Adjusted R²)

---

## Notebook

The notebooks/exploration.ipynb file contains exploratory data analysis and initial experiments.

---

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pytest

---

📌 Note

This project was developed as a structured data processing pipeline inspired by real-world monitoring systems.

---

## Author

Oumaima Benaziza
