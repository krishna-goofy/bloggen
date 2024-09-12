from flask import render_template, request, jsonify
from app import app
import google.generativeai as genai
import os

api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise ValueError("API key is not set in environment variables")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-blog', methods=['POST'])
def generate_blog():
    data = request.json
    topic = data.get('topic')
    style = data.get('style', 'formal')

    
    prompt = f"Write a {style} blog post about {topic}."
    response = model.generate_content(prompt)

    blog_content = response.text
    return jsonify({'blog_content': blog_content})
