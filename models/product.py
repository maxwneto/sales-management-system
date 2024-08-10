# models/product.py
class Product:
    def __init__(self, name, price, category, product_id, quantity):
        self.name = name
        self.price = price
        self.category = category
        self.id = product_id
        self.quantity = quantity
