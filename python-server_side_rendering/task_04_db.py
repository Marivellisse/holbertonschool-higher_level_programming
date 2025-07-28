from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_json_data():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []

def load_csv_data():
    data = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except ValueError:
                    continue
                data.append(row)
    except Exception:
        pass
    return data

def load_sql_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
    except Exception:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products = []

    if source == 'json':
        products = load_json_data()
    elif source == 'csv':
        products = load_csv_data()
    elif source == 'sql':
        products = load_sql_data()
    else:
        error = "Wrong source"

    if not error and product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if int(p.get('id')) == product_id]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid product ID"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

