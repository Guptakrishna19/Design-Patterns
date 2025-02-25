# Step 1: Define the Command Interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass

# Step 2: Receiver (The actual action taker)
class Light:
    def turn_on(self):
        print("The light is ON")

    def turn_off(self):
        print("The light is OFF")

# Step 3: Concrete Command Classes
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Step 4: Invoker (Requests the execution)
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()

# Step 5: Client Code
if __name__ == "__main__":
    light = Light()  # Receiver
    light_on = LightOnCommand(light)  # Concrete Command
    light_off = LightOffCommand(light)

    remote = RemoteControl()  # Invoker

    print("Turning on the light:")
    remote.set_command(light_on)
    remote.press_button()

    print("\nUndoing the action:")
    remote.press_undo()

    print("\nTurning off the light:")
    remote.set_command(light_off)
    remote.press_button()

    print("\nUndoing the action:")
    remote.press_undo()
