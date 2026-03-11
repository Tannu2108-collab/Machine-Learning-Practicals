# Multi-Linear Regression Implementation

This project implements *Multi-Linear Regression*, which extends Simple Linear Regression by using multiple independent variables (features) to predict a single outcome.

## 🛠️ Tech Stack
* *Python*
* *Scikit-Learn*
* *NumPy*

## 📂 Project Overview
Multi-Linear Regression models the relationship between two or more independent variables ($X_1, X_2, ..., X_n$) and a dependent variable ($y$). 
The mathematical equation is:
$$y = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_nX_n + \epsilon$$



## 🚀 How to Run
1. Install requirements:
   pip install scikit-learn numpy
2. Run the script:
   python multi_linear.py

## 📊 Logic Explained
* The model calculates the optimal coefficients ($\beta$) for each feature.
* It predicts the target value based on the weighted sum of all inputs.
