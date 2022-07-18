#QUES1
class Thing:
    pass
print(Thing)

example = Thing()
print(example)

#QUES 2
class Thing2:
    letters = "abc"

print(Thing2.letters)


#QUES 3
class Thing3:
    def __init__(self):
        self.letters = "xyz"
try:
    print(Thing3.letters())
except:
    thing_ = Thing3()
    print(thing_.letters)
# yeah we need to make object from class


#QUES 4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

my_elements = Element('Hydrogen', 'H', 1)


#QUES 5
dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
print(dict)
hydrogen = Element(*dict.values())


#QUES6
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()


#QUES7
print(hydrogen)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'{self.name} {self.symbol} {self.number}'

Hydrogen = Element('Hydrogen', 'H', 1)

print(Hydrogen)


#QUES 8
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def get_name(self):
        return self.__name

    @property
    def get_symbol(self):
        return self.__symbol

    @property
    def get_number(self):
        return self.__number


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.get_name)
print(hydrogen.get_symbol)
print(hydrogen.get_number)


#QUES 9
class Bear:
    def eats(self):
        print('berries')
class Rabbbit:
    def eats(self):
        print('clover')
class Octothorpe:
    def eats(self):
        print('campers')

b = Bear()
r = Rabbbit()
o = Octothorpe()
b.eats()
r.eats()
o.eats()


#QUES 10
class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class Smartphone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()

    def does(self):
        print(self.laser.does(), self.claw.does(), self.smartphone.does())

R = Robot()
R.does()