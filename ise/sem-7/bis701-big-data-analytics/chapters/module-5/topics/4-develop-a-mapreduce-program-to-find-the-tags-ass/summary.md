# **Revision Notes: MapReduce Program for Movie Lens Data**

## **Introduction**

- MapReduce is a programming model for processing large data sets in parallel across a cluster of nodes.
- Movie Lens data: a dataset containing information about movie ratings from users.

## **Key Concepts**

- **Map Phase**:
  - Maps each movie rating to a key-value pair: (movie ID, user ID)
  - Uses `map()` function to generate output
- **Reduce Phase**:
  - Reduces output from map phase by movie ID
  - Uses `reduceByKey()` function to aggregate ratings for each movie
- **Mapper and Reducer Functions**:
  - Mapper function: takes a tuple (movie ID, user ID) and returns a key-value pair (movie ID, rating)
  - Reducer function: takes a list of ratings and returns a single rating

## **MapReduce Program**

- Load Movie Lens data into Spark
- Map each rating to a key-value pair: (movie ID, user ID)
- Reduce output by movie ID
- Print movie ID and average rating

## **Important Formulas and Definitions**

- **Average Rating**: (sum of ratings) / (number of ratings)
- **Movie Rating**: a numerical value representing a user's rating of a movie (e.g., 1-5)

## **Theorems**

- **Data Parallelism**: MapReduce can process large data sets in parallel across a cluster of nodes.
- **Data Locality**: MapReduce can reduce communication overhead by processing data in local memory.

## **Revision Tips**

- Understand MapReduce programming model and its application in data processing.
- Familiarize yourself with Spark and its data analysis APIs.
- Practice mapping, reducing, and aggregating data using Spark.
