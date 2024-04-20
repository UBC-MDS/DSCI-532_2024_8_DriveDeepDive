from dash import html
from constants import data, us_abbrev_to_state
from utils import (
    generateDropDownrDiv,
    generageRangeSliderDiv,
)

sorted_states = sorted(list(data['state'].unique()))
state_option = []
for ab in sorted_states:
    if ab in us_abbrev_to_state:
        state_option.append({ "label": us_abbrev_to_state[ab], "value": ab })

filterArea = html.Div([
        html.Img(src="../assets/logo.jpg", className="logo"),
        html.Div("Drive Deep Dive", className="nav_title"), 
        generateDropDownrDiv(valueName='state', labelName='State:', options=state_option, value=None),
        generateDropDownrDiv(valueName='make', labelName='Make:', options=data['Make'].unique(), value=None),
        generateDropDownrDiv(valueName='quality', labelName='Quality:', options=data['Quality'].unique(), value=None),
        generateDropDownrDiv(valueName='bodyType', labelName='BodyType:', options=data['BodyType'].unique(), value=None),
        generageRangeSliderDiv(valueName='yearRange', labelName='YearRange', minValue=1950, maxValue=2020, value=[]),
        generageRangeSliderDiv(valueName='priceRange', labelName='PriceRange', minValue=0, maxValue=500_000, value=[], isPrice=True),
    ], className="filter_area")
