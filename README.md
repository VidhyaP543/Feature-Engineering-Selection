# Feature Engineering and Selection

## Project Overview

This project focuses on preparing the Titanic dataset for machine learning by performing feature engineering and feature selection. Various preprocessing techniques were applied to improve data quality and select the most relevant features for predictive modeling.

---

## Dataset

- **Dataset Name:** Titanic Passenger Dataset
- **File Format:** CSV
- **Total Records:** 891
- **Target Variable:** Survived

---

## Objective

- Handle missing values in the dataset.
- Convert categorical variables into numerical values.
- Scale numerical features.
- Select the most relevant features for machine learning.
- Generate a processed dataset for future model training.

---

## Tools & Technologies

- Python
- Pandas
- NumPy
- Scikit-learn

---

## Feature Engineering Steps

- Filled missing values in the **Age** column using the median.
- Filled missing values in the **Embarked** column using the mode.
- Removed the **Cabin** column due to excessive missing values.
- Encoded categorical features (**Sex** and **Embarked**) using Label Encoding.
- Scaled numerical features (**Age** and **Fare**) using StandardScaler.

---

## Feature Selection

Feature selection was performed using **SelectKBest** with the **Chi-Square (Chi²)** statistical test.

### Selected Features

- Sex
- Age
- SibSp
- Parch
- Embarked

---

## Output

The processed dataset containing the selected features was saved as:

- **engineered_features.csv**

---

## Challenges Faced

- Handling missing values appropriately.
- Encoding categorical features into numerical values.
- Applying feature scaling to numerical columns.
- Selecting the most relevant features using statistical methods.
- Organizing project files in a professional GitHub repository.

---

## GitHub Repository Structure

```text
Feature-Engineering-Selection/
│
├── data/
│   └── train.csv
│
├── output/
│   └── engineered_features.csv
│
├── reports/
│   └── Feature_Engineering_Report.pdf
│
├── scripts/
│   └── feature_engineering.py
│
├── README.md
└── requirements.txt
```

---

## Conclusion

Feature engineering and feature selection are important preprocessing steps in machine learning. By handling missing values, encoding categorical variables, scaling numerical features, and selecting the most relevant features, the dataset becomes better suited for building accurate and efficient machine learning models.
