# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 2 - Singapore Housing Data and Kaggle Challenge

## Introduction

In Singapore, Housing and Development Board (HDB) flats are a vital component of the public housing landscape. These flats serve as affordable and accessible housing options for the majority of Singaporeans. HDB flats are not just places to live; they represent a significant part of the Singaporean identity. For many, buying an HDB flat is a milestone and a long-term investment.

## Problem Statement

The decision to buy or sell a property is influenced by a multitude of factors. From location and property type to market trends and economic indicators, the complexities involved can often leave individuals and investors grappling with uncertainty.

Units selling at a million dollars? What factors drove to sell at such high prices? Is it the size of the room in each flat... or maybe it's more to do with the amenities?

It is in this ever-changing landscape that our role as real estate advisors comes to the forefront. As a data-driven real estate advisory group, our dedicated team of data scientists developed a state-of-the-art machine learning model that provides precise and tailored insights to our clients, ensuring they make informed decisions aligned with their financial preferences.

## Datasets

Source: https://www.kaggle.com/competitions/dsi-sg-project-2-regression-challenge-hdb-price/data

* train.csv: 150,534 rows, 78 columns; contains train data with 77 features (flat type, location, floor area etc.) and the resale prices
* test.csv: 16737 rows, 77 columns; contains test data with the same 77 features

## Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**id**|*integer*|HDB|unique id for each transaction|
|**tranc_yearmonth**|*string*|HDB|year and month of the resale transaction, e.g. 2015-02|
|**town**|*string*|HDB|HDB township where the flat is located, e.g. BUKIT MERAH|
|**flat_type**|*string*|HDB|type of the resale flat unit, e.g. 3 ROOM|
|**block**|*string*|HDB|block number of the resale flat, e.g. 454|
|**street_name**|*string*|HDB|street name where the resale flat resides, e.g. TAMPINES ST 42|
|**storey_range**|*string*|HDB|floor level (range) of the resale flat unit, e.g. 07 TO 09|
|**floor_area_sqm**|*float*|HDB|floor area of the resale flat unit in square metres|
|**flat_model**|*string*|HDB|HDB model of the resale flat, e.g. Multi Generation|
|**lease_commence_date**|*integer*|HDB|commencement year of the flat unit's 99-year lease|
|**resale_price**|*float*|HDB|the property's sale price in Singapore dollars|
|**tranc_year**|*integer*|HDB|year of resale transaction|
|**tranc_month**|*integer*|HDB|month of resale transaction|
|**mid_storey**|*integer*|HDB|median value of storey_range|
|**lower**|*integer*|HDB|lower value of storey_range|
|**upper**|*integer*|HDB|upper value of storey_range|
|**mid**|*integer*|HDB|middle value of storey_range|
|**full_flat_type**|*string*|HDB|combination of flat_type and flat_model|
|**address**|*string*|HDB|combination of block and street_name|
|**floor_area_sqft**|*float*|HDB|floor area of the resale flat unit in square feet|
|**price_per_sqft**|*float*|HDB|the property's price per square feet in Singapore dollars|
|**hdb_age**|*integer*|HDB|number of years from lease_commence_date to present year|
|**max_floor_lvl**|*integer*|HDB|highest floor of the resale flat|
|**year_completed**|*integer*|HDB|year which construction was completed for resale flat|
|**residential**|*string*|HDB|boolean value if resale flat has residential units in the same block|
|**commercial**|*string*|HDB|boolean value if resale flat has commercial units in the same block|
|**market_hawker**|*string*|HDB|boolean value if resale flat has a market or hawker centre in the same block|
|**multistorey_carpark**|*string*|HDB|boolean value if resale flat has a multistorey carpark in the same block|
|**precinct_pavilion**|*string*|HDB|boolean value if resale flat has a pavilion in the same block|
|**total_dwelling_units**|*integer*|HDB|total number of residential dwelling units in the resale flat|
|**1room_sold**|*integer*|HDB|number of 1-room residential units in the resale flat|
|**2room_sold**|*integer*|HDB|number of 2-room residential units in the resale flat|
|**3room_sold**|*integer*|HDB|number of 3-room residential units in the resale flat|
|**4room_sold**|*integer*|HDB|number of 4-room residential units in the resale flat|
|**5room_sold**|*integer*|HDB|number of 5-room residential units in the resale flat|
|**exec_sold**|*integer*|HDB|number of executive type residential units in the resale flat block|
|**multigen_sold**|*integer*|HDB|number of multi-generational type residential units in the resale flat block|
|**studio_apartment_sold**|*integer*|HDB|number of studio apartment type residential units in the resale flat block|
|**1room_rental**|*integer*|HDB|number of 1-room rental residential units in the resale flat block|
|**2room_rental**|*integer*|HDB|number of 2-room rental residential units in the resale flat block|
|**3room_rental**|*integer*|HDB|number of 3-room rental residential units in the resale flat block|
|**other_room_rental**|*integer*|HDB|number of "other" type rental residential units in the resale flat block|
|**postal**|*string*|HDB|postal code of the resale flat block|
|**latitude**|*float*|HDB|Latitude based on postal code|
|**longitude**|*float*|HDB|Longitude based on postal code|
|**planning_area**|*string*|HDB|Government planning area that the flat is located|
|**mall_nearest_distance**|*float*|HDB|distance (in metres) to the nearest mall|
|**mall_within_500m**|*float*|HDB|number of malls within 500 metres|
|**mall_within_1km**|*float*|HDB|number of malls within 1 kilometre|
|**mall_within_2km**|*float*|HDB|number of malls within 2 kilometre|
|**hawker_nearest_distance**|*float*|HDB|distance (in metres) to the nearest hawker centre|
|**hawker_within_500m**|*float*|HDB|number of hawker centres within 500 metres|
|**hawker_within_1km**|*float*|HDB|number of hawker centres within 1 kilometre|
|**hawker_within_2km**|*float*|HDB|number of hawker centres within 2 kilometre|
|**hawker_food_stalls**|*integer*|HDB|number of hawker food stalls in the nearest hawker centre|
|**hawker_market_stalls**|*integer*|HDB|number of hawker and market stalls in the nearest hawker centre|
|**mrt_nearest_distance**|*float*|HDB|distance (in metres) to the nearest MRT station|
|**mrt_name**|*string*|HDB|name of the nearest MRT station|
|**bus_interchange**|*integer*|HDB|boolean value if the nearest MRT station is also a bus interchange|
|**mrt_interchange**|*integer*|HDB|boolean value if the nearest MRT station is a train interchange station|
|**mrt_latitude**|*float*|HDB|latitude (in decimal degrees) of the the nearest MRT station|
|**mrt_longitude**|*float*|HDB|longitude (in decimal degrees) of the nearest MRT station|
|**bus_stop_nearest_distance**|*float*|HDB|distance (in metres) to the nearest bus stop|
|**bus_stop_name**|*string*|HDB|name of the nearest bus stop|
|**bus_stop_latitude**|*float*|HDB|latitude (in decimal degrees) of the the nearest bus stop|
|**bus_stop_longitude**|*float*|HDB|longitude (in decimal degrees) of the nearest bus stop|
|**pri_sch_nearest_distance**|*float*|HDB|distance (in metres) to the nearest primary school|
|**pri_sch_name**|*string*|HDB|name of the nearest primary school|
|**vacancy**|*integer*|HDB|number of vacancies in the nearest primary school|
|**pri_sch_affiliation**|*integer*|HDB|boolean value if the nearest primary school has a secondary school affiliation|
|**pri_sch_latitude**|*float*|HDB|latitude (in decimal degrees) of the the nearest primary school|
|**pri_sch_longitude**|*float*|HDB|longitude (in decimal degrees) of the nearest primary school|
|**sec_sch_nearest_dist**|*float*|HDB|distance (in metres) to the nearest secondary school|
|**sec_sch_name**|*string*|HDB|name of the nearest secondary school|
|**cutoff_point**|*integer*|HDB|PSLE cutoff point of the nearest secondary school|
|**affiliation**|*integer*|HDB|boolean value if the nearest secondary school has an primary school affiliation|
|**sec_sch_latitude**|*float*|HDB|latitude (in decimal degrees) of the the nearest secondary school|
|**sec_sch_longitude**|*float*|HDB|longitude (in decimal degrees) of the nearest secondary school|

