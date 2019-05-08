import sqlite3

class Column:
    def __init__(
        self,
        column_name,
        column_type,
        unique=False,
    ):
        self.column_name = column_name
        self.column_type = column_type
        self.unique = unique

    @property
    def unique_str(self):
        if self.unique:
            return 'UNIQUE'
        return ''

    def as_sql(self):
        return f"{self.column_name} {self.column_type} {self.unique_str}"


class Table:
    def __init__(self, table_name, columns):
        self.table_name = table_name
        self.columns = columns

    def column_str(self):
        return ', '.join([column.as_sql() for column in self.columns])

    def create(self, cursor):
        column_str = self.column_str()
        create_table = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name}
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {column_str}
                );
        """
        cursor.execute(create_table)

    def column_names(self):
        return [column.column_name for column in self.columns]

    def column_names_str(self):
        return ', '.join(self.column_names())

    def fetch_all(self, cursor):
        column_names_str = self.column_names_str()
        query = f"""
        SELECT {column_names_str} FROM {self.table_name}
        """
        cursor.execute(query)
        return cursor.fetchall()


class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_table(self, table):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        table.create(cursor)

        connection.commit()
        connection.close()

    def fetch_all_from_table(self, table):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        result = table.fetch_all(cursor)

        connection.commit()
        connection.close()

        return result



database = Database('newdb.db')
table = Table(
    'User',
    [
        Column('name', 'text', unique=True),
        Column('age', 'integer'),
    ]
)

database.create_table(table)
print(database.fetch_all_from_table(table))

