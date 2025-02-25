'''
Defination:-The Chain of Responsibility pattern allows multiple objects to handle a request without knowing which one will process it. 
            The request passes through a chain of handlers until one handles it.
'''
class Handler:
    """Abstract handler class"""
    def __init__(self, successor=None):
        self.successor = successor  # The next handler in the chain

    def handle_request(self, level):
        if self.successor:
            self.successor.handle_request(level)


class LowLevelSupport(Handler):
    """Handles low-level issues"""
    def handle_request(self, level):
        if level == "low":
            print("LowLevelSupport: Handling low-level issue.")
        else:
            super().handle_request(level)


class MediumLevelSupport(Handler):
    """Handles medium-level issues"""
    def handle_request(self, level):
        if level == "medium":
            print("MediumLevelSupport: Handling medium-level issue.")
        else:
            super().handle_request(level)


class HighLevelSupport(Handler):
    """Handles high-level issues"""
    def handle_request(self, level):
        if level == "high":
            print("HighLevelSupport: Handling high-level issue.")
        else:
            print("No support available for this level.")


# Setting up the chain: Low -> Medium -> High
support_chain = LowLevelSupport(MediumLevelSupport(HighLevelSupport()))

# Client makes requests of different levels
support_chain.handle_request("low")      # Handled by LowLevelSupport
support_chain.handle_request("medium")   # Handled by MediumLevelSupport
support_chain.handle_request("high")     # Handled by HighLevelSupport
support_chain.handle_request("urgent")   # No support available
