#factory pattern design
#factory pattern is used to create objects without exposing the instantiation logic to the client
#factory pattern is used when we have a super class with multiple sub-classes and based on input, we need to return one of the sub-class

# example 1:
# it comes under the creational 
# Design Pattern
class vehicle:
    def create_vehicle(self):
        pass
class Car(vehicle):
    def create_vehicle(self):
        return "car is created!!"
class Bike(vehicle):
    def create_vehicle(self):
        return "bike is created!!"
class vehicleFactory:
    def getVehicle(self,vehicleType):
        if vehicleType=="car":
            return Car()
        elif vehicleType=="bike":
            return Bike()
        else:
            return "No vehicle found"
        
car=vehicleFactory()
print(car.getVehicle("car").create_vehicle())
bike=vehicleFactory()
print(bike.getVehicle("bike").create_vehicle())


# example 2:
# Python Code for factory method 
# it comes under the creational 
# Design Pattern

class FrenchLocalizer:

    """ it simply returns the french version """

    def __init__(self):

        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg

def Factory(language ="English"):

    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()

if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
