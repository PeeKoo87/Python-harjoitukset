hytti = input("mikä hyttiluokka?")

LUX1 = ("parvekkeellinen hytti yläkannella")
A2 = ("ikkunallinen hytti autokannen yläpuolella")
B3 = ("ikkunaton hytti autokannen yläpuolella")
C4 = ("ikkunaton hytti autokannen alapuolella")

if hytti == "LUX" or hytti == "Lux" or hytti == "lux":
    print(LUX1)

elif hytti == "A" or hytti == "a":
    print(A2)

elif hytti == "B" or hytti == "b":
    print(B3)

elif hytti == "C" or hytti == "c":
    print(C4)

else:
    print("virheellinen hyttiluokka")