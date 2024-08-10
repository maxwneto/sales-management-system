# category_controller.py
from dal.data_manager import DataManager
from models.category import Category

class CategoryController:
    def __init__(self):
        self.data_manager = DataManager('categories.json')
        self.categories = self.data_manager.load_data()

    def get_category_by_name(self, name):
        for category in self.categories:
            if category['name'].lower() == name.lower():
                return category
        return None

    def create_category(self, name):
        new_category = Category(name)
        self.categories.append(new_category.__dict__)
        self.data_manager.save_data(self.categories)
        return new_category.__dict__

    def list_categories(self):
        return self.categories
