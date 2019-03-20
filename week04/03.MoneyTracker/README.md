# Money Tracker

Remember the Money Tracker application that you created two weeks ago?
Now it is time to use your OO knowledge and implement it again.

You have to create the following structure:

* in `category.py` you have to implement three classes.
  - parent class Category
  - two child classes - Income and Expense

* in `parse_money_tracker_data.py` you have to parse the data coming from `money_tracker.txt` and return list of the rows
* in `aggregated_money_tracker.py` you need to process the list of rows and create an aggregated object
* `money_tracker_menu.py` is responsible to call the MoneyTracker methods based on the option provided from the user
* the `money_tracker.py` module should process the user data, This class takes just one attribute - AggregatedMoneyTracker object.
* and the `main.py` is the starting point of the application.

**Do not forget to implement**
- at least these dunders `__str__`, `__repr__`, `__eq__`
- tests for your implementation
