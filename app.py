from flask import Flask, render_template
import json

app = Flask(__name__)

with open('config.json') as config_file:
    config_data = json.load(config_file)

resume_data = config_data.get("resume_data", {})
contact_data = config_data.get("contact", {})

@app.route('/')
def home():
    return render_template('home.html', name=resume_data.get("name", ""), about=resume_data.get("about", ""), skills=resume_data.get("skills", []), certifications=resume_data.get("certifications", []), education_data=resume_data.get("education", []))

@app.route('/skills', methods=['GET'])
def display_skills():
    return render_template('skills.html', skills=resume_data.get("skills", []))

@app.route('/certifications', methods=['GET'])
def display_certifications():
    return render_template('certifications.html', certifications=resume_data.get("certifications", []))

@app.route('/education', methods=['GET'])
def display_education():
    return render_template('education.html', education=resume_data.get("education", []))

# Error handler for routes that are not found
@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page not found, Please use the routes only that are available - Nihar", 404

if __name__ == '__main__':
   # The below 1 line is for running this app locally in docker. This line doesn't matter while running in beanstalk as beanstalk serves python app on 5000 port.
   app.run(host='0.0.0.0', port=80)
   app.run
