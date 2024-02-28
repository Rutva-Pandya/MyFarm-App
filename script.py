from flask import Flask, request, jsonify, render_template
import os
import openai

app = Flask(__name__)

# Make sure to set the OPENAI_API_KEY environment variable in your actual deployment
openai.api_key = os.getenv('OPENAI_API_KEY')  # Replace with the name of your environment variable

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/soil_moisture')
def soil_moisture():
    # Placeholder for fetching and returning soil moisture data
    return render_template('soil_moisture.html')

@app.route('/images')
def images():
    # Placeholder for fetching and returning images
   return render_template('field_view.html')
   

@app.route('/satellite')
def satellite_images():
    # Placeholder for fetching and returning satellite images
    return render_template('images.html')

@app.route('/chat')
def chat():
    # Serve the chat interface page
    return render_template('chat.html')

@app.route('/ask_cropwizard', methods=['POST'])
def ask_cropwizard():
    data = request.get_json()
    question = data['question']
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Specify the model here
        prompt=question,
        max_tokens=150
    )
    return jsonify({'response': response.choices[0].text})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, port=5001)  # You can change the port number if needed
