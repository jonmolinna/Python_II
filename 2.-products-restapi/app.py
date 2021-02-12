from flask import Flask, jsonify
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message" : "pong"})

@app.route('/products')
def getProducts():
    return jsonify({"products" : products, "message" : "Product's List"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name] # primer product obtiene una lista de producto
    return jsonify({'product' : productsFound[0]})

if __name__ == '__main__':
    app.run(debug=True, port=4000)



# 18 : 52