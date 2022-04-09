from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('boston_model', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        lstat = float(request.form['lstat'])
        rm=float(request.form['rm'])
        ptratio=float(request.form['ptratio'])
                
        prediction=model.predict([[lstat, rm, ptratio]])       
                
        return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(prediction))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)