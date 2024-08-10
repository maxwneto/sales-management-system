from controllers.supplier_controller import SupplierController

class SupplierView:
    def __init__(self):
        self.supplier_controller = SupplierController()

    def add_supplier(self):
        name = input("Enter supplier name: ")
        contact_info = input("Enter supplier contact info: ")
        self.supplier_controller.add_supplier(name, contact_info)
        print(f"Supplier '{name}' added successfully.")

    def update_supplier(self):
        supplier_id = input("Enter supplier ID to update: ")
        name = input("Enter new name (leave blank to keep current): ").strip()
        contact_info = input("Enter new contact info (leave blank to keep current): ").strip()
        self.supplier_controller.update_supplier(supplier_id, name or None, contact_info or None)

    def delete_supplier(self):
        supplier_id = input("Enter supplier ID to delete: ")
        self.supplier_controller.delete_supplier(supplier_id)

    def list_suppliers(self):
        suppliers = self.supplier_controller.list_suppliers()
        if not suppliers:
            print("No suppliers available.")
            return
        
        print("\nList of Suppliers")
        print("----------------------------------------------------------------------------------------------------")
        print(f"{'ID':<10} {'Name':<20} {'Contact Info':<30}")
        print("----------------------------------------------------------------------------------------------------")
        for supplier in suppliers:
            print(f"{supplier['id']:<10} {supplier['name']:<20} {supplier['contact_info']:<30}")
        print("----------------------------------------------------------------------------------------------------")

    def menu(self):
        while True:
            print("\nSupplier Management")
            print("1. Add Supplier")
            print("2. List Suppliers")
            print("3. Update Supplier")
            print("4. Delete Supplier")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_supplier()
            elif choice == '2':
                self.list_suppliers()
            elif choice == '3':
                self.update_supplier()
            elif choice == '4':
                self.delete_supplier()
            elif choice == '5':
                break
            else:
                print("Invalid option.")
