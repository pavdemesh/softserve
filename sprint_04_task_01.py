"""
Define class Employee with static method from_string() to parse dash-separated string data
"""


class Employee:

    def __init__(self, first, last, money):
        self.firstname = first
        self.lastname = last
        self.salary = money

    @classmethod
    def from_string(cls, string_data):
        employee_data = string_data.split("-")
        worker = cls(employee_data[0], employee_data[1], int(employee_data[2]))
        return worker


e1 = Employee('Mary', 'Johnson', 5000)
print(e1.lastname)

e2 = Employee.from_string('Peter-Parker-19999')
print(e2.salary)
