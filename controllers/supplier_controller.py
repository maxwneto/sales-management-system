from dal.data_manager import DataManager
from models.supplier import Supplier
import os

class SupplierController:
    def __init__(self):
        # Define o caminho absoluto para a pasta db_file dentro do projeto
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Sobe um nível no diretório
        file_path = os.path.join(base_dir, 'db_file', 'suppliers.json')  # Caminho para db_file/suppliers.json
        
        # Cria o diretório db_file se ele não existir
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        self.data_manager = DataManager(file_path)
        self.suppliers = self.data_manager.load_data()

    def add_supplier(self, name, contact_info):
        supplier_id = len(self.suppliers) + 1
        supplier = Supplier(name, contact_info, supplier_id)
        self.suppliers.append(supplier.__dict__)
        self.data_manager.save_data(self.suppliers)

    def list_suppliers(self):
        if not self.suppliers:
            print("No suppliers available.")
            return []
        
        return self.suppliers

    def get_supplier_by_id(self, supplier_id):
        for supplier in self.suppliers:
            if str(supplier.get('id')) == str(supplier_id):
                return supplier
        return None

    def update_supplier(self, supplier_id, name=None, contact_info=None):
        supplier = self.get_supplier_by_id(supplier_id)
        if supplier:
            if name:
                supplier['name'] = name
            if contact_info:
                supplier['contact_info'] = contact_info
            self.data_manager.save_data(self.suppliers)
            print(f"Supplier ID {supplier_id} updated successfully.")
        else:
            print(f"Supplier ID {supplier_id} not found.")

    def delete_supplier(self, supplier_id):
        supplier = self.get_supplier_by_id(supplier_id)
        if supplier:
            self.suppliers.remove(supplier)
            self.data_manager.save_data(self.suppliers)
            print(f"Supplier ID {supplier_id} deleted successfully.")
        else:
            print(f"Supplier ID {supplier_id} not found.")
