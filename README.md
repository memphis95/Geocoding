# Comparision of Open Source Geocoding APIs

Geocoding is the process of transforming a description of a location—such as an address, or a name of a place—to a location on the earth's surface i.e. a (latitude, longitude) coordinate. It is used extensively in GIS, geotagging media, cartography, customer data management etc.

Geocoding is highly prone to error for various reasons, including lack of coverage (local vs. global); lack of complete, correct, consistent, and updated reference databases; and the making of inappropriate assumptions. All these may affect match rate and positional accuracy. Additionally, incorrect geocoding may bias the results of spatial analysis, resulting in misclassification of actual physical locations that may adversely affect research outcomes or location-based business decisions. Accordingly, understanding and addressing these geocoding challenges is vital.

The dataset used for geocoding was extracted from the list of restaurants/markets that received the 2018 Award of Excellence in Orange Country, California, United States which was provided on the Orange Country Government Healthcare Agency website. The dataset was truncated to the first 1000 records due to the daily free limit of selected geocoders. 

Six different geocoders are chosen for this purpose - Google Maps, HERE, Texas A&M Geoservices, MapLarge, United States Census Bureau and GeoNames - that are free and appear to do their own geocoding using reference databases. These geocoders are tested on a dataset and the results are visualized using Google Maps.

For comparing geocoders, the resulting (latitude, longitude) pair from Google Maps Geocoding API is used as a benchmark. All other geocoders are compared on the basis of difference in distance in meters using the Haversine formula. Other comparative measures like match percentage, standard deviation etc can be computed using simple python scripts or MS Excel functions.

## Getting Started

Python scripts for sending multiple geocoding API requests and storing the results are available for Google Maps, HERE and Geonames. API key and other details for these geocoders would be required to run the scripts.

Other APIs provide batch geocoding services.

## Deployment

A python IDE like Spyder is suitable to run the scripts as libraries are pre-installed.

## Authors

* **Ankit Goel** - [USERNAME](PROFILE LINK)
* **Shruti Sahu** - [USERNAME](PROFILE LINK)

## Reference

* https://gist.github.com/shanealynn/033c8a3cacdba8ce03cbe116225ced31
* https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points/4913653#4913653
* https://opengeospatialdata.springeropen.com/articles/10.1186/s40965-017-0026-3
