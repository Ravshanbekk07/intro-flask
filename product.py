from flask import Flask,request,jsonify
from db import DB

app = Flask(__name__)
db = DB()


@app.route('/products/')
def get_all_products():
    params  =  request.args
    name  = params.get('name')
    if name:
        return jsonify(db.get_product_by_name(name))
    
    # print(db.get_all_products())
    return jsonify(db.get_all_products())

@app.route('/products/<int:id>')
def get_id(id):
    return jsonify(db.get_product_by_id(id))

@app.route('/products/',methods = ['POST'])
def add_product():
    data = request.get_json()
    db.add_product(data['name'],data['price'])
    return jsonify({'message':'product added'})

@app.route('/products/<int:id>',methods = ['PUT'])
def update(id):
    data = request.get_json()
    db.update(id,data['name'],data['price'])
    return jsonify({'message':'product updated'})

@app.route('/products/<int:id>',methods = ['DELETE'])
def delete(id):
    data = request.get_json()
    db.delete(id)
    return jsonify({'message':'product deleted'})

if __name__ == "__main__":
    app.run(debug=True)
