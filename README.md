# Taxi Fares in NYC

## Objective

What can we predict about a cab fare simply based on the pick-up location?
We tested:
* fare prediction
* tip amount
* higher or lower fare (compared to median of $9.80)
* tip or no top for next ride 

## The Data

We used NYC's public TLC data that can be downloaded on the NYC.gov[https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page] website. We used 2015 data as this was the last year in which the TLC provided lat and long coordinates. Each monthly dataset contains about 2GB of data.

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

To clean our dataset we followed Gaurav Sharma's cleaning guide on the NYC taxi data: Link[https://blog.goodaudience.com/taxi-demand-prediction-new-york-city-5e7b12305475]

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


1. Filtering out data points that were eithe zero or outside of NYC's coordinates: 
```
#filter out entries too west or too south
WESTMOST_LONG = -74.273654
SOUTHMOST_LAT = 40.480883
NORTHMOST_LAT = 40.917335
EASTMOST_LONG = -73.645863

concat = concat[concat['pickup_longitude'] >= WESTMOST_LONG]
concat = concat[concat['pickup_latitude'] >= SOUTHMOST_LAT]
concat = concat[concat['pickup_longitude'] <= EASTMOST_LONG]
concat = concat[concat['pickup_latitude'] <= NORTHMOST_LAT]
```
2. Trip characteristics

We used Gaurav's summary statistics[https://github.com/snowolf/Taxi-Demand-Prediction-New-York-City/blob/master/Taxi-Demand-Prediction-NYC.ipynb] of the Jan 2015 file to remove speed, distance and duration:

* Remove all rides with average speeds above 45.31 mph:
```
99 percentile value of speed is 35.75135055113604miles/hr
100 percentile value of speed is 192857142.85714284miles/hr
```
* Remove trips with a total distance of more than 23 miles:
```
99.9 percentile value of trip distance is 22.58miles
100.0 percentile value of trip distance is 258.9miles
```
* Remove trips with a fare amount above $86.6:
```
99.9 percentile value of trip fare is 86.6
100.0 percentile value of trip fare is 3950611.6
```
* Remove trips with total duration above 12hrs:
Remaining data points where the recording must be incorrect as we already removed extremelz high fares.
```
100 percentile value of Trip Duration is 548555.6333333333min
```

3. Keep only non-negatiev values

The resulting data set left us with a little more than 12 million data entries.

## Plot of the Cab Rides

![/resources/NYC_plot.png]

## Models

We used BigML to create our prediction models. The picked a random 5% sample of our complete dataset (maximum file load <1GB) with 505,000 entries and split it in 80:20 training and test set.

### Lienar Regression for Trip Fare

### Linear Fare for Trip Amount

### Decision Tree for High/Low Fare

### Descision Tree for Tip/No Tip



