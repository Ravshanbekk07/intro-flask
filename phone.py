from flask import Flask, request
from tinydb import TinyDB, Query

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


@app.route('/phones')
def get_phones():
    params = request.args
    brend_name = params.get('brend', None)
    if brend != None:
        q = Query()
        return {
            'phones': phones.search(q.brend == brend_name)
        }
    return {
        'phones': phones.all()
    }


if __name__ == '__main__':
    app.run(debug=True)

