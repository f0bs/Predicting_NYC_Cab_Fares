# Taxi Fares in NYC

## Objective

What can we predict about a cab fare simply based on the pick-up location and the ?
We tested:
* fare prediction
* tip amount
* higher or lower fare (compared to median of $9.80)
* tip or no top for next ride 

## The Data

We used NYC's public TLC data that can be downloaded on [NYC.gov](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). We used 2015 data as this was the last year in which the TLC provided lat and long coordinates. Each monthly dataset contains about 2GB of data.

| ID                    | Description                                    |
|-----------------------|------------------------------------------------|
| vendorID              | TPEP provider                                  |
| tpep_pickup_datetime  | Date & Time of pickup                          |
| payment_type          | Payment method (ex: 1 = credit card, 2 = cash) |
| tpep_dropoff_datetime | Date & Time of dropoff                         |
| fare_amount           | Time-and-distance fare calculated by meter     |
| passenger_count       | Number of passengers                           |
| extra                 | Other extras and surcharges                    |
| trip_distance         | Miles reported by taximeter                    |
| mta_tax               | $0.50 MTA tax by metered rate in use           |
| ratecodeID            | Final rate code (ex: 1 = Standard, 2 = JFK)    |
| tip_amount            | Tip amount (cash tips not included)            |
| store_and_fwd_flag    | Record held in vehicle memory                  |
| tolls_amount          | Tolls amount                                   |
| pickup_latitude       | Latitude where the meter was engaged           |
| pickup_longitude      | Longitude where the meter was engaged          |
| dropoff_latitude      | Longitude where the meter was timed off        |
| dropoff_longitude     | Longitude where the meter was timed off        |
| improvement_surcharge |                                                |
| congestion_surcharge  |                                                |
| total_amount          | Total amount charged (cash tips not included)


## The Problem

* There are about 65,000 vehicles affiliated with Uber in the city, which provide more than 400,000 trips per day (according to the Taxi and Limousine Commission)
* Lyft, its main rival, tallies about 112,000 trips per day
* City law caps the number of yellow taxis at about 13,500; they typically make about 300,000 trips each day
* About 44 percent of drivers made incomes between $20,000 and $39,000
* Tips are higher and much more likely for longer trips (=higher fares)

## Data Cleaning

