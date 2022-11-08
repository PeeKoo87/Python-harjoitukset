import random

cars = []

class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.max_speed = max_speed
        self.odometer = 0
        self.speed = 0

    def print_info(self):
        print(f"Auton {self.register_number} "
              f"huippunopeus on {self.max_speed}km/h "
              f"ja matkamittari {self.odometer}km "
              f"tämän hetkinen nopeus {self.speed}km/h ")


    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.max_speed:
            self.speed = self.speed + speed_change

        elif self.speed + speed_change <= 0:
            self.speed = 0

        elif self.speed + speed_change >= self.max_speed:
            self.speed = self.max_speed


    def travel(self, time):
        self.odometer += self.speed * time

class eCar(Car):
    def __init__(self, register_number, max_speed, battery):
        self.battery = battery
        super().__init__(register_number, max_speed)

class cCar(Car):
    def __init__(self, register_number, max_speed, fuelTank):
        self.fuelTank = fuelTank
        super().__init__(register_number, max_speed)

"""""
for i in range(10):
    cars.append(Car("ABC-" + str(i+1), random.randint(100, 200)))

stop = False
while not stop:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.travel(1)
        if car.odometer >= 10000:
            stop = True
            break

for c in cars:
    c.print_info()
"""""
car1 = eCar("ABC-15", 180, 52.5)
car2 = cCar("ADC-123", 165, 32.3)
car1.accelerate(180)
car2.accelerate(165)
car1.travel(3)
car2.travel(3)
car1.print_info()
car2.print_info()
