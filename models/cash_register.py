# models/cash_register.py

import json
import os

class CashRegister:
    def __init__(self):
        self.file_path = os.path.join(os.getcwd(), 'db_file', 'cash_register.json')
        self.total_sales = self.load_cash()
        print(f"[DEBUG] Initial Cash Total Loaded: {self.total_sales}")

    def add_sale(self, amount):
        # Adiciona a nova venda ao total existente
        self.total_sales += amount
        print(f"[DEBUG] Adding Sale: {amount}, New Total: {self.total_sales}")
        self.save_cash()

    def get_total_sales(self):
        return self.total_sales

    def load_cash(self):
        # Verifica se o arquivo existe e carrega os dados
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                print(f"[DEBUG] Cash Register Loaded Data: {data}")
                return data.get('total_sales', 0.0)
        print("[DEBUG] Cash Register File Not Found, Initializing with 0.0")
        return 0.0

    def save_cash(self):
        # Certifica-se de que o diretório 'db_file' existe
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        # Escreve o valor total acumulado de volta no arquivo
        with open(self.file_path, 'w') as file:
            json.dump({'total_sales': self.total_sales}, file)
            print(f"[DEBUG] Cash Register Saved: {self.total_sales}")

    def reset(self):
        # Reseta o valor total para 0.0 e salva
        self.total_sales = 0.0
        self.save_cash()
        print("[DEBUG] Cash Register Reset to 0.0")
