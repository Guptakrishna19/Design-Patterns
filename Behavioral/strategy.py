''' 
definitation :-The Strategy Pattern allows selecting a behavior (algorithm) at runtime.
It is useful when we have multiple ways of performing an operation, 
and we want to choose a strategy dynamically without modifying the existing code.

'''
from abc import ABC, abstractmethod

# Step 1: Define a Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Step 2: Implement Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card 💳"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal 🏦"

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin ₿"

# Step 3: Context Class (Uses a Payment Strategy)
class ShoppingCart:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy  # Set the payment strategy

    def checkout(self, amount):
        return self.strategy.pay(amount)  # Execute strategy

# Example Usage
if __name__ == "__main__":
    # Choose a payment method dynamically
    cart1 = ShoppingCart(CreditCardPayment())
    print(cart1.checkout(100))  # Output: Paid $100 using Credit Card 💳

    cart2 = ShoppingCart(PayPalPayment())
    print(cart2.checkout(200))  # Output: Paid $200 using PayPal 🏦

    cart3 = ShoppingCart(BitcoinPayment())
    print(cart3.checkout(300))  # Output: Paid $300 using Bitcoin ₿
