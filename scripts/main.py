# ------------------------------------------------------------------------------
# Import librairies
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)

# ------------------------------------------------------------------------------
# Import data
data = pd.read_csv("data/raw/neighbour_survey_clean-2024-06-14.csv")
df = pd.DataFrame(data)
print(df[:5])
print(type(df))

# ------------------------------------------------------------------------------
# # Count language occurrences
survey_languages = df.groupby("q001").size()
# the above returned a series:
print(type(survey_languages))
# convert the series back to a df:
survey_languages = survey_languages.reset_index()
print(type(survey_languages))
# rename the columns:
column_names = ["Language", "Count"]
survey_languages = survey_languages.rename(columns={"q001": "Language", 0: "Count"})
print(survey_languages)

# ------------------------------------------------------------------------------
# Bar plot of survey languages
fig = px.bar(survey_languages, x="Language", y="Count")
fig.show()

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div(
    [
        html.H1(
            "Ottawa Food Bank - 2024 Neighbour Survey", style={"text-align": "center"}
        ),
        dcc.Checklist(["Arabic", "English", "French", "Simplified Chinese"]),
        html.Div(id="output_container", children=[]),
        html.Br(),
        dcc.Graph(id="my_bee_map", figure=fig),
    ]
)


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True)
