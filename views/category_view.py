# category_view.py
from controllers.category_controller import CategoryController

class CategoryView:
    def __init__(self):
        self.category_controller = CategoryController()

    def add_category(self):
        name = input("Enter category name: ").strip()
        existing_category = self.category_controller.get_category_by_name(name)
        if existing_category:
            print(f"Category '{name}' already exists.")
        else:
            self.category_controller.create_category(name)
            print(f"Category '{name}' added successfully.")

    def list_categories(self):
        categories = self.category_controller.list_categories()
        if not categories:
            print("No categories available.")
        else:
            print("Available categories:")
            for category in categories:
                print(f"Name: {category['name']}")

    def menu(self):
        while True:
            print("\nCategory Management")
            print("1. Add Category")
            print("2. List Categories")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_category()
            elif choice == '2':
                self.list_categories()
            elif choice == '3':
                break
            else:
                print("Invalid option.")
