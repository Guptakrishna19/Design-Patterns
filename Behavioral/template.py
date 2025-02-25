"""
Defination:-The Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a base class 
but lets subclasses override specific steps without changing the algorithm's structure.
"""

from abc import ABC, abstractmethod


# Step 1: Define an Abstract Class with the Template Method
class OnlineOrder(ABC):
    """Abstract class defining the template method"""

    def process_order(self):
        """Template method defining the steps of order processing"""
        self.select_items()
        self.make_payment()
        self.deliver_order()
        print("Order processing completed \n")

    @abstractmethod
    def select_items(self):
        """Step 1: Selecting items (Implemented in subclass)"""
        pass

    @abstractmethod
    def make_payment(self):
        """Step 2: Making payment (Implemented in subclass)"""
        pass

    def deliver_order(self):
        """Step 3: Delivery (Common step for all orders)"""
        print("Delivering order")


# Step 2: Concrete Implementations of the Template
class CreditCardOrder(OnlineOrder):
    def select_items(self):
        print("Selected items for Credit Card order ")

    def make_payment(self):
        print("Payment done using Credit Card ")


class PayPalOrder(OnlineOrder):
    def select_items(self):
        print("Selected items for PayPal order")

    def make_payment(self):
        print("Payment done using PayPal")


# Step 3: Using the Template
if __name__ == "__main__":
    print("Processing Credit Card Order:")
    order1 = CreditCardOrder()
    order1.process_order()

    print("Processing PayPal Order:")
    order2 = PayPalOrder()
    order2.process_order()
