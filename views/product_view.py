from controllers.product_controller import ProductController
from controllers.category_controller import CategoryController

class ProductView:
    def __init__(self):
        self.product_controller = ProductController()
        self.category_controller = CategoryController()

    def list_products(self):
        products = self.product_controller.list_products()
        if not products:
            print("No products available.")
        else:
            print("\nProduct List")
            print("----------------------------------------------------------------------------------------------------")
            print(f"{'Product ID':<15} {'Name':<20} {'Category':<20} {'Quantity':<15} {'Price':<10}")
            print("----------------------------------------------------------------------------------------------------")
            for product in products:
                print(f"{product['id']:<15} {product['name']:<20} {product['category']['name']:<20} "
                      f"{product['quantity']:<15} {product['price']:<10}")
            print("----------------------------------------------------------------------------------------------------")

    def add_product(self):
        print("Available categories:")
        categories = self.category_controller.list_categories()
        if not categories:
            print("No categories available. Please add categories first.")
            return
        
        for category in categories:
            print(f"Name: {category['name']}")

        category_name = input("Enter category name: ").strip()
        category = None
        for cat in categories:
            if cat['name'].lower() == category_name.lower():
                category = cat
                break

        if not category:
            print("Invalid category. Please choose an existing category.")
            return

        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))  # Quantidade de produtos

        self.product_controller.add_product(name, price, category, quantity)
        print("Product added successfully.")

    def menu(self):
        while True:
            print("\nProduct Management")
            print("1. Add Product")
            print("2. List Products")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.list_products()
            elif choice == '3':
                break
            else:
                print("Invalid option.")
