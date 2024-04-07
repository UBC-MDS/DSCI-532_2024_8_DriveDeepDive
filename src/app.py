import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import Dash, callback, Input, Output, dcc, html
from vega_datasets import data
import pandas as pd
import geopandas as gpd
from utils import (
    parsePrice,
    generateDropDownrDiv,
    generageRangeSliderDiv,
    generateChart,
    filterData,
)

alt.data_transformers.enable("vegafusion")


us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

external_scripts = ["assets/tooltip.js"]

external_stylesheets = [dbc.themes.BOOTSTRAP, "assets/app.css"]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
)

cars = data.cars()
data = pd.read_csv("data/preprocessed/processed_data.csv")

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
    ], className="chart_container"),
    dbc.Row([
        generateChart('histo', spec={}),
        generateChart('bar2', spec={}),
        generateChart('line2', spec={}),
    ], className="chart_container")
])

footer = html.Footer(
    [
        html.Div("""
            DriveDeepDive Dashboard, created by Charles Xu, Chris Gao, Alan Powichrowski and Doris Wang, 
            offers interactive insights into the US used car market.
        """),
        html.Span("For more details, visit our "),
        dcc.Link("Github Repo", href="https://github.com/UBC-MDS/DSCI-532_2024_8_DriveDeepDive", target="_blank"),
        html.Span(" | Last Updated: 2024-Apr-6")
    ],
    className="footer"
)

app.layout = html.Div([
    html.Div([filterArea], className='nav_bar'), 
    html.Div([mainContainer, footer], className='left_div'),
], className='main_div')



@callback(
    Output("total_number_sales", "children"),
    Output("num_states", "children"),
    Output("num_body_types", "children"),
    Output("avg_sale_price", "children"),
    Input("state", "value"),
    Input("make", "value"),
    Input("quality", "value"),
    Input("bodyType", "value"),
    Input("yearRange", "value"),
    Input("priceRange", "value"),
)
def update_statistics(state, make, quality, bodyType, yearRange, priceRange):
    filtered = filterData(data, state, make, quality, bodyType, yearRange, priceRange)
    return (
        filtered.shape[0],
        filtered["state"].nunique(),
        filtered["BodyType"].nunique(),
        parsePrice(round(filtered["pricesold"].mean(), 2)),
    )


@callback(
    Output("map", "spec"),
    Input("state", "value"),
    Input("make", "value"),
    Input("quality", "value"),
    Input("bodyType", "value"),
    Input("yearRange", "value"),
    Input("priceRange", "value"),
)
def create_map(state, make, quality, bodyType, yearRange, priceRange):
    url = "https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_1_states_provinces.zip"
    us_provinces = gpd.read_file(url).query("iso_a2 == 'US'")[
        ["wikipedia", "name", "region", "postal", "latitude", "longitude", "geometry"]
    ]
    filtered = filterData(data, state, make, quality, bodyType, yearRange, priceRange)

    abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))
    df_processed = filtered[filtered["state"] != "AP"]
    df_processed["state_full"] = df_processed["state"].apply(
        lambda x: abbrev_to_us_state[x]
    )
    df_processed = df_processed[df_processed["state_full"] != "Puerto Rico"]

    df_count = df_processed.groupby("state_full").count()["ID"]
    df_count = df_count.reset_index()
    df_count.columns = ["state", "sale"]

    us_provinces["sale"] = 0
    for i in range(len(us_provinces)):
        province = us_provinces.iloc[i, 1]
        filtered_count = df_count[df_count["state"] == province]
        if not filtered_count.empty:
            sale = df_count[df_count["state"] == province].iloc[0, 1]
            us_provinces.iloc[i, -1] = sale

    return (
        alt.Chart(us_provinces, width=600, height=500)
        .mark_geoshape(stroke="white")
        .project("albersUsa", rotate=[90, 0, 0])
        .encode(
            tooltip=("name", "sale"),
            color="sale",  # To avoid repeating colors
            href="wikipedia",
        )
        .properties(width=320, height=300)
        .configure_title(fontSize=16, anchor="start")
        .properties(title="Car Sale Distribution in US")  # Adding title
        .to_dict(format="vega")
    )


