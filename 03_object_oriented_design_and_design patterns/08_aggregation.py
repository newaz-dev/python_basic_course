# Aggregation: has a Relationship: Weak type
# Kinda Independent type

class Department:
    def __init__(self, name):
        self.name = name


class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_departments(self, department):
        self.departments.append(department)
        
    def display_departments(self):
        return [department.name for department in self.departments]
    

university = University("Daffodil International University")

dep1 = Department("CSE")
dep2 = Department("SWE")
dep3 = Department("EEE")

university.add_departments(dep1)
university.add_departments(dep2)
university.add_departments(dep3)

print(university.display_departments())
