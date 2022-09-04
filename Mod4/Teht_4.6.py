import random
interval = int(input("Kerro arvottavien pisteiden määrä"))
circle_points = 0
square_points = 0
print("lasketaan odota hetki...")
for i in range(interval**2):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    origin_dist = x**2 + y**2
    if origin_dist <=1:
        circle_points +=1

    square_points +=1

    pi = 4*circle_points / square_points





print("lopullinen piin arvioitu arvo=" ,pi)
