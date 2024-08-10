from controllers.client_controller import ClientController

class ClientView:
    def __init__(self):
        self.client_controller = ClientController()

    def add_client(self):
        name = input("Enter client name: ")
        email = input("Enter client email: ")
        phone = input("Enter client phone: ")
        self.client_controller.add_client(name, email, phone)
        print("Client added successfully.")

    def list_clients(self):
        clients = self.client_controller.list_clients()
        if not clients:
            print("No clients available.")
            return
        
        print("\nList of Clients")
        print("----------------------------------------------------------------------------------------------------")
        print(f"{'ID':<10} {'Name':<20} {'Email':<30} {'Phone':<15}")
        print("----------------------------------------------------------------------------------------------------")
        for client in clients:
            print(f"{client['client_id']:<10} {client['name']:<20} {client['email']:<30} {client['phone']:<15}")
        print("----------------------------------------------------------------------------------------------------")

    def menu(self):
        while True:
            print("\nClient Management")
            print("1. Add Client")
            print("2. List Clients")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_client()
            elif choice == '2':
                self.list_clients()
            elif choice == '3':
                break
            else:
                print("Invalid option.")
