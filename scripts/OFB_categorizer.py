"""
Script providing additional cleaning steps to the OFB dataset.
It needs to be runned after the OB_cleaner.py script.

Copyright 2024 Caroline Mimeault <carolinemimeault@gmail.com>
SPDX-License-Identifier: MIT
"""

# import librairies
import pandas as pd

# import data
df = pd.read_csv("./data/processed/cleaned_neighbour_survey.csv")

# collapsing categories together in q035a
df.loc[df["q035a"] == "Other (please specify)", "q035a"] = (
    "Prefer not to answer or other"
)
df.loc[df["q035a"] == "Prefer not to answer", "q035a"] = "Prefer not to answer or other"
df.loc[df["q035a"] == "Other", "q035a"] = "Prefer not to answer or other"
df.loc[df["q035a"] == "Refugee", "q035a"] = "Refugee (confirmed and applying)"
df.loc[df["q035a"] == "Applying for refugee status", "q035a"] = (
    "Refugee (confirmed and applying)"
)
# df["q035a"] = df["q035a"].map(
#     {
#         "Other (please specify)": "Prefer not to answer or other",
#         "Prefer not to answer": "Prefer not to answer or other",
#         "Other": "Prefer not to answer or other",
#     }
# )

# saved processed data to csv file
df.to_csv("./data/processed/cleaned_neighbour_survey.csv", header=True, index=False)
