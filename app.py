# import librairies
import pandas as pd
import plotly.express as px
import plotly.io as pio
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

# import data
df = pd.read_csv("./data/processed/food_security_status_sub_sample.csv")

# graphs
fig = px.histogram(df, y="q035a")

# initialise the app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# app layout
app.layout = html.Main(
    [
        html.H1(children="Ottawa Food Bank - 2024 Neighbour Survey Analysis"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="food_security_status_dropdown",
                        options=[
                            {
                                "label": "High or marginal food security",
                                "value": "High/marginal food security",
                            },
                            {
                                "label": "Low food security",
                                "value": "Low food security",
                            },
                            {
                                "label": "Very low food security",
                                "value": "Very low food security",
                            },
                        ],
                        value="Very low food security",
                    )
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="question_dropdown",
                        options=[
                            {"label": "Survey language", "value": "q001"},
                            {"label": "Status in Canada", "value": "q035a"},
                        ],
                        value="q001",
                    )
                ),
            ],
        ),
        dcc.Graph(figure={}, id="graph1"),
    ]
)


# add controls to  build the interactions
@callback(
    Output(component_id="graph1", component_property="figure"),
    Input(component_id="food_security_status_dropdown", component_property="value"),
    Input(component_id="question_dropdown", component_property="value"),
)
def update_graph(food_security_status_dropdown, question_dropdown):
    fig = px.histogram(
        data_frame=df[df["food_security_status"] == food_security_status_dropdown],
        y=question_dropdown,
    )
    return fig


# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
