
  

# SWA-Practical

Small API written in Python using Flask that has routes to `skills`, `certifications`, `education` from a static resume.

  
  

App is publicly available at https://karnihar.awsps.myinstance.com/

- App redirects from HTTP to HTTPS.

- App is load-balanced and autoscaling is set to min=1 and max=4 instances.

- App uses `ELBSecurityPolicy-tls13-1-3-2021-06`, this policy is an AWS Elastic Load Balancer (ELB) security policy that supports TLS 1.3 encryption protocol.

- App uses recommendations which are aligned with [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/). The Well-Architected Framework provides best practices to help build secure, high-performing, resilient, and efficient infrastructure for applications and workloads. Focusing on the [Security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) of the framework, we will walk through additional configurations for increased network protection and protection of data at rest and in transit.

  

The application uses below security best practices based on the Security pillar of the Well-Architected Framework.

  

- Protect Networks

- Protect data at Rest

- Protect data in transit

  
  

To achieve the above three things, we implemented the below as part of this practical:

1. Created own VPC with public and private subnets.

5. Create a highly-available Elastic Beanstalk application.

6. Modified the configuration to deploy instances in private subnets and loadbalancer in public subnets.

7. Encrypted the logs and source code bucket.

8. Launched an encrypted RDS instance.

9. Set up encryption in-transit by using the HTTPS protocol and HTTPS redirection while using latest TLS policy.

  
  

## App Architecture:

  

![Figure 1: Target architecture for the two-tier web application deployed using Elastic Beanstalk](https://d2908q01vomqb2.cloudfront.net/22d200f8670dbdb3e253a90eee5098477c95c23d/2021/12/06/image1-1.png)

  

Figure 1: Architecture for the two-tier web application deployed using Elastic Beanstalk.

  

*Note: Database shown here is just a illustration of thought and I was not able to spin it up due to cost factors but the idea is simple.*

  

Clients resolve the website’s domain name using the Domain Name System (DNS) service [Amazon Route 53](https://aws.amazon.com/route53/). An [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) (ALB) is used to direct traffic to and from the [Amazon EC2](https://aws.amazon.com/ec2/) instances which are running the web servers. The EC2 instances are deployed in an [Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) in private subnets. To ensure that clients can always access the application, the infrastructure is setup so that it can automatically deal with system failures and scale up when there’s an increase in demand. This is done by placing the EC2 instances in the Auto Scaling group across two Availability Zones for high availability. There is also an RDS MySQL database deployed in a private subnet, which is replicated to a stand-by instance in another Availability Zone for disaster recovery. Logs and Metrics are sent to CloudWatch, and [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) is used to store logs and source code. Finally, a [Network Address Translation (NAT) gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) and [Internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) manage inbound and outbound traffic to subnets.

  

## VPC Flow Diagram:

  

![enter image description here](https://github.com/niharkarra/SA-Practical/blob/feature/v1.0/static/vpc_flow_diagram.png)

  
  

## Technology Stack:

  

**Source Code :**  `GitHub` - https://github.com/niharkarra/SA-Practical.git

  

**Automated Builds :**  `GitHub Actions` -https://github.com/niharkarra/SA-Practical/actions

  

**Artifact Repository and Logs:**  `S3 Bucket` - `s3://swa-practical/`

  

**Deployment Platform:**  `Beanstalk Environment` - `Swa-vpc-env-env`

https://us-east-1.console.aws.amazon.com/elasticbeanstalk/home?region=us-east-1#/environment/dashboard?environmentId=e-mfipgtqp5r

  

**CloudFormation Stack for beanstalk environment** - https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/stackinfo?stackId=arn%3Aaws%3Acloudformation%3Aus-east-1%3A217542142459%3Astack%2Fawseb-e-mfipgtqp5r-stack%2F9664f130-03d1-11ee-a4b4-0e88695980d3

  

**CloudFormation Stack for Custom VPC and additional Networking resources** - https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/stackinfo?stackId=arn%3Aaws%3Acloudformation%3Aus-east-1%3A217542142459%3Astack%2Fswa-vpc%2F2c96ca10-03ce-11ee-aac5-0a03e687a1a1

  

**Load Balancer** - `ALB` - https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#LoadBalancers:search=arn:aws:elasticloadbalancing:us-east-1:217542142459:loadbalancer/app/awseb-AWSEB-QQ19U5EL4CEJ/340ceb3a4b0b9316

  

**AWSEBSecurityGroup** - https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#SecurityGroups:search=sg-0b492d862b1662f31

  

**AWSEBLoadBalancerSecurityGroup** - https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#SecurityGroups:search=sg-0611c15de6121882f

  

**CloudWatch Alarms (High) -** https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#alarm:alarm:alarmFilter=ANY;name=awseb-e-mfipgtqp5r-stack-AWSEBCloudwatchAlarmHigh-11S162SXA3HBY

  

**CloudWatch Alarm (Low) -** https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#alarm:alarm:alarmFilter=ANY;name=awseb-e-mfipgtqp5r-stack-AWSEBCloudwatchAlarmLow-4DDYYRTNMLJ2

  

**AutoScaling Group -** https://us-east-1.console.aws.amazon.com/ec2autoscaling/home?region=us-east-1#/details?id=awseb-e-mfipgtqp5r-stack-AWSEBAutoScalingGroup-B1XZT8CT9X5B

  

**Other Technologies used:**

  

> Docker, Python, Secrets Manager, AWS Certificate Manager, Route53, AWS KMS, RDS

  

## Routes Available:

- home: https://karnihar.awsps.myinstance.com/

- skills: https://karnihar.awsps.myinstance.com/skills

- certifications: https://karnihar.awsps.myinstance.com/certifications

- education: https://karnihar.awsps.myinstance.com/education

  

## Running the App Locally:

  

**Prerequisites:** Python3

1. Run locally using `python3 -m flask run --host=0.0.0.0 --port=5001`

2. Visit the site at http://127.0.0.1:5001/

  

## Running the App as Docker Container:

  

1. From the root of the app, build docker image by running

`docker build -t swa-app .`

2. Now run the container using the build image by running

`docker run -p 80:80 swa-app`

3. Visit the site at http://127.0.0.1/

  
  
  

## References:

  

1. AWS Well-Architected Framework - https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc
2. Security Pillar of the framework - https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html
3. AWS Elastic Beanstalk - https://aws.amazon.com/elasticbeanstalk/

4. Beanstalk .ebextensions - https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html

6. GitHub - https://github.com/

7. GitHub Actions - https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions

8. AWS Elastic Load Balancing - https://aws.amazon.com/elasticloadbalancing/

9. AWS Certificate Manager - https://aws.amazon.com/certificate-manager/

10. AWS VPC - https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html

11. AWS S3 - https://aws.amazon.com/s3/

12. AWS Route53 - https://aws.amazon.com/route53/

13. AWS KMS - https://aws.amazon.com/kms/

14. AWS RDS - https://aws.amazon.com/rds/

15. AWS CloudWatch - https://aws.amazon.com/cloudwatch/

16. AWS CloudFormation - https://aws.amazon.com/cloudformation/

17. AWS Secrets Manager - https://aws.amazon.com/secrets-manager/

18. Docker - https://docs.docker.com/get-started/02_our_app/