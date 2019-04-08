# with performance(file_name):
Make a context manager ``performance`` that takes ``file_name`` and writes in it the date & time needed for executing a function that tends to be slow (keep every log on a new line)

## Example

```python
with performance('log_file.txt'):
    ...
    # sleep(1)
    ...
```

Log file should look like this:

```
Date 2018-04-20 15:10:42.410397. Execution time: 1.0014269351959229
Date 2018-04-20 15:10:46.886415. Execution time: 1.0006434917449951
```

# with assertRaises(exception, msg=None)
Make a context manager ``assertRaises`` that:

  * passes if exception is raised
  * is an error if another exception is raised
  * or fails if no exception is raised

To catch any of a group of exceptions, a tuple containing the exception classes may be passed as exception.

## Example

```python
with assertRaises(SomeException):  # asserts SomeException is raised
    do_something()
    
with assertRaises(SomeException, some_message):  # asserts SomeException is raised and contains some_message
    do_something()
```
