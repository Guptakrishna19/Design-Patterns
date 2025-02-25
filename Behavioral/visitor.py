"""
Defination:-The Visitor Pattern is a behavioral design pattern that allows adding new operations
            to a class hierarchy without modifying the classes themselves. 
            It helps separate the algorithm (operations) from the objects on which they operate
"""

from abc import ABC, abstractmethod

# 🔹 Step 1: Define Employee Base Class (Element)
class Employee(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# 🔹 Step 2: Concrete Employee Classes
class Developer(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def accept(self, visitor):
        visitor.visit_developer(self)

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def accept(self, visitor):
        visitor.visit_manager(self)

# 🔹 Step 3: Define Visitor Interface
class EmployeeVisitor(ABC):
    @abstractmethod
    def visit_developer(self, developer):
        pass

    @abstractmethod
    def visit_manager(self, manager):
        pass

# 🔹 Step 4: Concrete Visitor (Salary Calculation)
class SalaryCalculator(EmployeeVisitor):
    def visit_developer(self, developer):
        print(f"Developer {developer.name} has a salary of ${developer.salary}")

    def visit_manager(self, manager):
        total_salary = manager.salary + manager.bonus
        print(f"Manager {manager.name} has a total salary of ${total_salary}")

# 🔹 Step 5: Client Code
if __name__ == "__main__":
    # Create employees
    dev = Developer("Alice", 80000)
    mgr = Manager("Bob", 100000, 20000)

    # Create a visitor
    salary_calculator = SalaryCalculator()

    # Apply visitor to elements
    dev.accept(salary_calculator)
    mgr.accept(salary_calculator)

