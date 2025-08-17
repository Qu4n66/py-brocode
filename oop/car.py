class Car:

    chairs = 6 #class variable
    num_cars = 0
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        Car.num_cars += 1

    def drive(self):
        print(f'{self.model} dag chay Veo Veo brum brumm..')  
    def stop(self):
        print(f'{self.model} mau {self.color} dung lai kit kit kit')  

    def describe(self):
        print(f'{self.model} released {self.year} with color {self.color} and now {self.for_sale} for sale')


class Car_store(Car):
    pass
