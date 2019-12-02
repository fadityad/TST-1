import requests
from flask import Flask, jsonify

app = Flask(__name__)
#route untuk request
@app.route('/<asal>/<tujuan>')
def info_transport(asal, tujuan):
    #proses ubah format nama asal da tujuan agar dapat mengakses api map
    Asal = asal.replace(' ','+').replace(',','%2C')
    Tujuan = tujuan.replace(' ','+').replace(',','%2C')
    endpoint='https://www.mapquestapi.com/directions/v2/route?key=E9TT6Iq8q1SrxjXz3Tu9lqFW1RCBjP6V&from='+Asal+'&to='+Tujuan+'&outFormat=json&ambiguities=ignore&routeType=fastest&doReverseGeocode=false&enhancedNarrative=false&avoidTimedConditions=false'
    
    #proses request data dari api
    req = requests.get(endpoint)
    data = req.json()
    #proses pencarian jarak dari data yang diperoleh dalam km
    distance = data['route']['distance']
    #proses penghitungan harga dari jarak yang diperoleh
    if distance <= 1:
        hargaojol = 8000
        hargataxiol = 10000
        hargabluebird = 6500
    elif distance <= 2:
        hargaojol = 8000
        hargataxiol = 10000
        hargabluebird = ((distance - 1)*4100)+6500
    else :
        hargaojol = ((distance - 2)*1500)+8000
        hargataxiol = ((distance - 2)*3500)+10000
        hargabluebird = ((distance - 1)*4100)+6500
    
    data_final = {
        distance : 'jarak',
        hargaojol : 'harga_ojek_online' ,
        hargataxiol : 'harga_taxi_online' ,
        hargabluebird : 'harga_taxi_bluebird' 
    }
    return jsonify(data_final)

if __name__ == '__main__':
    app.run(threaded = True, debug = True, port = 5020)
