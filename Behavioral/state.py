'''definitation :- The State Pattern allows an object to change its behavior when its internal state changes. 
It helps in organizing code that depends on multiple conditions, making it more maintainable.'''


from abc import ABC, abstractmethod

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def change(self, traffic_light):
        pass

    @abstractmethod
    def show(self):
        pass

# Concrete States
class RedLight(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = GreenLight()  # Switch to Green

    def show(self):
        return "Red Light - STOP 🚦"

class GreenLight(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = YellowLight()  # Switch to Yellow

    def show(self):
        return "Green Light - GO ✅"

class YellowLight(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = RedLight()  # Switch to Red

    def show(self):
        return "Yellow Light - SLOW DOWN ⚠️"

# Context: Traffic Light
class TrafficLight:
    def __init__(self):
        self.state = RedLight()  # Default state

    def change(self):
        self.state.change(self)  # Change to next state

    def show(self):
        return self.state.show()  # Show current state

# Example Usage
if __name__ == "__main__":
    light = TrafficLight()

    for _ in range(5):
        print(light.show())  # Display current state
        light.change()       # Move to next state
