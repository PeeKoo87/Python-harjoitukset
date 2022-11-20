class elevator:
    def __init__(self,name, floorMin, floorMax):
        self.name = name
        self.floorMin = floorMin
        self.floorMax = floorMax
        self.currentFloor = 0
        self.tf = 0

    def floor_up(self):
        self.currentFloor = self.currentFloor + 1
        print(f"olet kerroksessa {self.currentFloor}")

    def floor_down(self):
        self.currentFloor = self.currentFloor - 1
        print(f"olet kerroksessa {self.currentFloor}")

    def moveToFloor(self, goal):
        self.tf = goal

        while self.currentFloor != self.tf:
            if self.currentFloor > goal:
                elevator.floor_down(self)

            elif self.currentFloor < self.floorMax:
                elevator.floor_up(self)

        if self.currentFloor == self.tf:
            print(f"olet tavoite kerroksessa: {goal}")


# tehtävä 1
print("hissi tehtävään 1")
elevator1 = elevator("",0, 5)
elevator1.moveToFloor(5)
elevator1.moveToFloor(0)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class building:
    def __init__(self,floorMin, floorMax, elevNum):
        self.floorMin = floorMin
        self.floorMax = floorMax
        self.elevList = elevNum
        self.elevList = []

        for i in range(elevNum):
            eleL = elevator("a"+str(i+1),floorMin, floorMax)
            self.elevList.append(eleL)

    def rideElevator(self, elevS, goal):
        elevSpesific = self.elevList[elevS - 1]
        elevSpesific.moveToFloor(goal)

    def fireAlarm(self):
        print("palohälytys!!")
        for i in range(len(self.elevList)):
            b1.rideElevator(len(self.elevList), self.floorMin)


b1 = building("",1, 7, 3)
b2 = building("",0, 9, 2)

b1.rideElevator("",1, 7)
b1.rideElevator("",2, 5)
b1.rideElevator("",3, 4)
# b2.rideElevator(1,9)
b1.fireAlarm()
