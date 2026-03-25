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

The data processing pipeline follows a structured workflow:

1. **Data Ingestion**
   - Load raw product dataset from CSV file
   - Handle parsing issues and malformed rows

2. **Data Cleaning**
   - Convert price values to numeric format
   - Remove missing or invalid entries
   - Standardize text fields (e.g., product descriptions)

3. **Brand Extraction & Processing**
   - Extract brand names from product descriptions
   - Handle inconsistent formats (e.g., "StradivariusThrow")
   - Normalize brand naming using mapping and preprocessing rules

4. **Feature Engineering**
   - Compute stockout count from size availability
   - Calculate stockout rate per product
   - Estimate lost revenue based on stockouts and price

5. **Data Filtering**
   - Remove low-frequency brands to ensure reliable analysis

6. **Aggregation & Analysis**
   - Group data by brand
   - Compute:
     - Average price
     - Average stockout rate
     - Total lost revenue
     - Number of products

7. **Visualization**
   - Generate a dashboard-style scatter plot:
     - X-axis: Average price
     - Y-axis: Stockout rate
     - Bubble size: Lost revenue
   - Highlight high-impact brands

8. **Output Generation**
   - Export cleaned dataset to CSV and JSON
   - Save aggregated analysis results
   - Save visualization as image

---

## Automation

The entire workflow is automated through a pipeline:

- A single entry point (`main.py`) executes all steps
- Modular scripts handle each stage (preprocessing, analysis, visualization)
- No manual intervention is required once the pipeline is triggered

This ensures reproducibility and consistency across runs.

---

## Key Insights

- Brands with **high price and high stockout rate** represent the highest revenue loss
- Larger bubbles indicate brands with significant financial impact
- The dashboard helps identify opportunities for inventory optimization and pricing strategies

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
