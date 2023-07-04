from flask import Flask, render_template, request, redirect

app = Flask(__name__)

menu = []
orders = []

@app.route('/')
def hello():
    return 'Hello, Zesty Zomato!'

@app.route('/menu')
def show_menu():
    return render_template('menu.html', menu=menu)

@app.route('/add-dish', methods=['GET', 'POST'])
def add_dish():
    if request.method == 'POST':
        dish_id = request.form['dish_id']
        dish_name = request.form['dish_name']
        dish_price = float(request.form['dish_price'])
        
        new_dish = {
            'id': dish_id,
            'name': dish_name,
            'price': dish_price,
            'availability': True
        }
        
        menu.append(new_dish)
        
        return redirect('/menu')
    
    return render_template('add_dish.html')

@app.route('/remove-dish', methods=['GET', 'POST'])
def remove_dish():
    if request.method == 'POST':
        dish_id = request.form['dish_id']
        
        for dish in menu:
            if dish['id'] == dish_id:
                menu.remove(dish)
                return redirect('/menu')
        
        return 'Dish not found'
    
    return render_template('remove_dish.html')

@app.route('/update-availability', methods=['GET', 'POST'])
def update_availability():
    if request.method == 'POST':
        dish_id = request.form['dish_id']
        new_availability = request.form['availability']
        
        for dish in menu:
            if dish['id'] == dish_id:
                dish['availability'] = (new_availability.lower() == 'yes')
                return redirect('/menu')
        
        return 'Dish not found'
    
    return render_template('update_availability.html')

@app.route('/take-order', methods=['GET', 'POST'])
def take_order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        dish_ids = request.form['dish_ids'].split(',')
        
        available_dishes = []
        for dish_id in dish_ids:
            for dish in menu:
                if dish['id'] == dish_id and dish['availability']:
                    available_dishes.append(dish)
        
        if len(available_dishes) == len(dish_ids):
            order_id = len(orders) + 1
            order_status = 'received'
            
            order = {
                'id': order_id,
                'customer_name': customer_name,
                'dish_ids': dish_ids,
                'status': order_status
            }
            
            orders.append(order)
            
            return redirect('/menu')
        
        return 'Invalid dish ID or dish not available'
    
    return render_template('take_order.html')


@app.route('/update-order-status', methods=['POST'])
def update_order_status():
    order_id = int(request.form['order_id'])
    new_status = request.form['status']

    for order in orders:
        if order['id'] == order_id:
            order['status'] = new_status
            return redirect('/review-orders')
        
        return 'Order not found'
    
    return render_template('update_order_status.html')



@app.route('/review-orders')
def review_orders():
    return render_template('review_orders.html', orders=orders)

@app.route('/exit')
def exit_app():
    # Perform any necessary cleanup or closing operations
    return 'Application exited'

if __name__ == '__main__':
    app.run()
