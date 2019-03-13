Queries
=========

Implement and *test* the following python functions:

## Filter
Write a function that takes one positional argument that is the name of a file. Use can use this example data set.
Implement your function in such a way that it accepts as many keyword arguments as the user wants. Every keyword argument must be a valid name of a column in the CSV file:
```
   full_name, favourite_color, company_name, email, phone_number, salary
```
Your function should filter the data set and return an array of arrays for every raw that matches the query.

Support the following behavior:

### Filter by one argument

```
    filter('example_data.csv', full_name="Diana Harris")
```
That should return all of the records named "Diana Harris"

### Filter by more then one arguments
```
    filter('example_data.csv', full_name="Diana Harris", favourite_color="lime")
```
That should filter using **AND** statement. This is going to return all of the records named "Diana Harris" that have lime as a favorite color.

### __startswith
```
    filter('example_data.csv', full_name__starswith="Diana")
```
That should filter all records have name starting with "Diana"

### __contains
```
    filter('example_data.csv', email__contains="@gmail")
```
That should return all records that are using gmail.

### __gt and __lt
```
    filter('example_data.csv', salary__gt=1000, salary__lt=3000)
```
This is short for 'grater than' and 'less than'. This query should return all of the records that are heaving more salary in the interval (1000, 3000).

### order_by
```
    filter('example_data.csv', salary__gt=1000, salary__lt=3000, order_by='salary')
```
If you have the ``order_by`` argument that means that you have to order your results by this field starting withe lowest value.

## count
Write another function that behaves the exact same way as filter but it returns only the count of the results.

## first
Write another function that behaves the exact same way as filter but it returns only the first result.

## last
Write another function that behaves the exact same way as filter but it returns only the last result.
