from database_layer.database import Database
from utils.logger import Logger


class Gateway:
    log = Logger()
    db = Database()

    def __call__(self):
        pass
