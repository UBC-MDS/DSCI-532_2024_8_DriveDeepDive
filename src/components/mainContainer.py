from dash import html
import dash_bootstrap_components as dbc
from utils import generateChart, parsePrice

total_number_sales = 27523
avg_sale_price = 32752
num_states = 52
num_body_type = 2

mainContainer = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Div('Total Number of Sales'),
                html.Div(total_number_sales, id="total_number_sales", className="summary_highlight"),
            ], className='summary_card_small')
        ]),
        dbc.Col([
            html.Div([
                html.Div('Current Average Sale Price'),
                html.Div(parsePrice(avg_sale_price), id='avg_sale_price', className="summary_highlight"),
            ], className='summary_card_small')
        ]),
        dbc.Col([
            html.Div([
                html.Div('Number of States'),
                html.Div(num_states, id="num_sales", className="summary_highlight"),
            ], className='summary_card_small')
        ]),
        dbc.Col([
            html.Div([
                html.Div('Number of Body Types'),
                html.Div(num_body_type, id='num_body_types', className="summary_highlight"),
            ], className='summary_card_small')
        ]),
    ]),
    dbc.Row([
        generateChart('map', spec={}, width=8, height='400px'),  # Height adjusted to match two stacked charts
        dbc.Col([
            generateChart('line1', spec={}, width=12, height='200px'),  # Height is half of the map's height
            generateChart('line2', spec={}, width=12, height='200px'),  # Height is half of the map's height
        ], width=4),
    ], className="chart_container"),
    dbc.Row([
        generateChart('bar1', spec={}, width=4),
        generateChart('bar2', spec={}, width=4),
        generateChart('histo', spec={}, width=4),
    ], className="chart_container"),
], fluid=True)
