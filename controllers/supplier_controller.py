from dal.data_manager import DataManager
from models.supplier import Supplier

class SupplierController:
    def __init__(self):
        self.data_manager = DataManager('suppliers.json')
        self.suppliers = self.data_manager.load_data()

    def add_supplier(self, name, contact_info):
        supplier = Supplier(name, contact_info)
        self.suppliers.append(supplier.__dict__)
        self.data_manager.save_data(self.suppliers)

    def list_suppliers(self):
        return self.suppliers
