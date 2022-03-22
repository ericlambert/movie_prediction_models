# Dataset Description

Data as of: January 10th 2022
Link: ([Kaggle](https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies))
Record Count: 918
Variable Count: 10

## Variable descriptions

Id : Unique numeric id per row, rank by Domestic Sales (in $)
Title : The title of the movie concatenated with its release year
Movie Info : a brief text description of the movie
Distributor : The organization that released the movie
Release Date : The release date for the movie. **Contains NAs.**
Domestic Sales (in $) : Box office sales within the United States in USD
International Sales (in $) : Box office sales outside the United States in USD
World Sales (in $) : Total Box office sales in USD
Genre : a text array of genre classifications that apply to each movie (e.g. ['Action', 'Adventure', 'Sci-Fi']).
Movie Runtime : the length of the movie in hours and minutes
License : The film rating for the movie. **Contains NAs.**

## Processing to be done

- imput missing data for Release Dates
- imput missing data for License
- add imdb film id so we can dynamically link to each film's Imdb page
- Parse and split Genre into individual dummy features