from flask import Flask, render_template, request, redirect
from db import menu_collection
from bson.objectid import ObjectId

app = Flask(__name__)


@app.route('/')
def index():
    items = list(menu_collection.find())
    return render_template('index.html', items=items)



@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        menu_collection.insert_one({
            "name": request.form['name'],
            "price": float(request.form['price']),
            "category": request.form['category']
        })
        return redirect('/')
    return render_template('add.html')



@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    item = menu_collection.find_one({"_id": ObjectId(id)})

    if request.method == 'POST':
        menu_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "name": request.form['name'],
                "price": float(request.form['price']),
                "category": request.form['category']
            }}
        )
        return redirect('/')

    return render_template('edit.html', item=item)



@app.route('/delete/<id>')
def delete(id):
    menu_collection.delete_one({"_id": ObjectId(id)})
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)