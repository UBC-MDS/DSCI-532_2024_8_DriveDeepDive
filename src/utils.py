
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


def generageRangeSliderDiv(valueName, labelName, minValue, maxValue, value=[], isPrice=False):
    if not value:
        value = [minValue, maxValue] 
    if isPrice:
        tooltip = {
            'always_visible': True,
            'placement': 'bottom',
            'transform': 'priceParser'
        }
    else:
        tooltip = {
            'always_visible': True,
            'placement': 'bottom',
        }
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
            tooltip=tooltip,
        )
    ], className="filter_input")


def generateChart(id, spec, width=12, height='400px'):
    return dbc.Col(
        dvc.Vega(id=id, spec=spec, opt={'actions': False}, style={'width': '100%', 'height': height}),
        width=width
    )


def filterData(data, state, make, quality, bodyType, yearRange, priceRange): 
    # filtered = data
    queries = []
    if state:
        queries.append('state == @state')
        # filtered = filtered.query('state == @state')
    if make:
        queries.append('Make == @make')
        # filtered = filtered.query('Make == @make')
    if quality:
        queries.append('Quality == @quality')
        # filtered = filtered.query('Quality == @quality')
    if bodyType:
        queries.append('BodyType == @bodyType')
        # filtered = filtered.query('BodyType == @bodyType')
    if yearRange:
        queries.append('Year >= @yearRange[0] & Year <= @yearRange[1]')
        # filtered = filtered.query('Year >= @yearRange[0] & Year <= @yearRange[1]')
    if priceRange:
        queries.append('pricesold >= @priceRange[0] & pricesold <= @priceRange[1]')
        # filtered = filtered.query('pricesold >= @priceRange[0] & pricesold <= @priceRange[1]')
    filtered = data.query(' & '.join(queries))
    return filtered
