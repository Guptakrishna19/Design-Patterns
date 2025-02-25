# Step 1: Define the Mediator Interface
class Mediator:
    def notify(self, sender, event):
        pass

# Step 2: Concrete Mediator
class ChatRoom(Mediator):
    def __init__(self):
        self.participants = {}

    def register(self, user):
        """Registers a user to the chatroom"""
        self.participants[user.name] = user
        user.mediator = self

    def notify(self, sender, message):
        """Send a message to all users except the sender"""
        for user in self.participants.values():
            if user.name != sender:
                user.receive(message)

# Step 3: Define the Colleague (Participant) Class
class User:
    def __init__(self, name):
        self.name = name
        self.mediator = None  # Will be set when registering to ChatRoom

    def send(self, message):
        
        
        """Send message through mediator"""
        print(f"{self.name} sends: {message}")
        self.mediator.notify(self.name, message)

    def receive(self, message):
        """Receive message"""
        print(f"{self.name} receives: {message}")

# Step 4: Client Code
if __name__ == "__main__":
    chatroom = ChatRoom()

    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Register users to the chatroom
    chatroom.register(alice)
    chatroom.register(bob)
    chatroom.register(charlie)

    # Users sending messages
    alice.send("Hello, everyone!")
    bob.send("Hey Alice!")
    charlie.send("Hi Alice and Bob!")
