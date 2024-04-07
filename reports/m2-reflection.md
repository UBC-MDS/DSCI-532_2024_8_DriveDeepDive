
### Reflection on Dashboard Implementation

**Implemented Features:**

We're thrilled to share an update on our dashboard project, where we've turned our sketches into a dynamic and interactive tool. The structure of our dashboard reflects our initial vision, offering a user-friendly experience and clear navigation. As we designed in Milestone 1, we have successfully implemented the following features:

* **Geographical Heatmap:** Our dashboard features a vibrant heatmap that showcases the volume of sales across different states.
* **Sale Price Distribution:** Users can view and analyze the distribution of sale prices, gaining insights into market trends.
* **Top 10 States Analysis:** We have a detailed bar chart revealing the states with the highest transaction volumes, offering targeted insights at a glance.
* **Time Series Analysis:** A line plot illustrates the number of transactions and average sale price over the years, providing a historical perspective on market dynamics.
* **Interactive Filters:** We've included responsive filters for state location, vehicle make, mileage, body type, and sliders for year range and price range, enabling users to tailor the data view to their specific queries.
* **Summary Widgets:** The dashboard's top corner is adorned with widgets that highlight the total number of sales, average price, number of states, and body types represented in the filtered data sample.

**Changed Features:**

Instead of having distribution of sale price over body type, we finally decided to present it by car quality, which is classified by mileage into four distinct categories—new, moderately used, slightly used, and very used—serves as a more direct indicator of a vehicle's condition and potential value to a buyer. By focusing on quality, we allow users to quickly assess the value proposition of a car, a utility that body type data alone could not offer with the same immediacy.

**Pending Features:**

Additionally, we acknowledge that our current layout and color theme have not yet achieved the high professional standard we set out in our initial sketches. The planned aesthetic, designed to embody a polished, business-like style, is crucial to the user experience we aim to provide. We are actively refining the visual elements to align with the sophisticated feel of a top-tier business tool, ensuring that our final product not only delivers on functionality but also on the professional presentation that our users deserve.

**Difficulties and Challenges**

1. The raw data, a rich seam mined from eBay, came with its share of complexities. We devoted countless hours to sanitizing strings that lacked consistency, deducing cryptic labels, and interpreting zip codes that veered from standard formats. This painstaking task demanded the aid of additional Python libraries to accurately map out state codes from the labyrinth of zip codes.
2. Contrary to our initial assumptions, the sales price data didn't conform to a neat bell curve but rather skewed right, displaying an atypical distribution. When filters were applied, the scarcity of data points posed a significant challenge, making it difficult to extract meaningful inferences and potentially impacting the user's analytical journey.

The initial vision of our dashboard underwent a transformation when faced with the ground realities of implementation. One of our most challenging moments was reconciling the idealistic sketches with the pragmatic aspects of data and design. Ensuring that the dashboard remained user-friendly while managing a heavy load of backend data processing required creative compromises and adaptive strategies.

**Deviations from Best Practices:**

In our dashboard's 3x2 layout featuring six distinct visual analytics, we've taken a creative liberty with our axes and scales. This diverges from the conventional wisdom imparted in DSCI 531, which emphasizes the importance of maintaining consistent scales and axes for comparative visualizations. We elected this approach for the following reasons:

1. Each visualization is designed to provide the most contextually relevant information, which at times necessitated diverging scales to best represent the underlying data characteristics. For instance, the sale price distribution required a scale sensitive enough to capture the high variability and outliers present in the data.
2. We aimed to ensure that each chart remains legible and informative within its own narrative. Due to the wide range of values, a uniform scale would have rendered some charts less comprehensible, with smaller values becoming indiscernible. By adapting the scales, we maintain the readability of each visualization, allowing for nuanced insights even when dealing with disparate value ranges.

**Successes and Limitations:**
The integration of interactive filtering controls is a significant triumph for our dashboard. Users can dynamically adjust the dataset based on various attributes like state, make, and year, providing them with the power to tailor the information to their specific needs. This interactivity enhances user engagement and ensures that our dashboard delivers valuable insights tailored to individual queries.

One notable limitation of our dashboard is its 2x3 layout configuration. By presenting six pieces of information with equal prominence, we inadvertently communicate that all metrics hold the same level of importance. This layout choice can overwhelm users and obscure critical data insights, as it doesn’t guide the user's attention to the most pertinent information first. A more strategic design would be to hierarchically arrange visual elements, emphasizing key data points that demand immediate attention and allowing secondary information to support the narrative. Enhancing our layout to direct user focus more effectively could significantly improve the dashboard's communicative power and user experience.

Another area for enhancement is the incorporation of predictive analytics. Currently, the dashboard excels at presenting historical data but falls short in forecasting future trends. Integrating machine learning models to predict future car sales and price trends could make the dashboard an invaluable tool for strategic planning and market analysis.
