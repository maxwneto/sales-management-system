from .person import Person

class Client(Person):
    def __init__(self, name, email, phone, client_id=None):
        super().__init__(name, email, phone)
        self.client_id = client_id
