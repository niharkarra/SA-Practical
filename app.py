from flask import Flask, render_template

app = Flask(__name__)

resume_data = {
    "name": "Nihar Karra",
    "skills": ["UNIX & LINUX", "AWS", "Docker", "Kubernetes", "Git, GitHub, BitBucket", "Jenkins", "Python", "Maven, Gradle, NodeJs", "Sonatype Nexus, NexusIQ", "Jfrog Artifactory, Xray", "Sonarqube", "CloudFormation", "Beanstalk", "VPC", "IAM", "S3", "ELB", "ROUTE53"],
    "certifications": ["Certified Kubernetes Administrator", "AWS Certfied Cloud Practitioner", "AWS DevOps Professional (In progress)", "Awarded a special recognition by MD, Enterprise Services, American Airlines for my contributions towards Enterprise DevOps Services", "Awarded Remedy Master for my services as a Release Manager &amp; DevOps Lead in Walmart."],
    "about": "As a seasoned DevOps Engineer with 9+ years of experience, I have expertise in automating, building, deploying, and releasing code across various environments. My technical skills include Linux OS, Containerization, Orchestration, Infrastructure Provisioning, Automation, and DevOps evaluations. I have a successful track record of achieving major milestones for high-profile clients such as Walmart and American Airlines. My knowledge and understanding of AWS Cloud Services, networking, and troubleshooting enable me to manage all aspects of the software configuration management process. I have experience in source code migrations, CI/CD pipeline creation, and building shared libraries. I also possess extensive experience in microservice-oriented architectures, utilizing Kubernetes for deployments, auto-scaling, config maps, and ingress. Moreover, I have demonstrated my ability to work with different development methodologies and enterprise systems architectures. As a team player, I have trained developers on different DevOps practices and tools. I am passionate about leveraging my skills to help organizations achieve their goals through efficient and effective DevOps practices.",
    "education": [
        {
            "degree": "Master of Science",
            "major": "Information Systems Security",
            "year": 2019,
            "location": "Kentucky, USA"
        },
        {
            "degree": "Master of Science",
            "major": "Electrical and Electronics Engineering",
            "year": 2015,
            "location": "California, USA"
        },
        {
            "degree": "Bachelor of Technology",
            "major": "Electrical and Electronics Engineering",
            "year": 2013,
            "location": "Hyderabad, India"
        }
    ],
    "contact": {
        "email": "niharreddyk9@gmail.com",
        "phone": "+1 847-786-9012",
        "address": "10591 N MacArthur Blvd, Irving, Tx, 75063"
    }
}

@app.route('/')
def home():
    return render_template('home.html', name=resume_data["name"], about=resume_data["about"], skills=resume_data["skills"], certifications=resume_data["certifications"], education_data=resume_data["education"])

@app.route('/skills', methods=['GET'])
def display_skills():
    return render_template('skills.html', skills=resume_data["skills"])

@app.route('/certifications', methods=['GET'])
def display_certifications():
    return render_template('certifications.html', certifications=resume_data["certifications"])

@app.route('/education', methods=['GET'])
def display_education():
    return render_template('education.html', education=resume_data["education"])

# Error handler for routes that are not found
@app.errorhandler(404)
def page_not_found(e):
    return "404 - Page not found", 404

if __name__ == '__main__':
    app.run(debug=True)
