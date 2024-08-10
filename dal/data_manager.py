import json
import os

class DataManager:
    def __init__(self, file_name):
        # Defina o caminho do diretório 'db_file'
        self.file_directory = os.path.join(os.path.dirname(__file__), '../db_file')
        if not os.path.exists(self.file_directory):
            os.makedirs(self.file_directory)

        # Defina o caminho completo do arquivo
        self.file_path = os.path.join(self.file_directory, file_name)

    def load_data(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
