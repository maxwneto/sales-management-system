import os
from views.client_view import ClientView
from views.employee_view import EmployeeView
from views.supplier_view import SupplierView
from views.product_view import ProductView
from views.sale_view import SaleView
from views.category_view import CategoryView

def clear_screen():
    # Comando para limpar a tela, depende do SO
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, Mac, etc.
        os.system('clear')

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Clients")
        print("2. Manage Employees")
        print("3. Manage Suppliers")
        print("4. Manage Categories")
        print("5. Manage Products")
        print("6. Manage Sales")
        print("7. Cash Report")
        print("8. Clear Screen")
        print("9. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            ClientView().menu()
        elif choice == '2':
            EmployeeView().menu()
        elif choice == '3':
            SupplierView().menu()
        elif choice == '4':
            CategoryView().menu()
        elif choice == '5':
            ProductView().menu()
        elif choice == '6':
            SaleView().menu()
        elif choice == '7':
            SaleView().cash_report()
        elif choice == '8':
            clear_screen()
        elif choice == '9':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
