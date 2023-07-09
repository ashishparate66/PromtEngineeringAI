from flask import Flask, render_template, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import json
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb+srv://root:Root@cluster0.9gabzyg.mongodb.net/?retryWrites=true&w=majority')

db = client['zesty_zomato']

# Initialize the orders list
menu_collection = db['menu']
orders_collection = db['orders']

# Route to display the menu
@app.route('/menu')
def display_menu():
    menu_data = list(menu_collection.find())
    menu_data = json.loads(json.dumps(menu_data, default=str))
    return menu_data
    
# Route to add a new dish to the menu
@app.route('/add_dish', methods=['POST'])
def add_dish():
    data = request.get_json()
    menu_collection.insert_one(data)
    return "Item created successfully!"
    



# Route to remove a dish from the menu
@app.route('/remove_dish/<item_id>', methods=['DELETE'])
def remove_dish(item_id):
    id = item_id
    menu_collection.delete_one({"_id": ObjectId(id)})
    return "Item deleted successfully!"



# Route to update the availability of a dish
@app.route('/update_availability/<item_id>', methods=['PATCH'])
def update_availability(item_id):
    id = item_id
    data = request.get_json()
    new_availability = data["availability"]
    menu_collection.update_one({"_id": ObjectId(id)}, {"$set": {"availability": new_availability}})
    return "Item updated successfully!"
     

# Route to take a new order
@app.route('/new_order', methods=['POST'])
def new_order():
    data=request.get_json()
    customer_name = data["customer_name"]
    dish_ids = data['dish_ids']
    
    order = {
        "customer_name": customer_name,
        "dish_ids": dish_ids,
        "status": "received"
    }
    
    for dish_id in dish_ids:
        dish = menu_collection.find_one({"_id": ObjectId(dish_id)})
        if not dish or not dish['availability']:
            return "Error: Invalid dish ID or dish not available"   
    
    orders_collection.insert_one(order)
    
    return "Order placed successfully"



# Route to update the status of an order
@app.route('/update_order_status/<order_id>', methods=['PATCH'])
def update_order_status(order_id):
    order_id = order_id
    data = request.get_json()
    new_status = data['status']

    orders_collection.update_one({"_id": ObjectId(order_id)}, {"$set": {"status": new_status}})
    
    return "Order updated successfully!"

# Route to display all orders
@app.route('/orders')
def display_orders():
    orders_data = list(orders_collection.find())
    orders_data = json.loads(json.dumps(orders_data, default=str))
    return orders_data


# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)