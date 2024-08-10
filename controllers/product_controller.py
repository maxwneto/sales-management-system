from dal.data_manager import DataManager
from models.product import Product

class ProductController:
    def __init__(self):
        self.data_manager = DataManager('products.json')
        self.products = self.data_manager.load_data()

    def add_product(self, name, price, category, quantity):
        product_id = len(self.products) + 1
        product = Product(name, price, category, product_id, quantity)
        self.products.append(product.__dict__)
        self.data_manager.save_data(self.products)

    def list_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.get('id') == int(product_id):
                return product
        return None

    def update_product(self, product_id, name=None, price=None, category=None, quantity=None):
        product = self.get_product_by_id(product_id)
        if product:
            if name:
                product['name'] = name
            if price is not None:
                product['price'] = price
            if category:
                product['category'] = category
            if quantity is not None:
                product['quantity'] = quantity
            self.data_manager.save_data(self.products)
            print(f"Product ID {product_id} updated successfully.")
        else:
            print(f"Product ID {product_id} not found.")

    def delete_product(self, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            self.products.remove(product)
            self.data_manager.save_data(self.products)
            print(f"Product ID {product_id} deleted successfully.")
        else:
            print(f"Product ID {product_id} not found.")
