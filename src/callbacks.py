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
        alt.Chart(us_provinces)
        .mark_geoshape(stroke="white")
        .project("albersUsa", rotate=[90, 0, 0])
        .encode(
            tooltip=("name", "sale"),
            color="sale",  # To avoid repeating colors
            href="wikipedia",
        )
        .configure_title(anchor="start")
        .properties(title="Car Sale Distribution in US", width=900)  # Adding title
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