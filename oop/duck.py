
class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print('gau gau')


class Cat(Animal):
    def speak(self):
        print('meo meo')


class Car: # ko phai con cua animal nhung se chay cac thuoc tinh neu giong cac class con cua animal

    alive = False
    def speak(self):
        print('Brum Brum')


animals = [Dog(), Cat(), Car()]


for animal in animals:
    animal.speak()
    print(animal.alive)