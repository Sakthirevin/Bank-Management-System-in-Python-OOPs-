# Abstract base class (ABC) - Define a class that can’t be instantiated directly - Blueprint for other classes /common interface that all subclasses 
from abc import ABC, abstractmethod #method without the definition
#abc-Libray or module--- ABC-class name

class Account(ABC): #class impote and inherits abstract class
  # @ - A decorator is a special type of function that modifies the behavior of another function or class without changing its source code. 
    
  #function that inharitate the abstract method  
    @abstractmethod 
    def create_account(self):
        pass

    @abstractmethod
    def display_balance(self):
        pass

# Main Customer class (Base Class)
class Customer(Account):  # Child Class
    def __init__(self, name, balance=0):# Encapsulation Method -Binding of variables and Methods
        self.__name = name          # Private variable
        self.__balance = balance    # Private variable

    def create_account(self): # Method Overriding with same function name
        print(f"Account created for {self.__name}")

    def deposit(self, amount): 
        self.__balance += amount
        print(f"₹{amount} deposited.")
                                             # Standard Operation
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print("Insufficient Balance")

    def display_balance(self): # Method Overriding with same function name
        print(f"Current Balance: ₹{self.__balance}")

#Getter Method - Use to print the function with the private variable is in outside the class
    def get_balance(self):  
        return self.__balance
    def get_name(self):
        return self.__name

#Setter Method - Use to modify the private Variable
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
            print(f"Balance updated to ₹{new_balance}")
        else:
            print("Invalid balance amount!")
    
    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
            print(f"Customer name updated to {new_name}")
        else:
            print("Invalid name!")

#Encapsulation
    def customer_info(self):
        print(f"Customer Name: {self.__name}")

# Derived class with method overriding (Polymorphism)
class CouponCustomer(Customer): # Inheritance
    def __init__(self, name, balance=0, coupon_amount=1000): # Parameterized Constructor (initialize or set up an object properties know as attributes )
        super().__init__(name, balance + coupon_amount) # Superclass gives you access to methods and properties of a parent class
# Method Overriding
    def display_balance(self): # Call the parent version
        print("Coupon Customer ", end="")
        super().display_balance() # Runtime Polymorphism (dynamic method dispatch)


# Function using *args and **kwargs accept variable-length arguments
def transaction_summary(*args, **kwargs):
    print("\nTransaction Summary:")
    for i, arg in enumerate(args): # Allows passing any number of positional arguments
        print(f"Operation {i+1}: {arg}")
    for key, value in kwargs.items(): # Allows passing any number of keyword arguments
        print(f"{key}: {value}")


# Lambda function - Anonymous (unnamed) function
calculate_gst = lambda amount: amount * 0.18  # expression that gets evaluated and returned

# Main
def main():
    cust1 = Customer("Sakthi")
    cust1.create_account()
    cust1.deposit(10000)
    cust1.withdraw(5000)
    cust1.display_balance()

# Using getter and setter
    print(f"Old Name: {cust1.get_name()}")
    cust1.set_name("Sakthi Revin")
    updated_name = cust1.get_name()
    print(f"New Name: {updated_name}")

    print(f"Old Balance: ₹{cust1.get_balance()}")
    cust1.set_balance(15000)
    print(f"Updated Balance: ₹{cust1.get_balance()}")


    print("\nGST on ₹1000:", calculate_gst(1000))  # Lambda function

    print("\n--- Coupon Customer ---")
    CC = CouponCustomer(updated_name)
    CC.create_account()
    CC.display_balance()

    # Return statement example
    total = cust1.get_balance() + CC.get_balance()
    print(f"\nTotal account balance : ₹{total}")

    # Transaction summary with *args and **kwargs
    transaction_summary("Deposit ₹10000", "Withdraw ₹5000", Bank="SBI Bank", Location="India")

# Run
if __name__ == "__main__":
    main()
