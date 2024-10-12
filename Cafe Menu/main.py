# Create Cafe menu
menu = {
    "chai" : 10,
    "coffee" : 20,
    "cold coffee" : 50,
    "vadapav" : 25,
    "puff" : 30,
    "pizza" : 60,
    "burger" : 50
}
total_price = 0

# Greet Message
print("Welcome to DR Cafe")
print("The menu:\nChai : 10\nCoffee : 20\nCold Coffee : 50\nVadaPav : 25\nPuff : 30\nPizza : 60\nBurger : 50")

# Ask user for order
order = input("What would you like to order? ").lower()
if order in menu:
    total_price += menu[order]
    print(f"Your item {order} has been added to your order")
else:
        print(f"Ordered item {order} is not available yet!")

# Ask for another order
while True:
    order_2 = input("Do you want to add another item? (Yes/No)")
    if order_2.lower() == "yes":
        item_2 = input("Enter the name of second item: ").lower()
        if item_2 in menu:
            total_price += menu[item_2]
            print(f"Your item {item_2} has been added to your order")
        else:
            print(f"Ordered item {item_2} is not available yet!")
    else:
        break

# Print total price of order
print(f"The total amount of your order is {total_price}.") 