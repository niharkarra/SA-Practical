from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

resume_data = {
    "name": "Nihar Karra",
    "skills": ["Python", "Java", "JavaScript", "SQL"],
    "certifications": ["AWS Certified Developer", "Microsoft Certified Azure Developer", "New Changes"]
}

@app.route('/')
def home():
    return f"Welcome to {resume_data['name']}'s Resume API!"

@app.route('/skills', methods=['GET'])
def display_skills():
    return jsonify(skills=resume_data["skills"])

@app.route('/certifications', methods=['GET'])
def display_certifications():
    return jsonify(certifications=resume_data["certifications"])

# Error handler for routes that are not found
@app.errorhandler(404)
def page_not_found(e):
    # Check the request content type to determine the response format
    if request.headers.get('Content-Type') == 'application/json':
        return jsonify(error="404 - Page not found"), 404
    else:
        return render_template('error.html', error_message="404 - Page not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
