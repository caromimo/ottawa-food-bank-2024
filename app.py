# ------------------------------------------------------------------------------
# import librairies
import pandas as pd
import plotly.express as px

# import plotly.graph_objects as go

from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)


# ------------------------------------------------------------------------------
# import data
df = pd.read_csv("./data/processed/food_security_status_sub_sample.csv")

# ------------------------------------------------------------------------------
# app layout
app.layout = html.Div(
    [
        html.H1(
            "Ottawa Food Bank - 2024 Neighbour Survey Analysis",
            style={"text-align": "center"},
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
# connect the Plotly graphs with Dash Components
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

    dff = df.copy()
    dff = dff[dff["q001"] == language_selection]

    # Plotly Express
    fig = px.histogram(
        data_frame=dff,
        x="food_security_score",
    )

    return container, fig


# ------------------------------------------------------------------------------
# run server
if __name__ == "__main__":
    app.run_server(debug=True)
