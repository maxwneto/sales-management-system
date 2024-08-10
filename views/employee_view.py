from controllers.employee_controller import EmployeeController

class EmployeeView:
    def __init__(self):
        self.employee_controller = EmployeeController()

    def add_employee(self):
        name = input("Enter employee name: ")
        email = input("Enter employee email: ")
        phone = input("Enter employee phone: ")
        self.employee_controller.add_employee(name, email, phone)
        print("Employee added successfully.")

    def list_employees(self):
        employees = self.employee_controller.list_employees()
        for employee in employees:
            print(f"ID: {employee['employee_id']}, Name: {employee['name']}, Email: {employee['email']}, Phone: {employee['phone']}")

    def menu(self):
        while True:
            print("\nEmployee Management")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.list_employees()
            elif choice == '3':
                break
            else:
                print("Invalid option.")
