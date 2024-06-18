# ------------------------------------------------------------------------------
# # import librairies
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)

# ------------------------------------------------------------------------------
# import data
df = pd.read_csv("data/raw/neighbour_survey_clean-2024-06-14.csv")
print(df[:10])

# ------------------------------------------------------------------------------
# # clean data
# count occurrences of languages
language_count = df.groupby(["q001"]).size()

# display occurrences of a particular column
print(language_count)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div(
    [
        html.H1(
            "Ottawa Food Bank - 2024 Neighbour Survey", style={"text-align": "center"}
        ),
        dcc.Checklist(["Arabic", "English", "French", "Simplified Chinese"]),
        html.Div(id="output_container"),
        html.Br(),
    ]
)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True)
