menu ={
    "Pizza":50,
    "Pasta":50,
    "Burger":50,
    "Salad":50,
    "Coffee":50,
    "Tea":20,
}
print("Welcome to Python Restaurant ")
print("pizza: 50\nPasta: 50\nBurger: 50\nSalad: 50\nCoffee: 50\nTea: 20")
order_total = 0
item_1 = input("Enter the name of item you want to order =")
if  item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else :
    print(f"Orderd item {item_1} has been not avaialable yet" )
another_order = input("Do you want to add another item ? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of secod item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"orderd item {item_2} is not avaialable!")
print(f" The total amount of item to pay is {order_total}")
