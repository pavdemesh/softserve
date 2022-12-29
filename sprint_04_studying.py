class A:
    name = "mara"
    f = 15


c = A()


def my(self):
    print(f'name is {self.name} and f is {self.f}')


A.raw = my
c.raw()
