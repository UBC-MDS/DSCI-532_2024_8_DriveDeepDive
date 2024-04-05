import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import Dash, callback, Input, Output, dcc, html
from vega_datasets import data
from utils import parsePrice, generateDropDownrDiv, generageRangeSliderDiv

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

cars = data.cars()

total_number_sales = 27523
avg_sale_price = 32752
num_states = 52
num_body_type = 2

html.Div(id='Header', children=[
    html.Link(
        rel='stylesheet',
        href='styles/app.css'
    )
])

filterArea = html.Div([
        generateDropDownrDiv(valueName='state', labelName='State:', value=[]),
        generateDropDownrDiv(valueName='make', labelName='Make:', value=[]),
        generateDropDownrDiv(valueName='mileage', labelName='Mileage:', value=[]),
        generateDropDownrDiv(valueName='bodyType', labelName='BodyType:', value=[]),
        generageRangeSliderDiv(valueName='yearRange', labelName='YearRange', minValue=1950, maxValue=2024, value=[]),
        generageRangeSliderDiv(valueName='priceRange', labelName='PriceRange', minValue=0, maxValue=500_000, value=[]   ),
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
                html.Div(total_number_sales, className="summary_highlight"),
            ], className='summary_card')
        ]),
        dbc.Col([
            html.Div([
                html.Div('Current Average Sale Price'),
                html.Div(parsePrice(avg_sale_price), className="summary_highlight"),
            ], className='summary_card')
        ]),
        dbc.Col([
            dbc.Row([
                html.Div([
                    html.Div('Number of States'),
                    html.Div(num_states, className="summary_highlight"),
                ], className='summary_card_small'),
            ]),
            dbc.Row([
                html.Div([
                    html.Div('Number of States'),
                    html.Div(num_states, className="summary_highlight"),
                ], className='summary_card_small'),
            ])
        ], className="card_column"),
    ]),
    dbc.Row([
        dbc.Col([
            dvc.Vega(id='scatter', spec={}, style={'width': '100%'}),
            dcc.Dropdown(id='x-col', options=cars.columns, value='Horsepower'),
        ])
    ])
])

app.layout = html.Div([
    html.Div([filterArea], className='nav_bar'), 
    html.Div([mainContainer], className='left_div'),
], className='main_div')

@callback(
    Output('scatter', 'spec'),
    Input('x-col', 'value')
)
def create_chart(x_col):
    return (
        alt.Chart(cars, width='container').mark_point().encode(
            x=x_col,
            y='Miles_per_Gallon',
            tooltip='Origin'
        ).interactive().to_dict()
    )


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
