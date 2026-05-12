class Animal:
    def __init__(self):
        self.__name = 'Животное'
        self.__age = 0

    def make_sound(self):
        print("издает звук")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным!")

class Dog(Animal):
    def make_sound(self):
        print('Гав-Гав')


class Cat(Animal):
    def make_sound(self):
        print('МЯУ')


kitty = Cat()
kitty.set_age(3)
kitty.set_name('luna')
print(kitty.get_name(), kitty.get_age())
kitty.make_sound()
puppy = Dog()
puppy.set_age(5)
puppy.set_name('Baron')
print(puppy.get_name(), puppy.get_age())
puppy.make_sound()
