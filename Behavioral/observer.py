# Step 1: Define Observer Interface
class Observer:
    def update(self, message):
        pass

# Step 2: Concrete Observer Classes
class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received update: {message}")

# Step 3: Subject (Observable)
class NewsAgency:
    def __init__(self):
        self._observers = []
        self._latest_news = None

    def attach(self, observer):
        """Attach an observer (subscriber)"""
        self._observers.append(observer)

    def detach(self, observer):
        """Detach an observer (unsubscribe)"""
        self._observers.remove(observer)

    def notify(self):
        """Notify all observers (publish update)"""
        for observer in self._observers:
            observer.update(self._latest_news)

    def add_news(self, news):
        """Update state and notify observers"""
        self._latest_news = news
        self.notify()

# Step 4: Client Code
if __name__ == "__main__":
    # Create a News Agency (Subject)
    agency = NewsAgency()

    # Create Observers (Subscribers)
    user1 = User("Alice")
    user2 = User("Bob")

    # Attach Observers to Subject
    agency.attach(user1)
    agency.attach(user2)

    # Publish News
    agency.add_news("Breaking News: Observer Pattern Implemented in Python!")

    # Detach one observer and publish another news
    agency.detach(user1)
    agency.add_news("Latest Update: Python is awesome!")
