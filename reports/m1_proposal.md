# Project Proposal

## Motivation and Purpose (Alan)

To be added

## Description of the data (Doris)

The dataset we select for our dashboard was sourced from eBay, which consists of numerous variables and metrics pertaining to car sold online. The dataset is comprised of approximately 160,000 observations of used cars sold in the United States – the data set is described to span 20 months between 2019 and 2020, however we see a number of sales in 2018 as well during our EDA. Some variables included are:

**Basic Car Details/Description:** Make, Model, Mileage, Year, Engine, Trim level, Body Style.  
  
**Sales Information:** Price car was sold for, Year the car was sold, ZIP code (location) of sale.

The dataset is comprised of both numerical and categorical features, for example `price sold` and `mileage` (continuous variable). As well as `make`, ‘body style`, and `model` (categorical variable) – as well as `year of sale` (temporal time-series variable).  
  
In our dashboard we plan to focus on the key variables that influence a cars sale and pricing, this includes variables such as `make`, `model`, `body style`, `year`, and `mileage`.  These variables are extremely important for understanding market trends, possible pricing strategies to employ, as well as the behaviour and preferences of consumers in the 2nd hand card market. We will also rely on `ZIP Code` to understand the spatial relationship and nature of car sales, to understand what geographies look for certain types of cars, and which locations have the highest demand for cars.   
  
One variable we look to derive and engineer for our visualization is `Price Range`, which will serve to categorize and bin the various cars sold into price brackets related to their level of ‘luxury’. This variable will include values such as: ‘economy’, ‘mid range’, and ‘luxury’. This variable will help us understand and segment the market trends and understand patterns within the groups to know what level of vehicle consumers are looking for when buying 2nd hand. We will also be looking to make use of the `ZIP Code` variable and converting it to a usable Coordinate Reference System, preferably a linear CRS so that we can model and display sales within the United States, since we are not working on a global scale where angular units would be useful. 

## Research questions and usage scenarios (Charles)

To be added

## App sketch & brief description (Chris)

To be added
