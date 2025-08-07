from flask import Flask, render_template, request, jsonify
from gpt_api import GeminiAPI
import os

app = Flask(__name__)

# Initialize Gemini API
gemini_api = GeminiAPI(api_key="AIzaSyBxQxzXCDT4xFLq0o8Fcxt45SniZUjnAao")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Get response from Gemini
        response = gemini_api.get_response(user_message)
        
        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
