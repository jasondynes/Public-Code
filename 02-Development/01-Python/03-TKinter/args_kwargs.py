# demonstrate multiple positional arguments using *args
def add(*args):
    calc = 0
    for x in args:
        calc += x
    # can also operate on individual items as tuple
    # e.g. print(args[1])
    return calc


# demonstrate multiple keyword arguments using **kwargs

def calculate(**kwargs):
    calc = 0
    for key, value in kwargs.items():
        if key == "add":
            calc += value
        elif key == "subtract":
            calc -= value
        elif key == "multiply":
            calc *= value
        elif key == "divide":
            calc /= value
        else:
            return "error"
    return calc


# demonstrate multiple keyword arguments using **kwargs with other arguments and referencing kwargs directly

def calculate2(num, **kwargs):
    # print(kwargs)
    num += kwargs["add"]
    num *= kwargs["multiply"]
    return num


# creating a class with **kwargs and using get so we return NONE from dictionary
# if not attribute is set as a kwarg
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


print(add(1, 2, 3, 4, 5))
print(calculate(add=3, multiply=5))
print(calculate2(2, add=3, multiply=5))

# accessing Car instance and showing NONE for model rather than KeyError due to use of GET in class __init__
my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)

