# models/sale.py
class Sale:
    def __init__(self, client, products, date):
        self.client = client
        self.products = products
        self.date = date
