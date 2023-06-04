from flask import Flask, render_template, jsonify
from wsgiref.simple_server import make_server, WSGIServer

application = Flask(__name__)

resume_data = {
    "name": "Nihar Karra",
    "skills": ["Python", "Java", "JavaScript", "SQL"],
    "certifications": ["AWS Certified Developer", "Microsoft Certified Azure Developer", "New Changes"]
}

@application.route('/')
def home():
    return f"Welcome to {resume_data['name']}'s Resume API!"

@application.route('/skills', methods=['GET'])
def display_skills():
    return render_template('skills.html', skills=resume_data["skills"])

@application.route('/certifications', methods=['GET'])
def display_certifications():
    return render_template('certifications.html', certifications=resume_data["certifications"])

# Error handler for routes that are not found
@application.errorhandler(404)
def page_not_found(e):
    # Check the request content type to determine the response format
    if request.headers.get('Content-Type') == 'application/json':
        return jsonify(error="404 - Page not found"), 404
    else:
        return render_template('error.html', error_message="404 - Page not found"), 404

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    application.run(debug=True)
    application.debug = True
