from views.client_view import ClientView
from views.employee_view import EmployeeView
from views.supplier_view import SupplierView
from views.product_view import ProductView
from views.sale_view import SaleView
from views.category_view import CategoryView  # Importando a CategoryView

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Clients")
        print("2. Manage Employees")
        print("3. Manage Suppliers")
        print("4. Manage Categories")  # Categoria na quarta opção
        print("5. Manage Products")
        print("6. Manage Sales")
        print("7. Exit")  # Opção de saída como última
        choice = input("Choose an option: ")
        if choice == '1':
            ClientView().menu()
        elif choice == '2':
            EmployeeView().menu()
        elif choice == '3':
            SupplierView().menu()
        elif choice == '4':
            CategoryView().menu()  # Opção correta para gerenciar categorias
        elif choice == '5':
            ProductView().menu()
        elif choice == '6':
            SaleView().menu()
        elif choice == '7':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
