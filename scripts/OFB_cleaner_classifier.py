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

# # clean data
# df.q003 = df.q003.str.lower()
# df.q004 = df.q004.str.lower()
# df.q005 = df.q005.str.lower()
# df.q006 = df.q006.str.lower()
# df.q007 = df.q007.str.lower()
# df.q008 = df.q008.str.lower()
# df.q009 = df.q009.str.lower()
# df.q011a = df.q011a.str.lower()

# saved processed data to csv file
# df.to_csv("test_clean_data.csv", index=False)
