"""
Home page handler for Student Portal
This module supports the home.html functionality
"""

from flask import Flask, render_template, request
import os

app = Flask(__name__)

# School information
SCHOOL_INFO = {
    "name": "SEVENTEEN University",
    "description": "Welcome to SEVENTEEN University where you will be taught by top professors in special courses and designs that best suits your curriculum and interests.",
    "founded": 2010,
    "motto": "Excellence in Education, Innovation in Learning"
}

@app.route('/')
@app.route('/home.html')
def home():
    """
    Render the home page with school information
    """
    return render_template('home.html', school=SCHOOL_INFO)

@app.route('/get-school-info')
def get_school_info():
    """
    API endpoint to get school information (for AJAX requests if needed)
    """
    return SCHOOL_INFO

@app.route('/calculator.html')
def calculator():
    """
    Route to calculator page
    """
    return render_template('calculator.html')

@app.route('/clubinfo.html')
def club_info():
    """
    Route to club info page
    """
    return render_template('clubinfo.html')

def initialize_app():
    """
    Initialize the Flask application with necessary configurations
    """
    app.config['TEMPLATE_FOLDER'] = os.path.dirname(os.path.abspath(__file__))
    app.config['STATIC_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    return app

if __name__ == '__main__':
    app = initialize_app()
    app.run(debug=True, host='localhost', port=5000)
