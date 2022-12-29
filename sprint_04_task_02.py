
class Pizza:
    orders = [0]

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.orders[0] += 1
        self.order_number = Pizza.orders[0]

    @classmethod
    def hawaiian(cls):
        hawaii_pizza = cls(['ham', 'pineapple'])
        return hawaii_pizza


p1 = Pizza(['ham', 'beacon'])
p2 = Pizza.hawaiian()
print(p1.order_number)
print(p2.order_number)
print(p2.ingredients)
