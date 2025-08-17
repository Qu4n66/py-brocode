#object = A bundle of related attributes (variables) and methods (function)


from car import *


car1 = Car('Mercedez', '2025', 'Black', 'yes')
car2 = Car('Roll Royce', '2026', 'NIgga', 'not')

car1.describe()
car2.describe()

print(Car.chairs)

print(f'Iam totally selling {Car.num_cars} cars')# class variable



honda = Car_store("oto")

honda.drive()
