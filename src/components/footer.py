from dash import html, dcc

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
