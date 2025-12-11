"""
Club Information page handler for Student Portal
This module supports the clubinfo.html functionality
"""

from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Club information database
CLUBS = [
    {
        "id": 1,
        "name": "Science Club",
        "description": "Explore the wonders of science through experiments and research.",
        "members": 45,
        "meeting_day": "Monday",
        "meeting_time": "3:00 PM",
        "advisor": "Dr. Smith"
    },
    {
        "id": 2,
        "name": "Debate Club",
        "description": "Develop public speaking skills and engage in friendly debates.",
        "members": 32,
        "meeting_day": "Wednesday",
        "meeting_time": "3:30 PM",
        "advisor": "Ms. Johnson"
    },
    {
        "id": 3,
        "name": "Tech Club",
        "description": "Learn programming, web development, and latest technologies.",
        "members": 58,
        "meeting_day": "Tuesday",
        "meeting_time": "4:00 PM",
        "advisor": "Mr. Chen"
    },
    {
        "id": 4,
        "name": "Sports Club",
        "description": "Stay active and build teamwork through various sports activities.",
        "members": 72,
        "meeting_day": "Thursday",
        "meeting_time": "3:45 PM",
        "advisor": "Coach Martinez"
    }
]

@app.route('/clubinfo.html')
@app.route('/clubs')
def club_info():
    """
    Render the club information page with all clubs
    """
    return render_template('clubinfo.html', clubs=CLUBS)

@app.route('/api/clubs')
def get_all_clubs():
    """
    API endpoint to get all clubs as JSON (for AJAX requests)
    """
    return jsonify(CLUBS)

@app.route('/api/clubs/<int:club_id>')
def get_club(club_id):
    """
    API endpoint to get a specific club by ID
    """
    club = next((club for club in CLUBS if club['id'] == club_id), None)
    if club:
        return jsonify(club)
    return jsonify({"error": "Club not found"}), 404

@app.route('/api/clubs/search/<query>')
def search_clubs(query):
    """
    API endpoint to search clubs by name or description
    """
    query = query.lower()
    results = [
        club for club in CLUBS 
        if query in club['name'].lower() or query in club['description'].lower()
    ]
    return jsonify(results)

def get_club_count():
    """
    Get the total number of clubs
    """
    return len(CLUBS)

def add_club(name, description, advisor, meeting_day, meeting_time):
    """
    Add a new club to the system
    """
    new_club = {
        "id": max((club['id'] for club in CLUBS), default=0) + 1,
        "name": name,
        "description": description,
        "members": 0,
        "meeting_day": meeting_day,
        "meeting_time": meeting_time,
        "advisor": advisor
    }
    CLUBS.append(new_club)
    return new_club

def remove_club(club_id):
    """
    Remove a club from the system by ID
    """
    global CLUBS
    CLUBS = [club for club in CLUBS if club['id'] != club_id]

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
