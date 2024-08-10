from controllers.sale_controller import SaleController
from controllers.client_controller import ClientController
from controllers.product_controller import ProductController

class SaleView:
    def __init__(self):
        self.sale_controller = SaleController()
        self.client_controller = ClientController()
        self.product_controller = ProductController()

    def add_sale(self):
        client_id_input = input("Enter client ID: ")
        try:
            client_id = int(client_id_input)
        except ValueError:
            print("Invalid client ID. Please enter a numeric value.")
            return

        client = self.client_controller.get_client_by_id(client_id)
        if not client:
            print("Client not found.")
            return

        print("Available products:")
        products = self.product_controller.list_products()
        product_ids = [str(product['id']) for product in products]
        for product in products:
            print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")

        product_ids_input = input("Enter product IDs (comma separated): ")
        selected_products = []
        for pid in product_ids_input.split(','):
            pid = pid.strip()
            if pid not in product_ids:
                print(f"Invalid product ID: {pid}. Please select a valid product.")
                return
            product = self.product_controller.get_product_by_id(int(pid))
            selected_products.append(product)

        if not selected_products:
            print("No valid products selected. Sale aborted.")
            return

        date = input("Enter sale date (YYYY-MM-DD): ")
        self.sale_controller.add_sale(client, selected_products, date)
        print("Sale added successfully.")

    def sales_report(self):
        sales = self.sale_controller.sales_report()
        for sale in sales:
            print(sale)

    def sales_by_date(self):
        date = input("Enter the date (YYYY-MM-DD) for the sales report: ")
        sales = self.sale_controller.sales_by_date(date)
        if not sales:
            print(f"No sales found for the date: {date}")
        else:
            for sale in sales:
                print(sale)

    def top_selling_products(self):
        top_products = self.sale_controller.top_selling_products()
        for product, count in top_products:
            print(f"Product: {product}, Sales: {count}")

    def top_clients(self):
        top_clients = self.sale_controller.top_clients()
        for client, count in top_clients:
            print(f"Client: {client}, Purchases: {count}")

    def menu(self):
        while True:
            print("\nSales Management")
            print("1. Add Sale")
            print("2. Sales Report")
            print("3. Sales by Date")
            print("4. Top Selling Products")
            print("5. Top Clients")
            print("6. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_sale()
            elif choice == '2':
                self.sales_report()
            elif choice == '3':
                self.sales_by_date()  # Certifique-se de que este método está agora implementado
            elif choice == '4':
                self.top_selling_products()
            elif choice == '5':
                self.top_clients()
            elif choice == '6':
                break
            else:
                print("Invalid option.")
