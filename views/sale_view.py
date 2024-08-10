from collections import Counter
from controllers.sale_controller import SaleController
from controllers.product_controller import ProductController
from controllers.client_controller import ClientController

class SaleView:
    def __init__(self):
        self.sale_controller = SaleController()
        self.product_controller = ProductController()
        self.client_controller = ClientController()

    def sales_report(self):
        sales = self.sale_controller.sales_report()
        if not sales:
            print("No sales available.")
            return
        
        print("\nSales Report")
        print("----------------------------------------------------------------------------------------------------")
        print(f"{'Client':<20} {'Product':<20} {'Quantity':<10} {'Total Price':<15} {'Date':<15}")
        print("----------------------------------------------------------------------------------------------------")
        for sale in sales:
            client = sale.get('client', {}).get('name', 'N/A')
            products = sale.get('products', [])
            date = sale.get('date', 'N/A')
            for item in products:
                product_name = item.get('name', 'N/A')
                quantity = item.get('quantity', 0)
                total_price = item.get('price', 0.0) * quantity
                print(f"{client:<20} {product_name:<20} {quantity:<10} {total_price:<15} {date:<15}")
            print("----------------------------------------------------------------------------------------------------")

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

        products = []
        while True:
            print("Available products:")
            available_products = self.product_controller.list_products()
            for product in available_products:
                print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity in Stock: {product['quantity']}")

            product_id_input = input("Enter product ID to add to the sale (or 'done' to finish): ")
            if product_id_input.lower() == 'done':
                break

            try:
                product_id = int(product_id_input)
            except ValueError:
                print("Invalid product ID. Please enter a numeric value.")
                continue

            product = self.product_controller.get_product_by_id(product_id)
            if not product:
                print("Product not found.")
                continue

            quantity = int(input(f"Enter quantity for {product['name']} (Available: {product['quantity']}): "))
            if quantity > product['quantity']:
                print(f"Not enough stock for {product['name']}.")
                continue

            # Reduz a quantidade no estoque e atualiza o banco de dados
            product['quantity'] -= quantity
            self.product_controller.update_product(product)

            # Adiciona apenas a quantidade informada ao relatório de vendas
            products.append({
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity
            })

        if not products:
            print("No products selected. Sale aborted.")
            return

        date = input("Enter sale date (YYYY-MM-DD): ")
        self.sale_controller.add_sale(client, products, date)
        print("Sale added successfully.")

    def top_selling_products(self):
        sales = self.sale_controller.sales_report()
        if not sales:
            print("No sales available.")
            return

        product_counter = Counter()
        for sale in sales:
            for item in sale.get('products', []):
                product_name = item.get('name')
                quantity = item.get('quantity', 0)
                product_counter[product_name] += quantity

        if not product_counter:
            print("No products sold yet.")
            return

        print("\nTop Selling Products")
        print("----------------------------------------------------------------------------------------------------")
        print(f"{'Product':<20} {'Quantity Sold':<15}")
        print("----------------------------------------------------------------------------------------------------")
        for product, quantity in product_counter.most_common():
            print(f"{product:<20} {quantity:<15}")
        print("----------------------------------------------------------------------------------------------------")

    def sales_by_date(self):
        date = input("Enter the date to filter sales (YYYY-MM-DD): ")
        sales = self.sale_controller.sales_report()
        filtered_sales = [sale for sale in sales if sale.get('date') == date]

        if not filtered_sales:
            print(f"No sales found for the date {date}.")
            return
        
        print(f"\nSales Report for {date}")
        print("----------------------------------------------------------------------------------------------------")
        print(f"{'Client':<20} {'Product':<20} {'Quantity':<10} {'Total Price':<15}")
        print("----------------------------------------------------------------------------------------------------")
        for sale in filtered_sales:
            client = sale.get('client', {}).get('name', 'N/A')
            products = sale.get('products', [])
            for item in products:
                product_name = item.get('name', 'N/A')
                quantity = item.get('quantity', 0)
                total_price = item.get('price', 0.0) * quantity
                print(f"{client:<20} {product_name:<20} {quantity:<10} {total_price:<15}")
            print("----------------------------------------------------------------------------------------------------")

    def top_clients(self):
        sales = self.sale_controller.sales_report()
        if not sales:
            print("No sales available.")
            return

        client_counter = Counter()
        for sale in sales:
            client = sale.get('client', {}).get('name', 'N/A')
            total_sale = sum(item.get('price', 0.0) * item.get('quantity', 0) for item in sale.get('products', []))
            client_counter[client] += total_sale

        if not client_counter:
            print("No clients found.")
            return

        print("\nTop Clients")
        print("----------------------------------------------------------------------------------------------------")
        print(f"{'Client':<20} {'Total Spent':<15}")
        print("----------------------------------------------------------------------------------------------------")
        for client, total_spent in client_counter.most_common():
            print(f"{client:<20} {total_spent:<15.2f}")
        print("----------------------------------------------------------------------------------------------------")

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
                self.sales_by_date()
            elif choice == '4':
                self.top_selling_products()
            elif choice == '5':
                self.top_clients()
            elif choice == '6':
                break
            else:
                print("Invalid option.")
