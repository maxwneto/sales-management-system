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
        # Garante que product_id seja comparado corretamente com o ID do produto
        for product in self.products:
            if str(product.get('id')) == str(product_id):
                return product
        return None

    def update_product(self, updated_product):
        for i, product in enumerate(self.products):
            if product['id'] == updated_product['id']:
                self.products[i] = updated_product  # Atualiza o produto na lista
                self.data_manager.save_data(self.products)
                return True
        return False
