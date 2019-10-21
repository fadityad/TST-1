import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<asal>/<tujuan>')
def info_transport(asal, tujuan):
    #asal = input('Masukkan alamat asal :')
    #tujuan = input('Masukkan alamat tujuan :')
    Asal = asal.replace(' ','+').replace(',','%2C')
    Tujuan = tujuan.replace(' ','+').replace(',','%2C')
    endpoint='https://www.mapquestapi.com/directions/v2/route?key=E9TT6Iq8q1SrxjXz3Tu9lqFW1RCBjP6V&from='+Asal+'&to='+Tujuan+'&outFormat=json&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false'

    req = requests.get(endpoint)
    data = req.json()
    distance = data['route']['distance']
    if distance <= 1:
        hargaa = 8000
        hargab = 10000
        hargac = 6500
    elif distance <= 2:
        hargaa = 8000
        hargab = 10000
        hargac = ((distance - 1)*4100)+6500
    else :
        hargaa = ((distance - 2)*1500)+8000
        hargab = ((distance - 2)*3500)+10000
        hargac = ((distance - 1)*4100)+6500
    print('Hasil :')
    print('Jarak',distance,'Kilometer')
    print('Harga menggunakan ojek online :',hargaa,'Rupiah')
    print('Harga menggunakan taxi online :',hargab,'Rupiah')
    print('Harga menggunakan taxi bluebird :',hargac,'Rupiah')

    data_final = {
        'jarak' : distance,
        'mata_uang' : 'rupiah',
        'harga_ojek_online' : hargaa,
        'harga_taxi_online' : hargab,
        'harga_taxi_bluebird' : hargac
    }
    return jsonify(data_final)

if __name__ == '__main__':
    #app.run(ssl_context = ('cert.pem', 'key.pem'))
    app.run(debug = True)
