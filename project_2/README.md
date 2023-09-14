# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2 - Singapore Housing Data and Kaggle Challenge

## Introduction

In Singapore, Housing and Development Board (HDB) flats are a vital component of the public housing landscape. These flats serve as affordable and accessible housing options for the majority of Singaporeans. HDB flats are not just places to live; they represent a significant part of the Singaporean identity. For many, buying an HDB flat is a milestone and a long-term investment.

## Problem Statement

Predicting the resale prices of HDB flats manually can be an error-prone task due to various factors such as the diverse range of flat types, locations, sizes etc. To make informed decisions in the real estate market, it is crucial to have accurate price predictions.

As a data-driven real estate agency, our team of data scientists has developed a cutting-edge machine learning model. This model provides precise and tailored insights to our clients, ensuring they make informed decisions aligned with their financial preferences.

## Datasets

Source: https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data

* train.csv: 150,534 rows, 78 columns; contains train data with 77 features (flat type, location, floor area etc.) and the resale prices
* test.csv: 16737 rows, 77 columns; contains test data with the same 77 features

## Data Preprocessing

- Discuss the steps you took to clean and preprocess the data.
- Explain how missing values, outliers, and categorical variables were handled.
- Provide code snippets or references to relevant data preprocessing scripts.

## Exploratory Data Analysis (EDA)

- Share visualizations and insights from the exploratory data analysis.
- Highlight any patterns, correlations, or interesting findings in the data.

## Model Development

- Describe the machine learning models and algorithms used for predicting resale prices.
- Explain the model evaluation criteria, such as mean squared error (MSE), root mean squared error (RMSE), and R-squared (R^2).
- Share the results of model training and validation.

## Conclusion

**Predictive Model Accuracy**
- The Linear Regression Model demonstrates the potential to estimate HDB resale prices with reasonable accuracy. 
- However, it can be improved with more sophisticated machine learning techniques like KNN Regressor Model.

**Key Predictors**

According to *SelectKBest*, the top 5 factors to focus on when considering hdb resale prices are:
1. Floor area
2. The HDB flat's age
3. Height of the hdb flat
4. Year completed
5. How many 5 room flats are sold in that flat


**Model Performance**
- The model achieved [mention the metrics, e.g., R-squared (R2)] as indicators of its performance. Investors should be aware of these metrics to gauge the model's reliability.

**Limitations**
- It's important to acknowledge the limitations of the model, such as its reliance on historical data and the assumption of linear relationships. Additionally, real-world property prices are influenced by a wide range of factors beyond those considered in this model.

## Recommendations

**Data Enrichment**
- To enhance the accuracy of price predictions, we can consider including non-numerical features like 'town', 'street_name', and 'planning_area' which are qualitative indicators of location.

**Diversification**
- Emphasize the importance of diversifying investment portfolios. Investors should consider spreading their investments across different types of properties, locations, and asset classes to mitigate risks associated with fluctuations in the HDB resale market.

**Policy Compliance**
- From the second half of 2024, HDB towns will no longer be classified as mature or non-mature. Instead, individual BTO projects within each town will now be classified as Standard, Prime, or Plus flats, depending on their locational attributes. Further study can be done to assess how these new classifications would affect the HDB resale market.

---

For any inquiries or assistance related to HDB flat resale price predictions, please feel free to contact us.
