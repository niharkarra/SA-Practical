# SA-Practical

Sample API written in Python using Flask that returns elements like skills, certifications, achievements from a static resume

## Technology Stack:

**Source Code :** `GitHub` - https://github.com/niharkarra/SA-Practical.git
**Automated Builds :** `GitHub Actions` -https://github.com/niharkarra/SA-Practical/actions

**Artifact Repository and Logs:** `S3 Bucket` - `s3://swa-practical/`

**Deployment Platform:** `Beanstalk Environment` - `SA-Practical-dev`

**CloudFormation Stack** - arn:aws:cloudformation:us-east-1:217542142459:stack/awseb-e-3fcdqdtmw4-stack/bafb6d90-0290-11ee-bfc7-0e9281aee647

**Load Balancer** - arn:aws:elasticloadbalancing:us-east-1:217542142459:loadbalancer/app/awseb-AWSEB-1QW0JORJ7XF2W/f12c1c2f930c5b3b

**Security Group** - sg-04e665a764e2246b1

**Beanstalk URL** - http://sa-practical-dev.us-east-1.elasticbeanstalk.com/

**Public URL** - https://karnihar.awsps.myinstance.com/

## Routes Available:

 - home: https://karnihar.awsps.myinstance.com/ 
 - skills: https://karnihar.awsps.myinstance.com/skills 
 - certifications: https://karnihar.awsps.myinstance.com/certifications
 - education: https://karnihar.awsps.myinstance.com/education

## Running the App Locally:


**Prerequisites:** Python3

Run locally using `python3 -m flask run --host=0.0.0.0 --port=5001`

