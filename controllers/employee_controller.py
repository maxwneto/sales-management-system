from dal.data_manager import DataManager
from models.employee import Employee

class EmployeeController:
    def __init__(self):
        self.data_manager = DataManager('employees.json')
        self.employees = self.data_manager.load_data()

    def add_employee(self, name, email, phone):
        # Gerando um ID único baseado no número de funcionários existentes
        employee_id = len(self.employees) + 1
        employee = Employee(name, email, phone, employee_id)
        self.employees.append(employee.__dict__)
        self.data_manager.save_data(self.employees)

    def list_employees(self):
        return self.employees

    def get_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee.get('employee_id') == employee_id:
                return employee
        return None
