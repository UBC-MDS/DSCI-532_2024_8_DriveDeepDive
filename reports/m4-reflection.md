
# Reflection on Final Dashboard Development
## Progress Since Milestone 3

### Implementation and Refinements:

As of the release of our dashboard for Milestone 3, we have put or focuses on enhancing our applications performance as well as user epxerience further. The most notable and universal improvement that we incorporated as per our instructors comments as well as peers, has been the incorporation of parquet data formats in order to expediate the load times. This is critical as it ensures that our users can access our apps insights swiftly, and have a nicer user experience.

We have also made adjustments to our year-range slider, before it gave users the ability to select fractional values - looking at 0.5 of a year doesn't make much sense. We updated it to only represent whole values and align with a more conventional representation of a year.

We also implemented the ability to add states to the filtering our of map through clicking the state, making it more interactive, as well as streamlining the process of filtering.

### Feedback and Usability Enhancements:

To improve experience concerns, we've incorporated a feature where one can hover over elements and this changes the cursor to a pointer - indicating interactivity. This is a helpful cue for guiding new users in using the app.

Understanding the need for clarity aswell, we now display the complete state name within our filtering options, plots, and tooltops. Initially this wasn't used to save space using abbreviations, however, many state abbreviations are similar and hard to take insights from at a glance.

### Unimplemented Advice:

A suggestion we decided not to consider was to reduce the options for `Make` as there were many, and to implement  `Model` instead. We decided not to do this as omitting essential makes that take up a substantial market share would lose sufficient information. There are also too many variations of models by year to display, so this was to save on performance and usability - moving forward maybe a company specific model based dashboard could be implemented.

### Adherence to Best Practices:

Our dashboard design follows an 'F' layout, as recommended in DSCI 531, with filter options on the left and visual plots to the right. This caters to the natural type of eye movement most users follow, and there was no need to deviate from this practice.

### Insights and Feedback Valuation:

We found that the iterative feedback from our peers and unstrcutor was invaluable for refining the app. It allowed us to see our tool through the eyes of potential users, and understand areas of improvement that we, as developers, might have ignored.

### Limitations and Future Improvements:

One limitation is the dashboard's response time, which we aim to further improve with potential use of caching. Future enhancements could also include predictive analytics capabilities, going beyond historical data forecasts. Also maybe displaying some high level model types based on top performers, and including links to aquiring them or their product pages for more information.

### Conclusion:

In conclusion, out dashboard is an great example of strong user centric design as well as data driven decision making to fuel out choice of layout. We believe from our own experience and user testimonys that our app successfully translates raw data into actionable insights, and has the potential to keep developing into an even more impactful tool.