from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

data = {}


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data[key] = value
        return "Entry created successfully!"
    return render_template('create.html')

@app.route('/read')
def read():
    return render_template('read.html', data=data)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            value = request.form['value']
            data[key] = value
            return "Entry updated successfully!"
        else:
            return "Entry not found!"
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return "Entry deleted successfully!"
        else:
            return "Entry not found!"
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(port=8080)
