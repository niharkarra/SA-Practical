from flask import Flask, render_template

app = Flask(__name__)

resume_data = {
    "name": "Nihar Karra",
    "skills": ["Python", "Java", "JavaScript", "SQL"],
    "certifications": ["AWS Certified Developer", "Microsoft Certified Azure Developer", "New Changes"],
    "about": "As a seasoned DevOps Engineer with 9+ years of experience, I have expertise in automating, building, deploying, and releasing code across various environments. My technical skills include Linux OS, Containerization, Orchestration, Infrastructure Provisioning, Automation, and DevOps evaluations. I have a successful track record of achieving major milestones for high-profile clients such as Walmart and American Airlines. My knowledge and understanding of AWS Cloud Services, networking, and troubleshooting enable me to manage all aspects of the software configuration management process. I have experience in source code migrations, CI/CD pipeline creation, and building shared libraries. I also possess extensive experience in microservice-oriented architectures, utilizing Kubernetes for deployments, auto-scaling, config maps, and ingress. Moreover, I have demonstrated my ability to work with different development methodologies and enterprise systems architectures. As a team player, I have trained developers on different DevOps practices and tools. I am passionate about leveraging my skills to help organizations achieve their goals through efficient and effective DevOps practices."
}

@app.route('/')
def home():
    return render_template('home.html', name=resume_data["name"], about=resume_data["about"], skills=resume_data["skills"], certifications=resume_data["certifications"])

@app.route('/skills', methods=['GET'])
def display_skills():
    return render_template('skills.html', skills=resume_data["skills"])

@app.route('/certifications', methods=['GET'])
def display_certifications():
    return render_template('certifications.html', certifications=resume_data["certifications"])

# Error handler for routes that are not found
@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page not found", 404

if __name__ == '__main__':
    app.run(debug=True)
