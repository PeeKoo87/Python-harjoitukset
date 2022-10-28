import random

cars = []
#luodaan auto olio
class Car:
    def __init__(self, register_number, max_speed):
        self.register_number = register_number
        self.max_speed = max_speed
        self.odometer = 0
        self.speed = 0

#olion tietojen tulostus
    def print_info(self):
        print(f"Auton {self.register_number} "
              f"huippunopeus on {self.max_speed}km/h "
              f"ja matkamittari {self.odometer}km "
              f"tämän hetkinen nopeus {self.speed}km/h ")

#kiihdytys funktio
    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change < self.max_speed:
            self.speed = self.speed + speed_change

        elif self.speed + speed_change <= 0:
            self.speed = 0

        elif self.speed + speed_change >= self.max_speed:
            self.speed = self.max_speed

#matkamittarin laskuri
    def travel(self, time):
        self.odometer += self.speed * time

#auto listan luonti
for i in range(10):
    cars.append(Car("ABC-" + str(i), random.randint(100, 200)))

#pääohjelma
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