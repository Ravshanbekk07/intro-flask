from tinydb import TinyDB, Query
from flask import Flask, request,jsonify

app = Flask(__name__)

db = TinyDB('db.json')
phones = db.table('phones')

@app.route('/brends')
def brend():
    if request.method == 'GET':
        brends = []
        for phone in phones.all():
            if phone['brend'] not in brends:
                brends.append(phone['brend'])
        return {
            'brends': brends
        }


@app.route('/phones/<brand>',methods=['GET','POST'])
def get_phones(brand: str):
    
    if brand != None:
        q = Query()
        return {
            'phones': phones.search(q.brend == brand.capitalize())
        }
    return {
        'phones': phones.all()
    }



@app.route('/ram')
def ram():
    params = request.args
    brend_ram = params.get('ram')
    
    q = Query()
    return {
            'phones': phones.search(q.ram == int(brend_ram))
        }

@app.route('/memory')
def memory():
    params = request.args
    memory_phones = params.get('memory')
    
    q = Query()
    return {
            'phones': phones.search(q.memory == int(memory_phones))
        }


@app.route('/price')
def get_phones_price():
    params = request.args
    min = params.get('min',None)
    max = params.get('max',None)
  
    
    q= Query()
    return {
            'phones':phones.search((q.price>=float(min))&(q.price<=float(max)))}



@app.route('/greetings/',methods = ['GET','POST'])
def greetings():
    if request.method == 'POST':
        data =  request.get_json()
        return jsonify ({'message':'salom '+ data['name'].capitalize()})



if __name__ == '__main__':
    app.run(debug=True)

