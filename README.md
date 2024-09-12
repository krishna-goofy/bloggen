Blog Generator with Gemini API
Overview
This project is a Flask-based application that generates blog content using the Gemini API. It provides an endpoint to generate blog posts based on a specified topic and writing style.

Features
Generates blog content using the Gemini API.
Configurable writing style (e.g., formal, informal).
Easy to set up and run with a Python virtual environment.
Prerequisites
Python 3.x
Flask
google-generativeai library
Installation
Clone the Repository

sh
git clone [https://github.com/krishna-goofy/bloggen](https://github.com/krishna-goofy/bloggen)
cd blog-generator
Set Up a Virtual Environment

sh
python -m venv bloggen_env
source bloggen_env/bin/activate   # On Windows: bloggen_env\Scripts\activate
Install Dependencies

sh
pip install -r requirements.txt
Set Up Environment Variables

Set your Gemini API key as an environment variable. For example:

sh
export GEMINI_API_KEY=your-api-key-here   # On Windows: set GEMINI_API_KEY=your-api-key-here
Run the Application

sh
python run.py
Usage
Open your web browser and go to http://127.0.0.1:5000/.

To generate a blog post, send a POST request to /generate-blog with a JSON payload. Example:

json
{
  "topic": "The Benefits of Meditation",
  "style": "informal"
}
The response will contain the generated blog content.

Example
sh
curl -X POST http://127.0.0.1:5000/generate-blog \
     -H "Content-Type: application/json" \
     -d '{"topic": "The Future of AI", "style": "formal"}'
Contributing
Contributions are welcome! Please submit a pull request with any improvements or bug fixes.
