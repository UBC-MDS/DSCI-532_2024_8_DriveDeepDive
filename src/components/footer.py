from dash import html, dcc

footer = html.Footer(
    [
        html.Div("""
            DriveDeepDive Dashboard, created by Charles Xu, Chris Gao, Alan Powichrowski, and Doris Wang, 
            offers interactive insights into the US used car market.
        """),
        html.Span("For more details, visit our "),
        dcc.Link("Github Repo", href="https://github.com/UBC-MDS/DSCI-532_2024_8_DriveDeepDive", target="_blank"),
        html.Span(" | Last Updated: 2024-Apr-20"),
        html.Div("*Footnote: Car quality is classified into four categories based on mileage: 'New' (0-20,000 miles), 'Slightly Used' (20,001-50,000 miles), 'Moderately Used' (50,001-100,000 miles), and 'Very Used' (over 100,000 miles).", 
                 style={'marginTop': '10px', 'fontSize': 'small', 'color': 'gray'})
    ],
    className="footer"
)
