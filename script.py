from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from ZSIC import ZeroShotImageClassification
import os
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to my application!", 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        zsic = ZeroShotImageClassification()
        image_url = request.form.get('image_url')
        if not image_url:
            return jsonify({'error': 'No image URL provided'}), 400
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        candidate_labels = request.form.get('candidate_labels', '').split(',')
        preds = zsic(image=image, candidate_labels=candidate_labels)
        # Ensure the preds dictionary is JSON-serializable
        preds = {k: str(v) for k, v in preds.items()}
        response = jsonify(preds)
        print(response.get_data(as_text=True))
        return response
    except Exception as e:
        app.logger.error(f"Exception occurred: {type(e).__name__}, {str(e)}")
        return "Doesn't work", 500

if __name__ == '__main__':
    app.run(debug=True)