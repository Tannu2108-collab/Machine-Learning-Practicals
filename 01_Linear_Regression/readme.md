# Simple Linear Regression Implementation

This project implements a *Simple Linear Regression* model to learn the direct relationship between input features ($X$) and target values ($y$).

## 🛠️ Tech Stack
* *Python*
* *Scikit-Learn*
* *NumPy*

## 📂 Project Overview
This script demonstrates the basic workflow of a Scikit-Learn model:
1. *Data Preparation:* Creating a simple dataset where the relationship is $y = 2x$.
2. *Model Training:* Fitting a LinearRegression model to the data.
3. *Prediction:* Using the trained model to predict the output for a new input ($X = 5$).

## 🚀 How to Run
1. Ensure you have the required libraries installed:
   pip install scikit-learn numpy
2. Run the script:
   python linear_regression.py

## 📊 Logic Explained
The model learns that for every unit increase in $X$, $y$ increases by a factor of 2. When we input $X=5$, the model predicts:
$$y = 2(5) = 10$$

[attachment_0](attachment)
