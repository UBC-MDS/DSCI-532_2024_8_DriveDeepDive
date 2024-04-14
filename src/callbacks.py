import altair as alt
from dash import callback, Input, Output
import pandas as pd
import geopandas as gpd
from constants import us_state_to_abbrev, data
from utils import parsePrice, filterData

alt.data_transformers.enable("vegafusion")


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
    # Load US states data
    url = "https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_1_states_provinces.zip"
    us_provinces = gpd.read_file(url).query("iso_a2 == 'US'")[
        ["name", "geometry"]
    ]

    # Filter your data
    filtered = filterData(data, state, make, quality, bodyType, yearRange, priceRange)

    # Map state abbreviations to full names
    abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))
    filtered['state_full'] = filtered['state'].map(abbrev_to_us_state)
    filtered = filtered[filtered['state_full'] != 'Puerto Rico']

    # Aggregate sales data by state
    df_count = filtered.groupby('state_full').size().reset_index(name='sales')

    # Join sales data with the geodata
    us_provinces = us_provinces.merge(df_count, how='left', left_on='name', right_on='state_full')
    us_provinces['sales'] = us_provinces['sales'].fillna(0)  # Replace NaN with 0

    # Create interactive selection
    select_state = alt.selection_single(fields=['name'], name='select_state', 
                                        on='click', clear='dblclick')

    # Define the chart
    chart = alt.Chart(us_provinces).mark_geoshape(stroke='white').encode(
        tooltip=[alt.Tooltip('name:N'), alt.Tooltip('sales:Q')],
        color=alt.condition(
        alt.datum.sales > 0,  # Condition to check if sales are greater than 0
        alt.Color('sales:Q', scale=alt.Scale(scheme='viridis'), legend=alt.Legend(title='Number of Sales')),
        alt.value('lightgray')),
        opacity=alt.condition(select_state, alt.value(0.9), alt.value(0.2))
    ).add_selection(
        select_state
    ).properties(
        title='Car Sale Distribution in US',
        width=700,
        height=400
    ).project(
        type='albersUsa'
    )
    return chart.to_dict(format="vega")



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
            x=alt.X("State:N", title="State",sort=alt.EncodingSortField(field="Count", order="descending"), axis=alt.Axis(labelAngle=-45)),
            y=alt.Y("Count:Q", title="Number of Transactions"),
            tooltip=[
                alt.Tooltip("State:N", title="State"),
                alt.Tooltip("Count:Q", title="Number of Transactions"),
            ],
        )
        .properties(
            title="Number of Transactions in the Top-10 States", width='container'
        )
        .to_dict(format="vega")
    )

    line1 = (
        alt.Chart(filtered)
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
        .properties(title="Total Number of Transactions: Over Selected Years", width='container', height='container')
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
        .properties(title="Distribution of Prices", width='container')
        .to_dict(format="vega")
    )

    bar2 = (
        alt.Chart(filtered)
        .mark_bar()
        .encode(
            x=alt.X("Quality:N", title="Quality", sort='-y', axis=alt.Axis(labelAngle=-45)),
            y=alt.Y("count()", title="Number of Cars"),
            color=alt.Color("Quality:N", legend=None),
            tooltip=[
                alt.Tooltip("Quality:N", title="Quality"),
                alt.Tooltip("count()", title="Number of Cars"),
            ],
        )
        .properties(title="Car Count by Quality", width='container')
        .to_dict(format="vega")
    )

    avg_price_by_year = filtered.groupby("Year")["pricesold"].mean().reset_index()

    line2 = (
        alt.Chart(avg_price_by_year)
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
        .properties(title="Average Sale Price: Over Selected Years", width='container', height='container')
        .configure_axisY(gridDash=[3], gridColor="lightgray")
        .to_dict(format="vega")
    )

    return bar1, line1, histo, bar2, line2