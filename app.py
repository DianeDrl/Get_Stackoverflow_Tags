# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
from stackoverflow_predict_tags import predict_tags

# Create Flask application
app = Flask(__name__)

# Route to fetch frontend
@app.route('/')
def index():
    return render_template('index.html')

# Run the application
if __name__ == "__main__":
    app.run(debug=True)




