class Animal:
    def make_sound(self):
        pass  # lớp cha không cần biết kêu thế nào

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow~")

class Duck(Animal):
    def make_sound(self):
        print("Quack!")

animals = [Dog(), Cat(), Duck()] #Cùng một lời gọi phương thức, nhưng hành vi khác nhau tùy đối tượng

for animal in animals:
    animal.make_sound()
