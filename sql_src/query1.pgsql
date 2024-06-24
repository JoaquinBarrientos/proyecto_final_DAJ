select vendorid, 
date_trunc('hour', tpep_pickup_datetime) AS pickup_hour,
avg(passenger_count) as avg_passenger_count,
sum(passenger_count) as total_passenger_count,
avg(trip_distance) as avg_trip_distance,
sum(trip_distance) as total_trip_distance,
avg (fare_amount) as avg_fare_amount,
sum (fare_amount) as total_fare_amount,
count (*) as total_trips
from yellow.yellow_taxi_trips
where tpep_pickup_date >='2023-01-01'
group by vendorid, pickup_hour