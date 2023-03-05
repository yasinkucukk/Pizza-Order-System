import csv
import datetime
import os

# create a superclass for the pizza
class Pizza(object):
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def get_description(self):
        return self.name + " pizza (" + ", ".join(self.ingredients) + ")"
    def get_cost(self):
        return self.price
    
""" lambda function version 
get_description = lambda self: self.name + " pizza (" + ", ".join(self.ingredients) + ")"
get_cost = lambda self: self.cost
"""

# create subclasses for the pizza types
class ClassicPizza(Pizza):
    def __init__(self, name, cost, ingredients):
        super(ClassicPizza, self).__init__(name, cost, ingredients)
        self.cost = self.price

class MargheritaPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super(MargheritaPizza, self).__init__(name, price, ingredients)
        self.cost = self.price

class TurkPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super(TurkPizza, self).__init__(name, price, ingredients)
        self.cost = self.price

class ItalianoPizza(Pizza):
    def __init__(self, name, price, ingredients):
        super(ItalianoPizza, self).__init__(name, price, ingredients)
        self.cost = self.price

# create a superclass for the pizza toppings
class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

# create subclasses for the pizza toppings    
class Olives(Decorator):
    def __init__(self, pizza):
        super(Olives, self).__init__(pizza)
        self.cost = 0.5

    def get_description(self):
        return ", with Olives"
    
    def get_cost(self):
        return self.cost
    
class Mushrooms(Decorator):
    def __init__(self, pizza):
        super(Mushrooms, self).__init__(pizza)
        self.cost = 0.75

    def get_description(self):
        return ", with Mushrooms"
    
    def get_cost(self):
        return self.cost

class GoatCheese(Decorator):
    def __init__(self, pizza):
        super(GoatCheese, self).__init__(pizza)
        self.cost = 1.5

    def get_description(self):
        return ", with Goat Cheese"
    
    def get_cost(self):
        return self.cost
    
class Pepperoni(Decorator):
    def __init__(self, pizza):
        super(Pepperoni, self).__init__(pizza)
        self.cost = 1.25

    def get_description(self):
        return ", with Pepperoni"
    
    def get_cost(self):
        return self.cost
    
class Onions(Decorator):
    def __init__(self, pizza):
        super(Onions, self).__init__(pizza)
        self.cost = 0.5

    def get_description(self):
        return ", with Onions"
    
    def get_cost(self):
        return self.cost

class Corn(Decorator):
    def __init__(self, pizza):
        super(Corn, self).__init__(pizza)
        self.cost = 0.5

    def get_description(self):
        return ", with Corn"
    
    def get_cost(self):
        return self.cost

# create a main function
def main():
    
    # print the menu
    f = open('Menu.txt', 'r')
    print(f.read())
    f.close()

    # create a list of pizza types
    pizza_types = {1: ClassicPizza("Classic", 8.0, ["Tomato Sauce", "Mozzarella", "Sausage", "Basil"]),
                   2: MargheritaPizza("Margherita", 7.0, ["Tomato Sauce", "Mozzarella", "Basil"]),
                   3: TurkPizza("Turkish", 16.0, ["Tomato Sauce", "Mozzarella", "Beefsteak", "Bacon", "Ham", "Sausage", "Pepper", "Oregano", "Basil"]),
                   4: ItalianoPizza("Italiano", 10.0, ["Tomato Sauce", "Mozzarella", "Sausage", "Pepper", "Oregano", "Basil"])}
    # create a list of pizza toppings
    pizza_toppings = {11: Olives,
                    12: Mushrooms,
                    13: GoatCheese,
                    14: Pepperoni,
                    15: Onions,
                    16: Corn}

    # prompt the user to enter the pizza type number
    user_pizza_type = int(input("Enter the pizza type number: "))
    # prompt the user to enter the pizza sauce number
    user_pizza_topping = int(input("Enter the pizza topping number: "))

    # calculate the total cost of the pizza
    total_cost = pizza_toppings[user_pizza_topping](pizza_types[user_pizza_type]).get_cost() + pizza_types[user_pizza_type].get_cost()
    # show the pizza description
    pizza_description = pizza_types[user_pizza_type].get_description() + pizza_toppings[user_pizza_topping](pizza_types[user_pizza_type]).get_description()

    # print the total cost and the pizza description
    print(f"\nTotal Cost: {total_cost}$")
    print("Pizza Description: " + pizza_description)
    
    # prompt the user to enter the name, ID number, credit card number, and password
    user_name = input("\nEnter your name: ")
    user_id = input("Enter your ID number: ")
    user_credit_card = input("Enter your credit card number: ")
    user_password = input("Enter your password: ")

    # create a list of the order and time
    order = [user_name, user_id, user_credit_card, user_password, pizza_description, total_cost, datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")]
    
   
    # keep the order history in a csv file dictionary format

    # open the file
    with open('Orders_Database.csv', 'a') as csv_file:
        # create a csv writer object
        headers = ['Name', 'ID', 'Credit Card', 'Password', 'Pizza Description', 'Total Cost', 'Time']
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers, delimiter=',', lineterminator='\n')
        # write headers if the file is empty
        if os.stat('Orders_Database.csv').st_size == 0:
            csv_writer.writeheader()
        # write the order to the csv file
        csv_writer.writerow({'Name': order[0], 'ID': order[1], 'Credit Card': order[2], 'Password': order[3], 'Pizza Description': order[4], 'Total Cost': order[5], 'Time': order[6]})
    
    # close the file
    f.close()


# call the main function
main()
   
