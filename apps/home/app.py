import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    html.Label("HOME APP"),
    dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'},
        {'label': 'Belém', 'value': 'BL'}
    ],
    multi=True,
    value="MTL"
)
])

