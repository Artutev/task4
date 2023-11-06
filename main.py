#1

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

my_car = Car("красный", 100)

print(f"Скорость моей машины: {my_car.speed} км/ч")


#2

import re

class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

while True:
    speed_input = input("Введите скорость машины (км/ч): ")
    if re.match(r'^\d+$', speed_input):
        speed = int(speed_input)
        break
    else:
        print("Неверный ввод. Введите положительное число.")

my_car = Car("красный", speed)

print(f"Скорость моей машины: {my_car.speed} км/ч")
