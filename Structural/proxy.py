from abc import ABC, abstractmethod
# Subject Interface
class Internet(ABC):
    @abstractmethod # Abstract Method to be implemented by RealSubject and Proxy classes
    def connect_to(self, website):
        pass

# Real Subject (Actual Internet Connection)
class RealInternet(Internet):
    def connect_to(self, website):
        print(f"Connecting to {website}")

# Proxy Internet with restricted access
class ProxyInternet(Internet):
    restricted_sites = ["facebook.com", "youtube.com", "instagram.com"]
    def __init__(self):
        self.real_internet = RealInternet()  # Using the real object inside proxy

    def connect_to(self, website):
        if website in self.restricted_sites:
            print(f"Access Denied: {website} is blocked!")
        else:
            self.real_internet.connect_to(website)

# Client Code
internet = ProxyInternet()
internet.connect_to("google.com")  # ✅ Allowed
internet.connect_to("facebook.com")  # ❌ Blocked
internet.connect_to("wikipedia.org")  # ✅ Allowed