@callback(
    Output("bar1", "spec"),
    Output("line1", "spec"),
    Output("histo", "spec"),
    Output("bar2", "spec"),
    Output("line2", "spec"),
    Input("state", "value"),
    Input("make", "value"),
    Input("quality", "value"),
    Input("bodyType", "value"),
    Input("yearRange", "value"),
    Input("priceRange", "value"),
)
def create_charts(state, make, quality, bodyType, yearRange, priceRange):
    filtered = filterData(data, state, make, quality, bodyType, yearRange, priceRange)

    state_counts = (
        filtered["state"]
        .value_counts()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    state_counts.columns = ["State", "Count"]
    bar1 = (
        alt.Chart(state_counts)
        .mark_bar()
        .encode(
            x=alt.X("State:N", title="State", axis=alt.Axis(labelAngle=-45)),
            y=alt.Y("Count:Q", title="Number of Transactions"),
            tooltip=[
                alt.Tooltip("State:N", title="State"),
                alt.Tooltip("Count:Q", title="Number of Transactions"),
            ],
        )
        .properties(
            width="container", title="Number of Transactions in the Top-10 States"
        )
        .to_dict(format="vega")
    )

    line1 = (
        alt.Chart(filtered, width="container")
        .mark_line()
        .encode(
            x=alt.X(
                "Year:O",
                title="Year of Production",
                axis=alt.Axis(
                    values=[year for year in range(1960, 2025, 10)], labelAngle=0
                ),
            ),
            y=alt.Y(
                "count():Q", title="Number of Transactions", axis=alt.Axis(grid=True)
            ),
            tooltip=[
                alt.Tooltip("Year:O", title="Year"),
                alt.Tooltip(
                    "count():Q", title="Total Number of Transaction", format=","
                ),
            ],
            color=alt.value("#4F71BE"),
        )
        .properties(title="Total Number of Transactions: Over Selected Years")
        .configure_axisY(gridDash=[3], gridColor="lightgray")
        .to_dict(format="vega")
    )

    histo = (
        alt.Chart(filtered)
        .mark_bar()
        .encode(
            x=alt.X("pricesold:Q", bin=True, title="Price"),
            y=alt.Y("count()", title="Number of Cars"),
            tooltip=[
                alt.Tooltip("pricesold:Q", title="Price", bin=True),
                alt.Tooltip("count()", title="Number of Cars"),
            ],
        )
        .properties(width="container", title="Distribution of Prices")
        .to_dict(format="vega")
    )

    bar2 = (
        alt.Chart(filtered)
        .mark_bar()
        .encode(
            x=alt.X("Quality:N", title="Quality", axis=alt.Axis(labelAngle=-45)),
            y=alt.Y("count()", title="Number of Cars"),
            color=alt.Color("Quality:N", legend=None),
            tooltip=[
                alt.Tooltip("Quality:N", title="Quality"),
                alt.Tooltip("count()", title="Number of Cars"),
            ],
        )
        .properties(width="container", title="Car Count by Quality")
        .to_dict(format="vega")
    )

    avg_price_by_year = filtered.groupby("Year")["pricesold"].mean().reset_index()

    line2 = (
        alt.Chart(avg_price_by_year, width="container")
        .mark_line()
        .encode(
            x=alt.X(
                "Year:O",
                title="Year of Production",
                axis=alt.Axis(
                    values=[year for year in range(1960, 2025, 10)], labelAngle=0
                ),
            ),
            y=alt.Y(
                "pricesold:Q",
                axis=alt.Axis(
                    title="Average Price",
                    format="$,.0s",
                    labelExpr="datum.value / 1000 + 'k'",
                ),
            ),
            tooltip=[
                alt.Tooltip("Year:O", title="Year"),
                alt.Tooltip("pricesold:Q", title="Average Price", format=","),
            ],
            color=alt.value("#4F71BE"),
        )
        .properties(title="Average Sale Price: Over Selected Years")
        .configure_axisY(gridDash=[3], gridColor="lightgray")
        .to_dict(format="vega")
    )

    return bar1, line1, histo, bar2, line2


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="127.0.0.1")
