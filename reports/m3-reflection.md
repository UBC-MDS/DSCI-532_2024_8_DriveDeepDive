
# Reflection on Dashboard
## Progress Since Milestone 2

Since our last update and implementation of our dashboard we have made a number of enhancements and updates to our dashboard, given some thoughtful thinking and the feedback we have recieved through Joel and our peers.

### Implemented Features:**

**Redesign Header and Title Section**: As per the feed back received from joel, we have made updates to our styling and design of the header and title section. In order to make our dashboard clear and more aesthetic, we moved the dashboard title to be positioned over the sidebare filter selection area. This allowed us to reduce the visual clutter of the title being next to our KPI cards, and created a more organized entry point for our users.

**Heat Map Highlighting Fix**: We have fixed a shortcoming of our geographical heatmap. When users would selected states of interest to filter by, our heat map would display the values of those states, however, it would also display "0" for the states not selected. This was misleading because it gives the impression that the unsleceted tates have counts of "0" in terms of sales - while they should actually be NA or greyed' out. So we have made an update there.

**Layout Improvments:** Given a number of comments related to our dahboards cluttered nature, and the fact that our geographical heat map was quite small - we updated and restructued our dashboard for a better visual flow and use experience. The map has bee given double the space so that it is easier to see and gain insights from. The heatmap is now complemented by an adjacent time-series line chart in the column next to it, while our bar charts are line in the row below the heat map and the line chart to reduce clutter and create a better visual appeal.

**Visual Enhancements:** We have also changed the styling of our dashboard - the headers now feature a white background along with distinct boarders around our metric cards. This helps our dashboard adhere to a more modern look as discussed with with Joel, and results in a cleaner design and better readability.

### Deviations and Rationale

**Geographical Heatmap Adjustment**: Originally our non-selected states in our heatmap showed a zero value which led to confusion - we have updated this to grey out unselected states, with no value associated with them to avoid any minsinterpretation of data presence vs. absense.

**Sorting Bar Charts**: We have also diverged from our initial dashboard layout to implement sorted bar charts - this was informed by standard best data visualization practices we learned in our previous Visualization 1 course. We want to emphasize the underlying data hierarchies found in our data, and emphasize clarity and immediate comprehension of the data at hand post filtering. 

### Current Limitations + Future Directions:

Our dashboard at it's current state is very robust and informative in-terms of showing historical sales data with dynamic interactivity - however there are some short commings:

**Performance**: Our dashboard is not very fast and responsive, when filtering is made the dashboard takes quite some time to update and display the new values and plots. This being said we would like to look into implementing methods to improve the performance of our dashboard and the speed at which it laods - we would like to explore pre-calculating the results, or possible using caching to improve the performance.

**Predictive Functionality:** Our dashboard as it is showcases current metrics and results, however the ability to perform forecasting on car trends would be a valuable feature. Moving forwards we would like to implement a possible model that forecasts car sales, or possible predicts the value of a vehicle given a certain set of metrics. This would help our users make more informed and strategic decisions.

**Heat Map Selection**: We would like to make our geographical heat map more interactive, possible incorporate a dropdown menu that can be accessed from click on the map itself - or some more interactive functionality that selects states of interest by clicking on them from the map itself. This would refine the user experience and allow for multiple selection and deselections in an easier way.

In conclusion our dashboard excels in offering an engaging and interactive experience which allows our users to manipulate the data in order to uncover custom insights. Our dashboard simplifies a complex dataset into a much more digestible visual story, highlight the trends and metrics that define the current used car market. We believe it is a truly effective tool for diverse user queries, which will result in fruitful results! 