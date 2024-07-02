"""
Script providing additional cleaning steps to the OFB dataset.
It needs to be runned after the OB_cleaner.py script.

Copyright 2024 Caroline Mimeault <carolinemimeault@gmail.com>
SPDX-License-Identifier: MIT
"""

# import librairies
import pandas as pd

# import data
df = pd.read_csv("./data/processed/food_security_status_sub_sample.csv")

# collapsing categories together in q035a
df["q035a"] = df["q035a"].replace("Other (please specify)", "Other")
df["q035a"] = df["q035a"].replace("Other", "Others and prefer not to answer")
df["q035a"] = df["q035a"].replace("Prefer not to answer", "Others and not to answer")


# saved processed data to csv file
df.to_csv("./data/processed/cleaned_neighbour_survey.csv", header=True)
