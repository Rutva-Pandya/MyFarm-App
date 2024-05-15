from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import openai
import base64
import requests
from werkzeug.utils import secure_filename

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

UPLOAD_FOLDER = '/Users/rutva/Downloads/picsave'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the UPLOAD_FOLDER exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/soil_moisture')
def soil_moisture():
    # Mock data for the sake of example
    mock_data = [
        {'Date': '2023-04-01', 'SoilMoisture': 24.5},
        {'Date': '2023-04-02', 'SoilMoisture': 25.1},
        {'Date': '2023-04-03', 'SoilMoisture': 20.3},
        {'Date': '2023-04-04', 'SoilMoisture': 22.7},
        {'Date': '2023-04-05', 'SoilMoisture': 21.8},
    ]
    return jsonify(mock_data)


@app.route('/images')
def images():
    return render_template('field_view.html')

@app.route('/satellite')
def satellite_images():
    return render_template('images.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

def encode_image(image_path):
    """Encodes the image at 'image_path' to base64."""
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

@app.route('/picsave/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/ask_cropwizard', methods=['POST'])
def ask_cropwizard():
    message = []  # Initialize the messages array

    # Check for text input
    if 'text' in request.form:
        text_data = request.form['text']
        message.append({
            "role": "user",
            "content": text_data
        })

    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Construct the URL for the uploaded image
        image_url = f"http://{request.host_url}picsave/{filename}"

        message.append({
            "role": "user",
            "content": {
                "type": "image_url",
                "image_url": {
                    "url": image_url
                }
            }
        })

    # Check if there is at least one message to send
    if not message:
        return jsonify({'error': 'No input provided'}), 400

    # API request headers and data
    headers = {
        "Authorization": f"Bearer {openai.api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4-vision-preview",  # Replace with model of choise
        "messages": message,
        "temperature": 0.1,  # Adjust the temperature if needed
        "stream": False  # Set to True for streaming response
    }

    # Make the API request
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=data
    )

    # Process the API response
    if response.status_code == 200:
        response_data = response.json()
        return jsonify({'response': response_data['choices'][0]['message']['content']})
    else:
        return jsonify({'error': 'Failed to get response from the model', 'status_code': response.status_code}), 500

if __name__ == '__main__':
    app.run(debug=True)