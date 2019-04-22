# First steps in Databases and SQL

Presentation: http://slides.com/hackbulgaria/deck-78-114

## Tables, tables everywhere! SELECT, UPDATE, INSERT, DELETE

Now, we know that our languages table looks like this:

| id      | language  | answer  | answered | guide |
| ------------- |:-------------:| --- | --- |-----:|
1|Python|google|0|A folder named Python was created. Go there and fight with program.py!
2|Go|200 OK|0|A folder named Go was created. Go there and try to make Google Go run.
3|Java|object oriented programming|0|A folder named Java was created. Can you handle the class?
4|Haskell|Lambda|0|Something pure has landed. Go to Haskell folder and see it!
5|C#|NDI=|0|Do you see sharp? Go to the C# folder and check out.
6|Ruby|https://www.ruby-lang.org/bg/|0|Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!
7|C++|header files|0|Here be dragons! It's C++ time. Go to the C++ folder.
8|JavaScript|Douglas Crockford|0|NodeJS time. Go to JavaScript folder and Node your way!

Your task is to write queries for:

* Create database
* Create table `Languages` with columns and attributes with the correct types
* Insert data
* Add new column `rating` which is number from 1 to 9. Insert values for every language.
* For few languages (`Python` and `Go`) update answered value from 0 to 1
* Select languages which answer is `200 OK` or `Lambda`.


## Foreign Keys

We have two type of keys - Primary (PK) and Foreign (FK).

If a column is a PK for the table, it can hold only unique values. And one value from that column should be able to "identify" the entire row. If we search in the `WHERE` clause with a PK, we should always get 1 value.

FK are different. They are used to express relations between two tables.

In the previous examples, the `author` column was a FK column. `student_id` and `course_id` in the junction table are FKs too.

Here is the deal with the FK:

* This is a **constraint** over what values can be inserted in the column, defined as a foreign key.
* Usually, when you define your table, you say that a given column is going to be a FK to another table's PK column.

Lets see the SQL for that:

Now, when you have the general idea, you can read more about FK's here - https://www.sqlite.org/foreignkeys.html



Lets see the SQL for that:


```sql
CREATE TABLE Users(
  user_id INTEGER PRIMARY KEY,
  user_name TEXT,
  user_email TEXT
)

CREATE TABLE Posts(
  post_id INTEGER PRIMARY KEY,
  post_title TEXT,
  post_content TEXT,
  author INTEGER,
  FOREIGN KEY(author) REFERENCES Users(user_id)
)
```

There is an additional `FOREIGN KEY` statement. This is the required thing.

**Here is the SQL for the Student-Courses tables:**

```sql
CREATE TABLE Students(
  student_id INTEGER PRIMARY KEY,
  student_name TEXT
)

CREATE TABLE Courses(
  course_id INTEGER PRIMARY KEY,
  course_name TEXT
)

CREATE TABLE Student_To_Course(
  student_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY(student_id) REFERENCES Students(student_id),
  FOREIGN KEY(course_id) REFERENCES Courses(course_id)
)
```

Now, when you have the general idea, you can read more about FK's here - https://www.sqlite.org/foreignkeys.html
