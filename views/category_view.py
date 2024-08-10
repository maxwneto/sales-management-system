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

    def update_category(self):
        old_name = input("Enter the current category name to update: ").strip()
        new_name = input("Enter the new category name: ").strip()
        self.category_controller.update_category(old_name, new_name)

    def delete_category(self):
        name = input("Enter the category name to delete: ").strip()
        self.category_controller.delete_category(name)

    def list_categories(self):
        categories = self.category_controller.list_categories()
        if not categories:
            print("No categories available.")
        else:
            print("\nAvailable Categories")
            print("----------------------------------------------------------------------------------------------------")
            print(f"{'Category Name':<30}")
            print("----------------------------------------------------------------------------------------------------")
            for category in categories:
                print(f"{category['name']:<30}")
            print("----------------------------------------------------------------------------------------------------")

    def menu(self):
        while True:
            print("\nCategory Management")
            print("1. Add Category")
            print("2. List Categories")
            print("3. Update Category")
            print("4. Delete Category")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_category()
            elif choice == '2':
                self.list_categories()
            elif choice == '3':
                self.update_category()
            elif choice == '4':
                self.delete_category()
            elif choice == '5':
                break
            else:
                print("Invalid option.")
