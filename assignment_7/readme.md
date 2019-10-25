# Assignment 7 - BI
We chose to use the Jupyter Notebook for this assignment along with sklearn.
We removed the indexes from our dataframe as we didn't need those.

## Assignment details
In this assignment, we'll predict whether the price is too high or too low.
In order for us to do that, we need some data to help us figure out the right price.

## Categories
Based on analysing the data we found that the best way to show the data would be to split it up in 5 categories.

1. Below -60 %. Either wrong data or a very unlucky time to sell.
2. Below 0 %. Sold below market value.
3. Sold just at market value.
4. Sold above market value.
5. Above 100 %. Either wrong data or a very lucky time to sell.

We'll make a new dataframe containing the data split up into the categories defined above.

We'll include the following columns in the dataframe
* Zipcode
* Square meters
* Number of rooms
* Price
* Latitude
* Longitude
* Address
* Housing type
* Construction year
* Price change in pct.
* Sell year

## Columns we need for machine learning
In this part of the exercise, we pick out the columns we think will be helpful
to predict the price.

* Zipcode
* Price
* Square meters
* Number of rooms
* Sell year
* Construction year

## Pick out rows for validation
We take out 50 random rows from each of the 5 classes for validation.

## ML models
We'll be using the following machine learning models to try to get the best results.

* Decision Tree
* Logistic Regression
* KNN
