
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import dcc, html

def parsePrice(price):
    return f'${price:,}'

def generateDropDownrDiv(valueName, labelName, options=[], value=None):
    return html.Div([
        dbc.Label(labelName, className='filter_label'),
        dcc.Dropdown(id=valueName, options=options, value=value, className="filter_input"),
    ])

def generageRangeSliderDiv(valueName, labelName, minValue, maxValue, value=[]):
    if not value:
        value = [minValue, maxValue] 
    return html.Div([
        dbc.Label(labelName, className='filter_label'),
        dcc.RangeSlider(
            id=valueName,
            min=minValue,
            max=maxValue,
            value=value,
            updatemode='drag',
            dots=False,
            marks=None,
            tooltip={
                'always_visible': True,
                'placement': 'bottom',
            },
        )
    ], className="filter_input")


def generateChart(id, spec):
    return dbc.Col([
            dvc.Vega(id=id, spec=spec, style={'width': '100%' }),
        ])