## Conclusion

**Predictive Model Accuracy**
- The Linear Regression Model demonstrates the potential to estimate HDB resale prices with reasonable accuracy. 
- However, it can be improved with more sophisticated machine learning techniques like KNN Regressor Model.

**Key Predictors**

According to *SelectKBest*, the top 5 factors to focus on when considering hdb resale prices are:
1. Floor area
2. The HDB flat's age
3. Height of the hdb flat
4. Year completed
5. How many 5 room flats are sold in that flat


**Model Performance**
- The model achieved [mention the metrics, e.g., R-squared (R2)] as indicators of its performance. Investors should be aware of these metrics to gauge the model's reliability.

**Limitations**
- It's important to acknowledge the limitations of the model, such as its reliance on historical data and the assumption of linear relationships. Additionally, real-world property prices are influenced by a wide range of factors beyond those considered in this model.

## Recommendations

**Data Enrichment**
- To enhance the accuracy of price predictions, we can consider including non-numerical features like 'town', 'street_name', and 'planning_area' which are qualitative indicators of location.

**Diversification**
- Emphasize the importance of diversifying investment portfolios. Investors should consider spreading their investments across different types of properties, locations, and asset classes to mitigate risks associated with fluctuations in the HDB resale market.

**Policy Compliance**
- From the second half of 2024, HDB towns will no longer be classified as mature or non-mature. Instead, individual BTO projects within each town will now be classified as Standard, Prime, or Plus flats, depending on their locational attributes. Further study can be done to assess how these new classifications would affect the HDB resale market.

---

For any inquiries or assistance related to HDB flat resale price predictions, please feel free to contact us.
