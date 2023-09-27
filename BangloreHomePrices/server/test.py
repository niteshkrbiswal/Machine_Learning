from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route('/hello')
def hello():
    return "Hi"

if __name__=='__main__':
    print('Starting python Flask server for Home price prediction')
    app.run()