class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self, password):
        if password == 'newaz123':
            print(f"Salary of Employee1: {self._salary}")
        else:
            print("Invalid Access!")
    def set_salary(self, password, salary):
        if password == 'newaz123':
            self._salary = salary
            print(f"New Salary: {salary}")
        else:
            print("Invalid Access!")
emp1 = Employee("Newaz", 50000)
emp1.get_salary("newaz123")
emp1.set_salary('newaz123', 276826)

