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

    def update_employee(self):
        employee_id = input("Enter employee ID to update: ")
        name = input("Enter new name (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()
        phone = input("Enter new phone (leave blank to keep current): ").strip()
        self.employee_controller.update_employee(employee_id, name or None, email or None, phone or None)

    def delete_employee(self):
        employee_id = input("Enter employee ID to delete: ")
        self.employee_controller.delete_employee(employee_id)

    def list_employees(self):
        employees = self.employee_controller.list_employees()
        if not employees:
            print("No employees available.")
            return
        
        print("\nList of Employees")
        print("----------------------------------------------------------------------------------------------------")
        print(f"{'ID':<10} {'Name':<20} {'Email':<30} {'Phone':<15}")
        print("----------------------------------------------------------------------------------------------------")
        for employee in employees:
            print(f"{employee['employee_id']:<10} {employee['name']:<20} {employee['email']:<30} {employee['phone']:<15}")
        print("----------------------------------------------------------------------------------------------------")

    def menu(self):
        while True:
            print("\nEmployee Management")
            print("1. Add Employee")
            print("2. List Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.list_employees()
            elif choice == '3':
                self.update_employee()
            elif choice == '4':
                self.delete_employee()
            elif choice == '5':
                break
            else:
                print("Invalid option.")
