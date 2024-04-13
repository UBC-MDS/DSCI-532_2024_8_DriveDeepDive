from dash import html
from constants import data
from utils import (
    generateDropDownrDiv,
    generageRangeSliderDiv,
)

filterArea = html.Div([
        html.Div("Used Car Transaction Dashboard", className="nav_title"), 
        generateDropDownrDiv(valueName='state', labelName='State:', options=sorted(list(data['state'].unique())), value=None),
        generateDropDownrDiv(valueName='make', labelName='Make:', options=data['Make'].unique(), value=None),
        generateDropDownrDiv(valueName='quality', labelName='Quality:', options=data['Quality'].unique(), value=None),
        generateDropDownrDiv(valueName='bodyType', labelName='BodyType:', options=data['BodyType'].unique(), value=None),
        generageRangeSliderDiv(valueName='yearRange', labelName='YearRange', minValue=1950, maxValue=2020, value=[]),
        generageRangeSliderDiv(valueName='priceRange', labelName='PriceRange', minValue=0, maxValue=500_000, value=[], isPrice=True),
    ], className="filter_area")
