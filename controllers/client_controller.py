from dal.data_manager import DataManager
from models.client import Client

class ClientController:
    def __init__(self):
        self.data_manager = DataManager('clients.json')
        self.clients = self.data_manager.load_data()

    def add_client(self, name, email, phone):
        client_id = len(self.clients) + 1
        client = Client(name, email, phone, client_id)
        self.clients.append(client.__dict__)
        self.data_manager.save_data(self.clients)

    def list_clients(self):
        return self.clients

    def get_client_by_id(self, client_id):
        # Garantir que a comparação seja feita com tipos de dados consistentes
        for client in self.clients:
            if str(client.get('client_id')) == str(client_id):
                return client
        return None
