from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    num1 = request.args.get('num1', default=0, type=float)
    num2 = request.args.get('num2', default=0, type=float)
    
    prediction = 1 if (num1 + num2) > 5.8 else 0

    returned_dict = {
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    }
    return jsonify(returned_dict)

if __name__ == '__main__':
    app.run()