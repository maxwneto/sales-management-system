from dal.data_manager import DataManager
from models.product import Product

class ProductController:
    def __init__(self):
        self.data_manager = DataManager('products.json')
        self.products = self.data_manager.load_data()

    def add_product(self, name, price, category):
        # Gerando um ID único baseado no número de produtos existentes
        product_id = len(self.products) + 1
        product = Product(name, price, category, product_id)
        self.products.append(product.__dict__)
        self.data_manager.save_data(self.products)

    def list_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.get('id') == product_id:
                return product
        return None
