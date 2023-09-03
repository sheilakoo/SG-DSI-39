# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Exploring Climate Data of Singapore

SG-DSI-39

Mohammad Farhan Bin Rais

### Problem Statement

Army units have to conduct BMT, during which there will be PT sessions conducted. 
However, these sessions can be cancelled due to rain. 
This project aims to explore trends in weather data to determine the number of PT sessions an Army unit should plan for in otder to complete all PT sessions.

### Context

- Army units have to conduct Basic Military Training (BMT) as their first phase of training.
- During BMT, there is a set number of Physical Training (PT) sessions to be completed.
- However, the sessions can be cancelled due to inclement weather, like rain.

**Key Statistics**

1. **1,030** recruits to undergo BMT
2. **16** days of PT to be completed
3. **9** weeks of BMT

**Assumptions**

- BMT is to be conducted in July-August.
- A day is considered to have ‘rained’ if the total rainfall for that day is 0.2mm or more.

### Data Cleaning

1. Checked for missing values
2. Checked for NaN values
3. Converted Dtypes
4. Ammended wrong values/ incorrect data
5. Dropped unnecessary columns
6. Renaming columns
7. Merging dataframes

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|year|*integer*|rainfall-monthly-number-of-rain-days|Year|
|month|*integer*|rainfall-monthly-number-of-rain-days|Month|
|no_of_rainy_days|*integer*|rainfall-monthly-number-of-rain-days|Number of rainy days for that month|
|rain_days_per_month|*float*|rainfall-monthly-number-of-rain-days|Percentage of rainy days for that month|

### Exploratory Data Analysis

- Comparing the number of rainy days in each month over the years, January and February are the driest months while November and December are the wettest.
- July and August, when BMT is to be conducted, are in between the dry and wet seasons.
- The percentage of rainy days have been fluctuating over the years, with no discernible trend.
- There is an average of 44.2% of rainy days in July and August.

### Recommendations and Conclusion

- Given 44.2% chance of rain in July and August, an Army unit should plan for 36 days of PT in order to complete all 16 sessions.
- This should be spread out over 9 weeks, with 4 PT sessions per week, to space out the strenuous activities.
- There should be alternative activities planned in the training program, given the high likelihood of PT cancellation.

### Limitations and Way Ahead

- Rain: Some PT can still be conducted under sheltered areas.
- Temperature: SAF also restricts activities when temperature is > 35°C.
- Lightning alert: SAF uses presence of lightning (CAT 1) as an indicator to cease activities.
- CAT 1 data: Though broadcasted, CAT 1 data is not collated or archived.

### Sources

- Images: [BMTC Facebook](https://www.facebook.com/BMTCSAF)
- Datasets: [Meteorological Services Singapore](http://www.weather.gov.sg/climate-historical-daily/)