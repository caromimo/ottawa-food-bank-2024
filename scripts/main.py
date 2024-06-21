# ------------------------------------------------------------------------------
# Import librairies
import pandas as pd
import plotly.express as px

# import plotly.graph_objects as go

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
# figure = px.bar(survey_languages, x="Language", y="Count")

# ------------------------------------------------------------------------------
# app layout
app.layout = html.Div(
    [
        html.H1(
            "Ottawa Food Bank - 2024 Neighbour Survey", style={"text-align": "center"}
        ),
        dcc.Dropdown(
            id="language_selection",
            options=[
                {"label": "Arabic", "value": "Arabic"},
                {"label": "English", "value": "English"},
                {"label": "French", "value": "French"},
                {"label": "Simplified Chinese", "value": "Simplified Chinese"},
            ],
            multi=False,
            value="English",
            style={"width": "50%"},
        ),
        html.Div(id="output_container", children=[]),
        html.Br(),
        dcc.Graph(id="language_plot", figure={}),
    ]
)


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [
        Output(component_id="output_container", component_property="children"),
        Output(component_id="language_plot", component_property="figure"),
    ],
    [Input(component_id="language_selection", component_property="value")],
)
def update_graph(language_selection):
    print(language_selection)
    print(type(language_selection))

    container = "The language chosen by user was: {}".format(language_selection)

    dff = survey_languages.copy()
    dff = dff[dff["Language"] == language_selection]

    # Plotly Express

    fig = px.bar(
        data_frame=survey_languages,
        x="Language",
        y="Count",
    )

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True)
