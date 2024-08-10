from dal.data_manager import DataManager
from models.sale import Sale
from models.cash_register import CashRegister

class SaleController:
    def __init__(self):
        self.data_manager = DataManager('sales.json')
        self.sales = self.data_manager.load_data()
        self.cash_register = None  # Inicializa como None

    def _initialize_cash_register(self):
        if self.cash_register is None:
            self.cash_register = CashRegister()

    def add_sale(self, client, products, date):
        self._initialize_cash_register()  # Garante que o CashRegister é inicializado somente quando necessário
        sale = Sale(client, products, date)
        self.sales.append(sale.__dict__)
        self.data_manager.save_data(self.sales)

        # Calcula o total da venda e adiciona ao caixa
        total_sale_amount = sum(item['price'] * item['quantity'] for item in products)
        self.cash_register.add_sale(total_sale_amount)

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
                product_sales[product['name']] = product_sales.get(product['name'], 0) + product['quantity']
        return sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

    def top_clients(self):
        client_sales = {}
        for sale in self.sales:
            client_name = sale['client']['name']
            total_sale = sum(item['price'] * item['quantity'] for item in sale['products'])
            client_sales[client_name] = client_sales.get(client_name, 0) + total_sale
        return sorted(client_sales.items(), key=lambda x: x[1], reverse=True)

    def get_cash_total(self):
        self._initialize_cash_register()  # Garante que o CashRegister é inicializado somente quando necessário
        return self.cash_register.get_total_sales()
