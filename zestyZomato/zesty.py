# Step 1: Menu Management
menu = {}

def add_item(dish_id, name, price, stock, availability):
    menu[dish_id] = {'name': name, 'price': price, 'stock': stock, 'availability': availability}

def remove_item(dish_id):
    if dish_id in menu:
        del menu[dish_id]
        print(f"Dish with ID {dish_id} has been removed from the menu.")
    else:
        print(f"Dish with ID {dish_id} is not in the menu.")

def update_stock(dish_id, stock):
    if dish_id in menu:
        menu[dish_id]['stock'] = stock
        print(f"Stock of dish with ID {dish_id} has been updated to {stock}.")
    else:
        print(f"Dish with ID {dish_id} is not in the menu.")

def update_availability(dish_id, availability):
    if dish_id in menu:
        menu[dish_id]['availability'] = availability
        print(f"Availability of dish with ID {dish_id} has been updated to {availability}.")
    else:
        print(f"Dish with ID {dish_id} is not in the menu.")

def display_menu():
    print("Menu:")
    for dish_id, dish_info in menu.items():
        print(f"ID: {dish_id}, Name: {dish_info['name']}, Price: ${dish_info['price']}, "
              f"Availability: {dish_info['availability']}, Stock: {dish_info['stock']}")


# Task 2: Order Tracking
orders = []
order_id_counter = 1

def add_order(customer_name, dish_ids):
    global order_id_counter  # Declare order_id_counter as a global variable
    items = []
    for dish_id in dish_ids:
        if dish_id in menu and menu[dish_id]['availability'] == 'yes':
            items.append(menu[dish_id]['name'])
            menu[dish_id]['stock'] -= 1
        else:
            print(f"Dish with ID {dish_id} is not available.")
            return

    order = {'order_id': order_id_counter, 'customer_name': customer_name, 'items': items, 'status': 'received'}
    orders.append(order)
    print(f"Order {order_id_counter} received for customer '{customer_name}'.")
    order_id_counter += 1

def update_order_status(order_id, status):
    for order in orders:
        if order['order_id'] == order_id:
            order['status'] = status
            print(f"Order {order_id} status updated to '{status}'.")
            break
    else:
        print(f"Order with ID {order_id} not found.")

def display_orders():
    print("Orders:")
    for order in orders:
        print(order)


# Task 7: Exit option
def exit_system():
    print("Exiting the system.")


# Developer adds menu items
add_item(1, 'Pizza', 10, 10, 'yes')
add_item(2, 'Burger', 5, 5, 'yes')
add_item(3, 'Pasta', 8, 7, 'yes')
add_item(4, 'Salad', 6, 3, 'yes')


# User Interface
while True:
    print("\n===== Zesty Zomato Menu Management =====")
    print("1. Display Menu")
    print("2. Add Item to Menu")
    print("3. Remove Item from Menu")
    print("4. Update Stock")
    print("5. Update Availability")
    print("6. Take New Order")
    print("7. Update Order Status")
    print("8. Review Orders")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        display_menu()
    elif choice == '2':
        dish_id = int(input("Enter the dish ID: "))
        name = input("Enter the dish name: ")
        price = float(input("Enter the price: "))
        stock = int(input("Enter the stock: "))
        availability = input("Enter the availability (yes/no): ")
        add_item(dish_id, name, price, stock, availability)
    elif choice == '3':
        dish_id = int(input("Enter the dish ID to remove: "))
        remove_item(dish_id)
    elif choice == '4':
        dish_id = int(input("Enter the dish ID to update stock: "))
        stock = int(input("Enter the new stock: "))
        update_stock(dish_id, stock)
    elif choice == '5':
        dish_id = int(input("Enter the dish ID to update availability: "))
        availability = input("Enter the new availability (yes/no): ")
        update_availability(dish_id, availability)
    elif choice == '6':
        customer_name = input("Enter the customer's name: ")
        dish_ids = input("Enter the dish IDs (separated by commas): ").split(",")
        dish_ids = [int(dish_id.strip()) for dish_id in dish_ids if dish_id.strip()]
        add_order(customer_name, dish_ids)
    elif choice == '7':
        order_id = int(input("Enter the order ID to update status: "))
        status = input("Enter the new status: ")
        update_order_status(order_id, status)
    elif choice == '8':
        display_orders()
    elif choice == '9':
        exit_system()
        break
    else:
        print("Invalid choice. Please try again.")
