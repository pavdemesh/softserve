"""
Define class with unknown number of keyword arguments.
"""


class Employee:

    def __init__(self, full_name, **kwargs):
        split_name = full_name.split()
        self.name = split_name[0]
        self.lastname = split_name[1]

        for key, value in kwargs.items():
            setattr(self, key, value)


john = Employee('Kohn Doe', nationality="Italian", height=198)
print(john.lastname)
print(john.height)
