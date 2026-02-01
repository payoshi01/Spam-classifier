from flask import Flask, render_template, request
from predict import predict_message

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    if request.method == 'POST':
        message = request.form['message']
        prediction = predict_message(message)
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
