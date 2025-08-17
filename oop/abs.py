
#Abstraction


from abc import ABC, abstractmethod

#lớp trừu tượng
class Animal(ABC):
    #phuong thuc truu tuong

    @abstractmethod # bat buoc cac class con phai co ham speak
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return 'Gau Gau'
    

dog = Dog()
print(dog.speak())






