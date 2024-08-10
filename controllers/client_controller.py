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
        for client in self.clients:
            if str(client.get('client_id')) == str(client_id):
                return client
        return None

    def update_client(self, client_id, name=None, email=None, phone=None):
        client = self.get_client_by_id(client_id)
        if client:
            if name:
                client['name'] = name
            if email:
                client['email'] = email
            if phone:
                client['phone'] = phone
            self.data_manager.save_data(self.clients)
            print(f"Client ID {client_id} updated successfully.")
        else:
            print(f"Client ID {client_id} not found.")

    def delete_client(self, client_id):
        client = self.get_client_by_id(client_id)
        if client:
            self.clients.remove(client)
            self.data_manager.save_data(self.clients)
            print(f"Client ID {client_id} deleted successfully.")
        else:
            print(f"Client ID {client_id} not found.")
