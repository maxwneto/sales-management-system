from dal.data_manager import DataManager
from models.sale import Sale

class SaleController:
    def __init__(self):
        self.data_manager = DataManager('sales.json')
        self.sales = self.data_manager.load_data()

    def add_sale(self, client, products, date):
        sale = Sale(client, products, date)
        self.sales.append(sale.__dict__)
        self.data_manager.save_data(self.sales)

    def list_sales(self):
        return self.sales

    def sales_report(self):
        return self.sales

    def sales_by_date(self, date):
        return [sale for sale in self.sales if sale['date'] == date]

    def top_selling_products(self):
        product_sales = {}
        for sale in self.sales:
            for product in sale['products']:
                product_sales[product['name']] = product_sales.get(product['name'], 0) + 1
        return sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

    def top_clients(self):
        client_sales = {}
        for sale in self.sales:
            client_sales[sale['client']['name']] = client_sales.get(sale['client']['name'], 0) + 1
        return sorted(client_sales.items(), key=lambda x: x[1], reverse=True)
