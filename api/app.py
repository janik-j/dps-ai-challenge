from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.abspath(os.getcwd()), 'checkpoints', 'xgb_model.joblib')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    input_data = pd.DataFrame({
        'year': [data['year']],
        'month': [data['month']]
    })
    
    prediction = model.predict(input_data)[0]
    
    return jsonify({'prediction': float(prediction)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
