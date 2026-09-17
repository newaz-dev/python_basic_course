class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, password,  new_salary):
        if password == "admin":
            self._salary = new_salary
        else:
            return "Acess Denied"
        
emp1 = Employee("Fahmir", 40000)
print(emp1.salary)
emp1.salary("admin", 90000)
print(emp1.salary)
