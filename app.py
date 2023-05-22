import os

from flask import Flask, render_template, request
from src.dall_e_model import DallEModel

app = Flask(__name__)
dell_model = DallEModel(os.getenv("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    keywords = request.form['keywords'].split(',')
    image = dell_model.generate_image(keywords)
    image.save('static/generated_image.jpg')
    return render_template('result.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)