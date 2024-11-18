# Vidal Bustamante
# UWYO COSC 1010
# 11/17/2024
# Lab 09
# Lab Section: 13
# Sources, people worked with, help given to: NA


class Pizza:
    SIZE_OPTIONS = {10: "Small", 13: "Medium", 15: "Large", 18: "Extra Large", 20: "Shaq Size"}
    SAUCE_OPTIONS = ["Red", "Pesto", "Alfredo", "Garlic & Oil", "Romesco", "Buffalo", "Barbecue", "Spicy Red"]
    TOPPING_OPTIONS = ["Pepperoni", "Sausage", "Black Olives", "Spinach", "Mushrooms", "Bacon", "Onions", "Bell Pepper", "Extra Cheese", "Pineapple", "Ham"]

    def __init__(self, size, sauce):
        self.setSize(size)
        self.sauce = sauce if sauce else "Red"
        self.toppings = ["Cheese"]

    def setSize(self, size):
        if size < 10:
            self.size = 10
        else:
            self.size = min([s for s in self.SIZE_OPTIONS.keys() if s >= size], default=10)

    def setToppings(self, toppings):
        self.toppings.extend(toppings)

    def getSize(self):
        return self.size

    def getSauce(self):
        return self.sauce

    def getToppings(self):
        return self.toppings

    def getAmountOfToppings(self):
        return len(self.toppings)

class Pizzeria:
    price_per_topping = 0.30
    price_per_inch = 0.60

    def __init__(self):
        self.orders = 0
        self.pizzas = []

    def placeOrder(self):
        self.orders += 1
        try:
           size = int(input("Please enter the size of pizza, as a whole number.\nWe have: 10 for Small, 13 for Medium, 15 for large, 18 for XLarge, and 20 for Shaq Size.\nLeave blank for 10.\n"))
        except:
            size = 10

        sauce = input("What kind of sauce would you like?\nWe have Red, Pesto, Alfredo, Garlic & Oil, Romesco, Buffalo, Barbecue, Spicy Red\nLeave blank for Red Sauce\n").strip()
        toppings_input = input("Please enter the toppings you would like.\nWe have Pepperoni, Sausage, Black Olives, Spinach, Mushrooms, Bacon, Onions, Bell Pepper, Extra Cheese, Pineapple, and Ham.\nPress \"Enter\" when done.\n").strip()

        toppings = toppings_input.split() if toppings_input else []

        pizza = Pizza(size, sauce)
        pizza.setToppings(toppings)

        self.pizzas.append(pizza)

        self.getReceipt(pizza)

    def getPrice(self, pizza):
        size_price = pizza.getSize() * self.price_per_inch
        topping_price = pizza.getAmountOfToppings() * self.price_per_topping
        return size_price + topping_price

    def getReceipt(self, pizza):
        price = self.getPrice(pizza)
        print(f"\nYou ordered a {pizza.getSize()}\" pizza with {pizza.getSauce()} Sauce and the following toppings:")
        for topping in pizza.getToppings():
            print(f"   {topping}")
        print(f"You ordered a {pizza.getSize()}\" pizza for ${pizza.getSize() * self.price_per_inch:.2f}")
        print(f"You had {pizza.getAmountOfToppings()} topping(s) for ${pizza.getAmountOfToppings() * self.price_per_topping:.2f}")
        print(f"Your total price is ${price:.2f}\n")

    def getNumberOfOrders(self):
        return self.orders

def main():
    pizzeria = Pizzeria()

    while True:
        order_input = input("Would you like to place an order? Type \"yes\" to place order; \"exit\" to exit.\n").strip().lower()
        if order_input == "exit":
            break
        elif order_input == "yes":
            pizzeria.placeOrder()
        else:
            print("Invalid option. Please type \"yes\" to order or \"exit\" to quit.")

    print(f"\nTotal orders placed: {pizzeria.getNumberOfOrders()}")

if __name__ == "__main__":
    main()