To clean our dataset we followed [Gaurav Sharma's cleaning process](https://blog.goodaudience.com/taxi-demand-prediction-new-york-city-5e7b12305475) on the NYC taxi data. 

Our combined data file from Jan to December 2015 had 12.7 million entries.
```
tpep_pickup_datetime     12748986
tpep_dropoff_datetime    12748986
passenger_count          12748986
trip_distance            12748986
pickup_longitude         12748986
pickup_latitude          12748986
dropoff_longitude        12748986
dropoff_latitude         12748986
fare_amount              12748986
extra                    12748986
mta_tax                  12748986
tip_amount               12748986
tolls_amount             12748986
improvement_surcharge    12748983
total_amount             12748986
dtype: int64
```


1. Filtering out data points that were either zero or outside of NYC's coordinates: 
```
#filter out entries too west or too south
WESTMOST_LONG = -74.273654
SOUTHMOST_LAT = 40.480883
NORTHMOST_LAT = 40.917335
EASTMOST_LONG = -73.645863
```
2. Trip characteristics

We followed Gaurav's methods for [data cleaning](https://github.com/snowolf/Taxi-Demand-Prediction-New-York-City/blob/master/Taxi-Demand-Prediction-NYC.ipynb) to remove speed, distance and duration:

* Remove all rides with average speeds above 45.31 mph:
```
99.1 percentile value of speed is 36.31081290376664miles/hr
99.2 percentile value of speed is 36.91470054446461miles/hr
99.3 percentile value of speed is 37.588235294117645miles/hr
99.4 percentile value of speed is 38.330334294788756miles/hr
99.5 percentile value of speed is 39.17580011612381miles/hr
99.6 percentile value of speed is 40.15384615384615miles/hr
99.7 percentile value of speed is 41.338029086798095miles/hr
99.8 percentile value of speed is 42.866243893093184miles/hr
99.9 percentile value of speed is 45.310675074725154miles/hr
100.0 percentile value of speed is 192857142.85714284miles/hr
```

![](/resources/Speed.png)

```
new_frame_cleaned = new_frame_cleaned[(new_frame_cleaned.speed>0) & (new_frame_cleaned.speed<45.31)]
```


* Remove trips with a total distance of more than 23 miles:
```
99.1 percentile value of trip distance is 18.37miles
99.2 percentile value of trip distance is 18.6miles
99.3 percentile value of trip distance is 18.84miles
99.4 percentile value of trip distance is 19.14miles
99.5 percentile value of trip distance is 19.5miles
99.6 percentile value of trip distance is 19.97miles
99.7 percentile value of trip distance is 20.51miles
99.8 percentile value of trip distance is 21.23miles
99.9 percentile value of trip distance is 22.58miles
100.0 percentile value of trip distance is 258.9miles
```
![](/resources/Distance.png)

```
new_frame_cleaned = new_frame_cleaned[(new_frame_cleaned.trip_distance>0) & (new_frame_cleaned.trip_distance<23)]
```

* Remove trips with a fare amount above $86.6:
```
99.1 percentile value of trip fare is 67.55
99.2 percentile value of trip fare is 68.8
99.3 percentile value of trip fare is 69.6
99.4 percentile value of trip fare is 69.73
99.5 percentile value of trip fare is 69.73
99.6 percentile value of trip fare is 69.76
99.7 percentile value of trip fare is 72.46
99.8 percentile value of trip fare is 75.16
99.9 percentile value of trip fare is 86.6
100.0 percentile value of trip fare is 3950611.6
```

![](/resources/Fare.png)

```
new_frame_cleaned = new_frame_cleaned[(new_frame_cleaned.total_amount>0) & (new_frame_cleaned.total_amount<86.6)]
```

* Remove trips with total duration above 12hrs:
```
90 percentile value of Trip Duration is 23.45min
91 percentile value of Trip Duration is 24.35min
92 percentile value of Trip Duration is 25.383333333333333min
93 percentile value of Trip Duration is 26.55min
94 percentile value of Trip Duration is 27.933333333333334min
95 percentile value of Trip Duration is 29.583333333333332min
96 percentile value of Trip Duration is 31.68333333333333min
97 percentile value of Trip Duration is 34.46666666666667min
98 percentile value of Trip Duration is 38.71666666666667min
99 percentile value of Trip Duration is 46.75min
100 percentile value of Trip Duration is 548555.6333333333min
100 percentile value of Trip Duration is 548555.6333333333min
```
![](/resources/Trip_duration.png)

```
new_frame_cleaned = new_frame[(new_frame.trip_duration>1) & (new_frame.trip_duration<720)]
```

## Plot of the Cab Rides

![](/resources/NYC_plot.png)

## Data Preparation

We also tested location clustering using 100 clusters, but the clusters did not add value to our models below. 
```
coord = new_frame_cleaned[["pickup_latitude", "pickup_longitude"]].values
regions = MiniBatchKMeans(n_clusters = 100, batch_size = 10000).fit(coord)
new_frame_cleaned["pickup_cluster"] = regions.predict(new_frame_cleaned[["pickup_latitude", "pickup_longitude"]])
```

Here's a map of our NYC clusters:
![](/resources/clusters.png)

Time data:
We used BigML for our models. Pick-up date and time is automatically split into new columns (month, day of month, day of week, hour, minute, second).

## Models

We used BigML to create our prediction models. The picked a random 5% sample of our complete dataset (maximum file load <1GB) with 505,000 entries and split it in 80:20 training and test set.

### Linear Regression for Trip Fare and Tip Amount

We ran linear regressions with the predictors below and removed them if the p-value was >0.05.
```
tpep_pickup_datetime.day-of-month
tpep_pickup_datetime.day-of-week
tpep_pickup_datetime.hour
tpep_pickup_datetime.minute
pickup_longitude
pickup_latitude
```
Both models have little ability to predict the fare amount or the tip amount. R squared for both models are well below 0.5.

![](/resources/lin_reg_fare.png)

![](/resources/lin_reg_tip.png)

### Decision Tree for High/Low Fare

We used a Decision Tree model with the same input as in the linear regressions above. We added another field as boolean *fare split* that divided the *fare_amount* into higher or lower than median ($9.80). This field was our model target.

![](/resources/model_fare_class.png)


* Field importance:
  1. pickup_latitude: 30.55%
  2. pickup_longitude: 27.41%
  3. tpep_pickup_datetime.hour: 20.99%
  4. tpep_pickup_datetime.day-of-week: 11.94%
  5. tpep_pickup_datetime.day-of-month: 9.12%
  
The ROC AUC of 0.6212 shows the model is better than a simple coin flip, but does not serve as a great predictor:

| Evaluation | ROC Curve |
|----------------------------------------------------- |-----------------------------------------------|
| ![](/resources/evaluation_fare_class.png)            | ![](/resources/ROC_fare_class.png)            |

We ran various classification models (incl. ensemble models that BigML supported), but saw little to no improvement compared to a simple decision tree.
![](/resources/comparison_fare_class.png)

### Descision Tree for Tip/No Tip

We used a Decision Tree model with the same input as in the linear regressions above. We added another field as boolean *tip exists* that divided the *tip_amount* into $0 or >$0. This field was our model target.

![](/resources/model_tip_class.png)


* Field importance:
  1. pickup_longitude: 32.44%
  2. pickup_latitude: 25.63%
  3. tpep_pickup_datetime.hour: 21.12%
  4. tpep_pickup_datetime.day-of-month: 12.99%
  5. tpep_pickup_datetime.day-of-week: 7.82%

  
The ROC AUC of 0.5940 shows the model is better than a simple coin flip, but even worse than the fare prediction and does not serve as a great predictor:

| Evaluation | ROC Curve |
|----------------------------------------------------- |-----------------------------------------------|
| ![](/resources/evaluation_fare_class.png)            | ![](/resources/ROC_fare_class.png)            |

We ran various classification models (incl. ensemble models that BigML supported), but saw little to no improvement compared to a simple decision tree.
![](/resources/comparison_fare_class.png)



## Key Learnings


* Predicting fares and tips amount simply based on location and time is difficult
* K-Means model did not give much valuable insights in our effort to improve actionability
* Models had higher success rate than random choice (50:50), but **ROC AUC** did not indicate good models
* Even **ensemble ML models** (decision forest, boosted trees) could not really improve the model performance
* Our model predicting the range of increase/decrease of both fare and tips show low R-squared, so the current input variables in the dataset are **not good enough predictors** to explain response variable


