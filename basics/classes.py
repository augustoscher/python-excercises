class Car:
    def __init__(self, color, age):
        self.color = color
        self.age = age


car1 = Car("red", 1)
print(car1)
print(car1.color)
car1.color = "blue"
print(car1.color)