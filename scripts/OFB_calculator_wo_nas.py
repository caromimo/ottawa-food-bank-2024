"""
Script to calculate the food security scores and attribute food security status.
Scores and status are based on the U.S. Household Food Security Survey Module: Six-Item Short Form
Economic Research Service, USDA, September 2012

This script needs to be runned after the OFB_cleaner.py script and the OFB_categorizer script.

Copyright 2024 Caroline Mimeault <carolinemimeault@gmail.com>
SPDX-License-Identifier: MIT
"""

# import librairies
import pandas as pd

# import data
df = pd.read_csv("./data/processed/cleaned_neighbour_survey.csv")

# keep respondents who answered all questions between 3 and 8 inclusively
df = df[df.q003.notnull()]
df = df[df.q004.notnull()]
df = df[df.q005.notnull()]
df = df[df.q006.notnull()]
df = df[df.q007.notnull()]
df = df[df.q008.notnull()]

# set categories for questions 3 and 4
HH_scores = {
    "Sometimes true": 1,
    "Often true": 1,
    "Never true": 0,
    "Prefer not to answer": 0,
    "Don't know": 0,
}

# create new column and replace the values
df["HH3_scores"] = df["q003"].replace(HH_scores)
df["HH3_scores"].value_counts()

# Create new column and replace the values
df["HH4_scores"] = df["q004"].replace(HH_scores)
df["HH4_scores"].value_counts()

# set categories for questions 5, 7 and 8
AD_scores = {
    "Yes": 1,
    "No": 0,
    "Don't know": 0,
    "Prefer not to answer": 0,
}

df["AD1_scores"] = df["q005"].replace(AD_scores)
df["AD1_scores"].value_counts()

df["AD2_scores"] = df["q007"].replace(AD_scores)
df["AD2_scores"].value_counts()

df["AD3_scores"] = df["q008"].replace(AD_scores)
df["AD3_scores"].value_counts()


# set categories for question 6
AD1a_scores = {
    "Some months but not every month": 1,
    "Almost every month": 1,
    "Only 1 or 2 months": 0,
    "Don't know": 0,
    "Prefer not to answer": 0,
    "Never true": 0,
}

# Create new column and replace the values
df["AD1a_scores"] = df["q006"].replace(AD1a_scores)
df["AD1a_scores"].value_counts()

# calculate the food security status
df["food_security_score"] = (
    df["HH3_scores"]
    + df["HH4_scores"]
    + df["AD1_scores"]
    + df["AD1a_scores"]
    + df["AD2_scores"]
    + df["AD3_scores"]
)

df["food_security_score"].value_counts()

# assign food security status based on score
food_security_status = {
    0: "High",
    1: "Marginal",
    2: "Low",
    3: "Low",
    4: "Low",
    5: "Very low",
    6: "Very low",
}

# make the food security status categories
df["food_security_status"] = (
    df["food_security_score"].replace(food_security_status).astype("category")
)
df["food_security_status"].value_counts()
df["food_security_status"].value_counts(normalize=True)

# save the new df
df.to_csv(
    "./data/processed/food_security_status_sub_sample.csv", header=True, index=False
)
