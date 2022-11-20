import random
import string

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
              f"tämänhetkinen nopeus {self.speed}km/h ")

#random.choice(string.ascii_uppercase)
#x = 3
#def random_letter(x):
    #return ''.join(random.choice(string.ascii_uppercase) for a in range(x))


#def random_number():
   # nums = '123456789'
    #numbers = ''
   # for a in range(3):
        #numbers += random.choice(nums)
    #return numbers
#letters = random_letter(x)
#numbers = random_number()
#for i in range(3):
    #rint(f"{letters}-{numbers}")
#print(random_letter(3))
#print(random_number())
#cars = list[""]
#def car_list(random_letter,random_number):

    #for i in range(10):
        #cars.append(Car[random_letter(3) + random_number()])
       # Car()
        #print(cars)

#for car in cars:
    #print(car.print_info())
#print(cars)

#for i in range():
    #print(''.join[random_letter(3)]+['']+[random_number(3)])



#def regGen(self):
    #chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #numbs = '123456789'
    #letters = ''
    #numbers = ''
    # plateNum = 10
    #for i in range(3):
        #letters += random.choice(chars)

    #for i in range(3):
        #numbers += random.choice(numbs)

    #msp = random.randint(100, 200)
    #print(f"{letters}-{numbers}{msp}")
    #print(letters)
    #print(numbers)
    #print(msp)

    #for i in range(10):
       #cars.append(self.register_number(f"{letters}-{numbers}{msp}"))
        #Car()


cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i), random.randint(100,200)))

for Car in cars:
    print(Car.print_info())