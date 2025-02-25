# Subsystem 1: Light Control
class Light:
    def turn_on(self):
        print("Lights turned ON")

    def turn_off(self):
        print("Lights turned OFF")


# Subsystem 2: TV Control
class TV:
    def turn_on(self):
        print("TV turned ON")

    def turn_off(self):
        print("TV turned OFF")


# Subsystem 3: Air Conditioner Control
class AirConditioner:
    def turn_on(self):
        print("Air Conditioner turned ON")

    def turn_off(self):
        print("Air Conditioner turned OFF")


# Facade: Simplified interface to control all subsystems
class HomeAutomationFacade:
    # Constructor initializes all subsystems
    def __init__(self):
        self.light = Light()
        self.tv = TV()
        self.ac = AirConditioner()

    def movie_mode(self):
        print("\nActivating Movie Mode...")
        self.light.turn_off()
        self.tv.turn_on()
        self.ac.turn_on()

    def good_night_mode(self):
        print("\nActivating Good Night Mode...")
        self.light.turn_off()
        self.tv.turn_off()
        self.ac.turn_on()

    def morning_mode(self):
        print("\nActivating Morning Mode...")
        self.light.turn_on()
        self.tv.turn_on()
        self.ac.turn_off()


# Client Code
if __name__ == "__main__":
    home = HomeAutomationFacade()

    home.movie_mode()
    home.good_night_mode()
    home.morning_mode()
