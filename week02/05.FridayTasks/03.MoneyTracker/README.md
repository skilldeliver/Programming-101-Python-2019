# Money Tracker

In a file called `money_tracker.py` implement a program that tracks user incomes and expenses.
We are going to use the TDD approach to create our small application. Write your tests in `test_money_tracker.py`.

Your application must have the following functionalities:
- Show all user data(incomes and expenses).
- Show user data for specific date.
- Lists all expense categories.
- Lists all income categories.
- The user can add new income or expense for specific date and category.
- The user must be able to create new categories.

In the `money_tracker.py` module you must have these methods:

```python
def list_user_data(all_user_data):
    pass


def show_user_incomes(all_user_data):
    pass


def show_user_savings(all_user_data):
    pass


def show_user_deposits(all_user_data):
    pass


def show_user_expenses(all_user_data):
    pass


def list_user_expenses_ordered_by_categories(all_user_data):
    pass


def show_user_data_per_date(date, all_user_data):
    pass


def list_income_categories(all_user_data):
    pass


def list_expense_categories(all_user_data):
    pass


def add_income(income_category, money, date, all_user_data):
    pass


def add_expense(expense_category, money, date, all_user_data):
    pass
```

The user data is going to be saved in a file called `money_tracker.txt`. In order to have a working program, you should parse the information saved in the file. The `modey_tracker.txt` has a specific format:
```txt
=== 22-03-2019 ===
760, Salary, New Income
5.5, Eating Out, New Expense
34, Clothes, New Expense
41.79, Food, New Expense
12, Eating Out, New Expense
7, House, New Expense
14, Pets, New Expense
112.40, Bills, New Expense
21.5, Transport, New Expense
=== 23-03-2019 ===
50, Savings, New Income
15, Food, New Expense
200, Deposit, New Income
5, Sports, New Expense
```

The following test example is based on the data in the `money_tracker.txt`
## Examples:
```python
Hello, Peter!
Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
>>> 1
=== 22-03-2019 ===
760, Salary, New Income
5.5, Eating Out, New Expense
34, Clothes, New Expense
41.79, Food, New Expense
12, Eating Out, New Expense
7, House, New Expense
14, Pets, New Expense
112.40, Bills, New Expense
21.5, Transport, New Expense
=== 23-03-2019 ===
50, Savings, New Income
15, Food, New Expense
200, Deposit, New Income
5, Sports, New Expense


Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
>>> 4
New income amount:
>>> 10
New income type:
>>> Deposit
New income date:
23-03-2019


Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
>>> 1
=== 22-03-2019 ===
760, Salary, New Income
5.5, Eating Out, New Expense
34, Clothes, New Expense
41.79, Food, New Expense
12, Eating Out, New Expense
7, House, New Expense
14, Pets, New Expense
112.40, Bills, New Expense
21.5, Transport, New Expense
=== 23-03-2019 ===
50, Savings, New Income
15, Food, New Expense
200, Deposit, New Income
5, Sports, New Expense
10, Deposit, New income


Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
```


** To be able to test your methods, you have to pass parameters that are not going to change with time.

## Example
```python
>>> all_user_data = {'22-03-2019': {'income': [(10, 'Deposit')], 'expense': [(27.7, 'Food')]}, '23-03-2019': {'income': [(700, 'Salary'), (50, 'Savings')], 'expense': [(4, 'Eating Out')]}}
>>> show_user_incomes(all_user_data)
[(10, 'Deposit'), (50, 'Savings'), (700, 'Salary')]
```

For the `all_user_data` parameter use the `dict` data structure.

** Do not forget to catch the exceptions:**
- when a user passes an invalid option(number out of the range (1, 6))
- when the file with the user data does not exist
- when a user tries to add an income/expense with a negative amount of money. For this example, you have to create your custom exception.


## Test Examples:
```python
>>> list_user_expenses_ordered_by_categories({'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})
[(112.40, 'Bills'), (34, 'Clothes'), (5.5, 'Eating Out'), (12, 'Eating Out'), (15, 'Food'), (41.79, 'Food'), (7, 'House'), (14, 'Pets'), (5, 'Sports'), (21.5, 'Transport')]
>>> show_user_data_per_date('23-03-2019', {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})
[(50, 'Savings', 'New Income'), (15, 'Food', 'New Expense'), (200, 'Deposit', 'New Income'), (5, 'Sports', 'New Expense'), (10, 'Deposit', 'New income')]  
>>> list_income_categories({'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})
['Deposit', 'Salary', 'Savings']   
>>> add_income('Salary', 600, '25-03-2019', {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})
>>> add_expense('Health', 2.5, '25-03-2019', {'22-03-2019': {'expense': [(5.5, ' Eating Out'), (34.0, ' Clothes'), (41.79, ' Food'), (12.0, ' Eating Out'), (7.0, ' House'), (14.0, ' Pets'), (112.4, ' Bills'), (21.5, ' Transport')], 'income': [(760.0, ' Salary')]}, '23-03-2019': {'expense': [(15.0, ' Food'), (5.0, ' Sports')], 'income': [(50.0, ' Savings'), (200.0, ' Deposit'), (10.0, ' Deposit')]}})

```
