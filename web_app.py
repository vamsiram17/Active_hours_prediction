import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('sleep_model', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getprediction',methods=['POST'])
def getprediction():    
    input = [request.form.get("hours")]
    final_input = [np.array(input)]
    prediction = model.predict(final_input)

    return render_template('success.html',output='You can actively work for {} hours'.format(prediction),output_1="Hello {}".format(request.form.get('Name')))

if __name__ == "__main__":
    app.run(debug=True)

