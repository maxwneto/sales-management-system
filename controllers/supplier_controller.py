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
