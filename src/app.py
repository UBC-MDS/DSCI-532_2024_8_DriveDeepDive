import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import Dash, callback, Input, Output, dcc, html
from vega_datasets import data
import pandas as pd
from utils import parsePrice, generateDropDownrDiv, generageRangeSliderDiv, generateChart


external_scripts = [
    'assets/tooltip.js'
]

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    'assets/app.css'
]

app = Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=external_scripts)

cars = data.cars()
data = pd.read_csv('data/preprocessed/processed_data.csv')

total_number_sales = 27523
avg_sale_price = 32752
num_states = 52
num_body_type = 2


filterArea = html.Div([
        generateDropDownrDiv(valueName='state', labelName='State:', options=sorted(list(data['state'].unique())), value=None),
        generateDropDownrDiv(valueName='make', labelName='Make:', options=data['Make'].unique(), value=None),
        generateDropDownrDiv(valueName='quality', labelName='Quality:', options=data['Quality'].unique(), value=None),
        generateDropDownrDiv(valueName='bodyType', labelName='BodyType:', options=data['BodyType'].unique(), value=None),
        generageRangeSliderDiv(valueName='yearRange', labelName='YearRange', minValue=1950, maxValue=2020, value=[]),
        generageRangeSliderDiv(valueName='priceRange', labelName='PriceRange', minValue=0, maxValue=500_000, value=[], isPrice=True),
    ], className="filter_area")


mainContainer = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Div('Used Car Transaction Overview:', className="title"),
                html.Div('Across States in US', className="title")
            ], className="title_box")
        ], md=4),
        dbc.Col([
            html.Div([
                html.Div('Total Number of Sales'),
                html.Div(total_number_sales, id="total_number_sales", className="summary_highlight"),
            ], className='summary_card')
        ]),
        dbc.Col([
            html.Div([
                html.Div('Current Average Sale Price'),
                html.Div(parsePrice(avg_sale_price), id='avg_sale_price', className="summary_highlight"),
            ], className='summary_card')
        ]),
        dbc.Col([
            dbc.Row([
                html.Div([
                    html.Div('Number of States'),
                    html.Div(num_states, id="num_states", className="summary_highlight"),
                ], className='summary_card_small'),
            ]),
            dbc.Row([
                html.Div([
                    html.Div('Number of Body Types'),
                    html.Div(num_body_type, id="num_body_types", className="summary_highlight"),
                ], className='summary_card_small'),
            ])
        ], className="card_column"),
    ]),
    dbc.Row([
        generateChart('map', spec={}),
        generateChart('bar1', spec={}),
        generateChart('line1', spec={}),
        # dbc.Col([
        #     dvc.Vega(id='map', spec={}, style={'width': '100%' }),
        # ]),
        # dbc.Col([
        #     dvc.Vega(id='bar1', spec={}, style={'width': '100%'}),
        # ]),
        # dbc.Col([
        #     dvc.Vega(id='line1', spec={}, style={'width': '100%'}),
        # ]),
    ], className="chart_container"),
    dbc.Row([
        generateChart('histo', spec={}),
        generateChart('bar2', spec={}),
        generateChart('line2', spec={}),
        # dbc.Col([
        #     dvc.Vega(id='histo', spec={}, style={'width': '100%' }),
        # ]),
        # dbc.Col([
        #     dvc.Vega(id='bar2', spec={}, style={'width': '100%'}),
        # ]),
        # dbc.Col([
        #     dvc.Vega(id='line2', spec={}, style={'width': '100%'}),
        # ]),
    ], className="chart_container")
])

app.layout = html.Div([
    html.Div([filterArea], className='nav_bar'), 
    html.Div([mainContainer], className='left_div'),
], className='main_div')


@callback(
    Output('total_number_sales', 'children'),
    Output('num_states', 'children'),
    Output('num_body_types', 'children'),
    Output('avg_sale_price', 'children'),
    Input('state', 'value'),
    Input('make', 'value'),
    Input('quality', 'value'),
    Input('bodyType', 'value'),
    Input('yearRange', 'value'),
    Input('priceRange', 'value'),
)
def update_statistics(state, make, quality, bodyType, yearRange, priceRange):
    filtered = data
    if state:
        filtered = filtered.query('state == @state')
    if make:
        filtered = filtered.query('Make == @make')
    if quality:
        filtered = filtered.query('Quality == @quality')
    if bodyType:
        filtered = filtered.query('BodyType == @bodyType')
    if yearRange:
        filtered = filtered.query('Year >= @yearRange[0] & Year <= @yearRange[1]')
    if priceRange:
        filtered = filtered.query('pricesold >= @priceRange[0] & pricesold <= @priceRange[1]')
    return filtered.shape[0], filtered['state'].nunique(), filtered['BodyType'].nunique(), parsePrice(round(filtered['pricesold'].mean(), 2))




@callback(
    Output('map', 'spec'),
    Input('state', 'value'),
    Input('make', 'value'),
    Input('quality', 'value'),
    Input('bodyType', 'value'),
    Input('yearRange', 'value'),
    Input('priceRange', 'value'),
)
def create_map(state, make, quality, bodyType, yearRange, priceRange):
    return (
        alt.Chart(cars, width='container').mark_point().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            tooltip='Origin'
        ).interactive().to_dict()
    )

@callback(
    Output('bar1', 'spec'),
    Input('state', 'value'),
    Input('make', 'value'),
    Input('quality', 'value'),
    Input('bodyType', 'value'),
    Input('yearRange', 'value'),
    Input('priceRange', 'value'),
)
def create_bar1(state, make, quality, bodyType, yearRange, priceRange):
    return (
        alt.Chart(cars, width='container').mark_point().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            tooltip='Origin'
        ).interactive().to_dict()
    )

@callback(
    Output('line1', 'spec'),
    Input('state', 'value'),
    Input('make', 'value'),
    Input('quality', 'value'),
    Input('bodyType', 'value'),
    Input('yearRange', 'value'),
    Input('priceRange', 'value'),
)
def create_line1(state, make, quality, bodyType, yearRange, priceRange):
    return (
        alt.Chart(cars, width='container').mark_point().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            tooltip='Origin'
        ).interactive().to_dict()
    )


@callback(
    Output('histo', 'spec'),
    Input('state', 'value'),
    Input('make', 'value'),
    Input('quality', 'value'),
    Input('bodyType', 'value'),
    Input('yearRange', 'value'),
    Input('priceRange', 'value'),
)
def create_histogram(state, make, quality, bodyType, yearRange, priceRange):
    return (
        alt.Chart(cars, width='container').mark_point().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            tooltip='Origin'
        ).interactive().to_dict()
    )


@callback(
    Output('bar2', 'spec'),
    Input('state', 'value'),
    Input('make', 'value'),
    Input('quality', 'value'),
    Input('bodyType', 'value'),
    Input('yearRange', 'value'),
    Input('priceRange', 'value'),
)
def create_bar2(state, make, quality, bodyType, yearRange, priceRange):
    return (
        alt.Chart(cars, width='container').mark_point().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            tooltip='Origin'
        ).interactive().to_dict()
    )


@callback(
    Output('line2', 'spec'),
    Input('state', 'value'),
    Input('make', 'value'),
    Input('quality', 'value'),
    Input('bodyType', 'value'),
    Input('yearRange', 'value'),
    Input('priceRange', 'value'),
)
def create_line2(state, make, quality, bodyType, yearRange, priceRange):
    return (
        alt.Chart(cars, width='container').mark_point().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            tooltip='Origin'
        ).interactive().to_dict()
    )


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
