from utils.constants import DataBaseConstants


DATABASE_EXGINE = DataBaseConstants.ENGINE
DATABASE_NAME = DataBaseConstants.NAME

@atomic_transaction
class Database:
    def __init__(self):
        self.connection = DATABASE_EXGINE.connect(DATABASE_NAME)
        self.cursor = self.connection.cursor
        self.cursor.row_factory = DATABASE_EXGINE.Row

    def create(self, model_name, **kwargs):
        # does model_name exist?
        # are kwargs valid columns
        #  are kwargs values valid?

    def find
