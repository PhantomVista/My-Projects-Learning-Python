# Using Classes to create name variables and call on them after def.

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


Goku = Person("Goku")
Goku.talk()

Vegeta = Person("Vegeta")
Vegeta.talk()


# Using Inheritance


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def yawn(self):
        print("yawn")


dog = Dog()
dog.bark()
dog.walk()
cat = Cat()
cat.walk()
cat.yawn()


