# Carisurg  Portfolio

## 1. What is this project, and what does it do?
This repository contains data analysis and cleaning notebooks developed during Week 0 of the Carisurg program. The project demonstrates clinical dataset preprocessing, data imputation, and clinical risk visualization. 

### Key Portfolios & Features
*   **Task 1: Data Profiling & Column Cleaning** – Analyzed a clinical dataset to identify structural data type errors (Gender, GCS, SBP, Pulse) and engineered a remapping pipeline specifically for the Gender feature.
*   **Task 2: Collaborative Data Imputation** – Handled respiratory rate anomalies, managed missing (NaN) values, and applied mean imputation to build a clean baseline dataset.
*   **Task 3: Clinical Risk Visualization** – Plotted clinical distributions and relationships to isolate high-risk patients:
    *   *Histogram:* Categorizes patients by clinical breathing patterns (**Eupnea**, **Tachypnea**, or **Bradypnea**).
    *   *Scatter Plot (Respiratory Rate vs. FiO_2):* Visually separates stable individuals from critical, high-risk patients requiring oxygen support.

---

## 2. Who is it for?
This project is built for healthcare data analysts, clinical researchers, and Carisurg program evaluators looking to see structured examples of clinical data cleaning and patient risk mapping.

---

## 3. How do I install and run it?

### Prerequisites
Make sure you have Python 3 and Jupyter Notebook (or JupyterLab) installed.

### Installation
1. Clone the repository:
```bash
   git clone [https://https://github.com/Colosolizer/carisurg-portfolio]

```

2. Navigate to the project folder:

```bash
   cd carisurg-portfolio

```

3. Install required visualization and analysis libraries (e.g., pandas, matplotlib, seaborn):

```bash
   pip install pandas notebook matplotlib seaborn

```

### Running the Notebooks

Launch Jupyter Notebook from your terminal to open and run any file in the `notebooks/` directory:

```bash
jupyter notebook

```

---

## 4. Where does the data come from?

The analysis utilizes an anonymized clinical dataset containing 2,205 rows and 11 distinct clinical patient columns (including features like Gender, Glasgow Coma Scale (GCS), Systolic Blood Pressure (SBP), Pulse, Fraction of Inspired Oxygen ($FiO_2$), and Respiratory Rate).

---

## 5. Who built it, and how do I reach them?

### Individual Contribution

* **Task 1 & Task 3 Lead:** Sekou Ruddock

### Task 2 Collaborators

* Tyler Baksh
* Kaylah Leigertwood-Ollivierre
* Mya Symister
* Sariana Ramoutar
* Zhanna McDonald
* Sekou Ruddock

*For inquiries or collaboration, please reach out via GitHub*

