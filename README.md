# Find distance between countries

This problem is from [RKCR software's career page](https://rckr.com/careers).

Find latitude and longitude of utmost 20 countries, ordered by population, with a population greater or equal to the population limit given below and have atleast one currency exclusively for themselves. (countries like Madagascar, Sri Lanka but not India, USA). Use the country details from [this dataset](data.json).

Your task is to find the sum of the length of all lines (in kms) that can be drawn between co-ordinates of these countries.
- Assume radius of earth: 6371 km
- Round length of each line and final result to 2 decimal points
- If co-ordinates are missing for any country use 0.000 N 0.000 E

## How to use
1. clone the repository 
```
$ git clone https://github.com/Maryll-castelino/find-distance-between-countries.git
```
2. change directories
```
$ cd find-distance-between-countries
```
3. execute the file with the population limit as an argument
```
$ python main.py <your limit here>
```

example:
```
$ python main.py 73628384
704896.45
```