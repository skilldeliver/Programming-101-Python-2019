from hospital.user import User
from gateway_proxy.gateway import Gateway


class UserGateway(Gateway):
    def create_new_user(self, username, password, **kwargs):
        try:
            if not self.find(username1):
                kwargs.update({'username': username1, 'password': password})
                self.db.create(User, username1, password, **kwargs)
                self.log.info(f'New user was created - {username1}')
            else:
                raise UserAlreadyExistsError(username)
        except DatabaseConnectionError:
            sys.exit(1)

    def find(self, username):
        return self.db.find(User, username)

    def find_all(self):
        return self.db.find_all(User)

    def delete(self, username):
        try:
            if self.find_existing_user(username):
                self.db.delete(User, username)
            else:
                raise UserDoesNotExistError(username)
        except DatabaseConnectionError as exp:
            sys.exit(1)

    def update(self, username, **params):
        try:
            if self.find_existing_user(username):
                self.db.update(User, (params.keys()), (params.values()))
            else:
                raise UserDoesNotExistError(username)
        except DataIntegrityError as exp:
            self.log.exception(exp)
