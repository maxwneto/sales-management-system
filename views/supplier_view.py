from controllers.supplier_controller import SupplierController

class SupplierView:
    def __init__(self):
        self.supplier_controller = SupplierController()

    def add_supplier(self):
        name = input("Enter supplier name: ")
        contact_info = input("Enter supplier contact info: ")
        self.supplier_controller.add_supplier(name, contact_info)
        print("Supplier added successfully.")

    def list_suppliers(self):
        suppliers = self.supplier_controller.list_suppliers()
        for supplier in suppliers:
            print(supplier)

    def menu(self):
        while True:
            print("\nSupplier Management")
            print("1. Add Supplier")
            print("2. List Suppliers")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_supplier()
            elif choice == '2':
                self.list_suppliers()
            elif choice == '3':
                break
            else:
                print("Invalid option.")
