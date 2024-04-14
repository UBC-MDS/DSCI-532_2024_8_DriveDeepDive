
import dash_bootstrap_components as dbc
from dash import Dash, html
from callbacks import *
from components.filterArea import filterArea
from components.mainContainer import mainContainer
from components.footer import footer


external_scripts = ["assets/tooltip.js"]
external_stylesheets = [dbc.themes.BOOTSTRAP, "assets/app.css"]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
)
server = app.server

app.layout = html.Div([
    html.Div([filterArea], className='nav_bar'), 
    html.Div([mainContainer, footer], className='left_div'),
], className='main_div')


if __name__ == "__main__":
    app.run(debug=False, port=8000, host="127.0.0.1")
