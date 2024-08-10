from dal.data_manager import DataManager
from models.employee import Employee

class EmployeeController:
    def __init__(self):
        self.data_manager = DataManager('employees.json')
        self.employees = self.data_manager.load_data()

    def add_employee(self, name, email, phone):
        employee_id = len(self.employees) + 1
        employee = Employee(name, email, phone, employee_id)
        self.employees.append(employee.__dict__)
        self.data_manager.save_data(self.employees)

    def list_employees(self):
        return self.employees

    def get_employee_by_id(self, employee_id):
        for employee in self.employees:
            if str(employee.get('employee_id')) == str(employee_id):
                return employee
        return None

    def update_employee(self, employee_id, name=None, email=None, phone=None):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            if name:
                employee['name'] = name
            if email:
                employee['email'] = email
            if phone:
                employee['phone'] = phone
            self.data_manager.save_data(self.employees)
            print(f"Employee ID {employee_id} updated successfully.")
        else:
            print(f"Employee ID {employee_id} not found.")

    def delete_employee(self, employee_id):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            self.employees.remove(employee)
            self.data_manager.save_data(self.employees)
            print(f"Employee ID {employee_id} deleted successfully.")
        else:
            print(f"Employee ID {employee_id} not found.")
