class Vehicle:

    type='Vehicle'

    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year

    def showVehicle(self):
        print("Type of vehicle:",self.type)
        print("Model Name of vehicle:",self.modelname)
        print("Manufacturing Year of vehicle:",self.year)

class Car:

    type='Luxury Car'

    def __init__(self,modelname,year,cc):
        Vehicle.__init__(self,modelname,year)
        self.cc=cc

    def displayCar(self):
        print("Type of Car:",self.type)
        print("Model Name:",self.modelname)
        print("CC :",self.cc)


c2=Car("Honda",2007,1200)
c2.displayCar()


        
        
