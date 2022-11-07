import numpy as np
from flask import Flask ,request,jsonify,render_template
import pickle
#create an app object using the flask class
app = Flask(__name__)
# load the trained model
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    '''
    for rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]  #converts string from the boxes to float
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0],2)
    def output_from_val(output):
        if output == 0:
            return ("The person has no daibetes")
        else:
            return ("The person has diabetes")
    return render_template('index.html', prediction_text ='{}'.format(output_from_val(output=output)))

if __name__ == "__main__":
    app.run(debug=True)