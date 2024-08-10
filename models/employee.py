from .person import Person

class Employee(Person):
    def __init__(self, name, email, phone, employee_id=None):
        super().__init__(name, email, phone)
        self.employee_id = employee_id
