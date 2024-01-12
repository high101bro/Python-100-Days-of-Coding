def add(*args):
    sum_num = 0
    for n in args:
        sum_num += n
    return sum_num


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def test(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print('the key item:   ', key)
        print('the value item: ', value)

    print('\nchoosing the key', kwargs["add"])


test(add=3, multiply=5)


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)



class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']
        self.trim = kw.get('trim') # Note that if you don't provide it, using get will return None

my_car = Car(make='Mitsubishi', model='3000GT')
print(my_car.make)
print(my_car.model)
print(my_car.trim)


