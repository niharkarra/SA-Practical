from flask import Flask, render_template

app = Flask(__name__)

resume_data = {
    "name": "John Doe",
    "skills": ["Python", "Java", "JavaScript", "SQL"],
    "certifications": ["AWS Certified Developer", "Microsoft Certified Azure Developer"]
}

# Route to display skills in HTML
@app.route('/skills', methods=['GET'])
def display_skills():
    return render_template('skills.html', skills=resume_data["skills"])

# Route to display certifications in HTML
@app.route('/certifications', methods=['GET'])
def display_certifications():
    return render_template('certifications.html', certifications=resume_data["certifications"])

if __name__ == '__main__':
    app.run(debug=True)

