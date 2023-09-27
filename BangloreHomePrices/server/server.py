from flask import Flask,request,jsonify
import util

app=Flask(__name__)

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response=jsonify({'locations':util.get_location_names()})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk']) #when we will making http call from html application ,we will get all inputs in request.form

    response=jsonify({'estimated_price':util.get_estimated_price(location,total_sqft,bath,bhk)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=='__main__':
    print('Starting python Flask server for Home price prediction...')
    util.load_saved_artifacts()
    app.run()