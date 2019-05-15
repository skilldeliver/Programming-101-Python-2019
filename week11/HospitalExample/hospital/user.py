class User:
    db = Database()

    def __init__(self, username, password, status=None):
        self.username = username
        self.password = password
        self._status = status

    @classmethod
    def find(cls, username, password):
        result = cls.db.find_user(username, password)
        if result:
            return cls(username, password, result['status'])

    @classmethod
    def create_new_user(cls, username, hashed_pass, **kwargs):
        try:
            # TODO check kwargs
            cls.db.create_user(username, password, **kwargs)
        except DatabaseConnectionError:
            sys.exit(1)
        return cls(username, password, **kwargs)

    @property
    def status:
        return self._status
