# What is Cloud Computing?
The delivery of computing service to offer faster innovation, flexible resources and economies of scales.

## Types of Cloud and their use cases
- Public: owned and operated by a 3rd party, rent access to cloud - AWS, Microsoft Azure, Google.
- Private: used exclusively by a business and it's usually located witin the company (e.g bank ,government) or they might rent space at a provider for their own server.
- Hybrid: some resources on public and some on private e.g Netflix.

## Who's using it?
- Netflix
- Google
- McDonalds
- Spotify


## Benefits of Using Cloud Computing
- Reduced IT costs
- Scalability
- Collaboration efficiency
- Flexibility of work practices


## What is AWS?
- Comprehensive evolving cloud computing platform provided by Amazon
- Includes mixture of:
    - infrastructure as a service (IaaS)
    - platform as a service (PaaS)
    - software as a service (SaaS)

- AWS services can offer an organization tools such as compute power, database storage and content delivery services

## AWS Global Infrastructure
The AWS Cloud spans 81 Availability Zones within 25 geographic regions around the world.
### Regions
- AWS has several regions (physical location around the world where amazon clusters data centres) where you can create resources: each region has several availability zones (consists of one or more data centres at a location within an AWS region - each AZ has independent cooling, power and physical security
- If app is partitioned accross AZs, companies are better isolated/ protected from power outages, natural disasters (AZs within a region are separated within 100km from each other)
- Pick region (and AZ) thats geographically close to company/ customers:  lowest network latency and quickest response

### Data centres
- Each region has at least 2 data centres, means its highly available
    - If one data centre becomes unavailable there is a backup

## AWS services
- Elastic Compute Service `EC2`
    - A web service that provides; secure, resizable computer capacity in the cloud, designed to make web-scale cloud computing services easier: with choice of processor, storage, networking, operating system.
- Simple Storage `S3`
    - Object storage service built to store and retrieve any amount of data from anywhere.
- Virtual Private Network `VPC`
    - VPC is the networking layer for Amazon EC2 and enables launching AWS resources into a virtual network that you've defined.
        - Internet Gateway `IG`
            - Internet gateway = gateway you attach to your VPC to enable communication between resources (VPC and internet)
        - Route Tables `RT`
            - Route table: set of rules (routes)determines where network traffic is directed - routes to particular network destinations
        - Subnets `sn`
            - Subnet: the range of IP addresses in your VPC/ virtual network
        - VPC endpoints enables private connections between your VPC and AWS services e.g a S3 bucket (gateway)
        - CIDR block: how you define subnet mask, specify the range of IP addresses for the VPC

- Network Access Control `NACLs`
    - Optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets
- Security Groups `SG`
    - Acts as a virtual firewall for EC2 instances to control incoming and outgoing traffic. 
- Cloudwatch `CW`
    - A monitoring and observability service for DevOps engineers, developers etc. Provides you with data and insights to monitor applications, respond to system-wide performance changes, optimize resource utilization and get unified view of operational health
- Simple Notification Service `SNS`
    - A messaging service for both application-to-application and application-to-person communication
- Simple Que Service `SQS`
    - message queing service that allows you to decouple and scale microservices, distributed systems and serverless apps
- Load Balancers `LB` - `ALB` - `ELB`- `NLB`: The load balancer distributes incoming traffic across multiple targets, e.g Amazon EC2 instances. Increases the availability of your application. Add one or more listeners to your load balancer. A load balancer distributes incoming app traffic across multiple EC2 instances in multiple Availability Zones - increases the fault tolerance of your applications.

    - `ALB`: Application Load Balancer, operates at the request level (layer 7), routing traffic to targets- EC2 instances, containers, IP adds, based on the content of request.
        - Ideal for advanced load balancing of HTTP and HTTPS traffic.
    - `ELB`: Elastic Load Balancing, automatically distributes incoming application traffic accross multiple targets and virtual apps in one or more AZs
    - `NLB`: Network Load Balancer, functions at 4th layer (Transport), can handle millions of requests per second. After load balancer receives connection requests, it selects a target from the target group for the default rule. Then attempts to open a TCP connection to the selected target on the port specified in the listener configuration.
- Autoscaling Groups `ASG`
    - Contains a collection of Amazon EC2 instances, treated as a logical grouping for the purposes of automatic scaling and management.
- Amazon Machine Image `AMIs`
    - Provides the information required to launch an instance
    - Contains an operating system (Linux, Unix, Windows) , application server (containers: mysql server, phpmyadmin server) and applications - software configuration, contains launch permissions that control which AWS accounts can use the AMI to launch instances


## Building an EC2 instance for app

1. Choose an Amazon Machine Image (AMI)
    - Ubuntu Server 16.04 LTS (HVM), SSD
2. t2 microservice
3. Add EBS volume
    - An Amazon EBS volume is a durable, block-level storage device that you can attach to your instances. After you attach a volume to an instance, you can use it as you would use a physical hard drive.
4. Ports:
    - SSH, TCP, 22
    - HTTP, TCP, 80
    - App, TCP, 3000
5. Connect to instance
    - Add private key file to `~/.ssh`
    - `chmod 400 privatekey`
    - Connect to instance using `ssh -i`
6. Set up environment
    - update and upgrade system
    - install nginx
    - nginx enabled
    - check the public IP globally 
    - install node correct verison
    - install required dependencies
    - `app code` currently available on `local host` => must migrate it to cloud
        - `scp -i ./key.pem -r /local/host/path/ name@ipv4.compute.amazonaws.com:/instance/path/`
    - `npm install`
    - `npm start`
    - Reverse proxy
        - `sudo rm -rf /etc/nginx/sites-available/default`
        - `sudo mv ./edited_default_file /etc/nginx/sites-available/`
        - `sudo systemctl restart`
        - `sudo systemctl enable nginx`
        - `sudo systemctl status nginx`
        - `npm start`
        - access IP address without :3000 

## Building an EC2 instance for Mongodb - pseudo coding

1. Build EC2 instance as shown above
    - SSH 22 and port 27017 for security group
2. Update mongod.conf with:
```
# network interfaces
net:
  port: 27017
  bindIp: 0.0.0.0
  ```
3. 
    - `sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv D68FA50FEA312927`
    - `echo "deb https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list`
    - `sudo apt-get update -y`
    - `sudo apt-get upgrade -y`
    - `sudo apt-get install mongodb-org=3.2.20 -y`
    - `sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20`
    - `sudo systemctl restart mongod`
    - `sudo systemctl enable mongod`
- **SSH back into app instance**
4. Go back to app instance `sudo echo 'export DB_HOST="mongodb://ip:27017/posts"' >> ~/.bashrc`
    - `source ~/.bashrc`
5. `node app/app/seeds/seed.js`
6. `npm start`


## Amazon Machine AMI
- Which OS, distro version
- Dependencies
- VPC Networking - SG - or Rules
- If you save the AMI of your instance it means you can easily relaunch it at anytime

### Create an AMI
- Select the instance you wish to create an image of > Actions > Image and templates > Create an image > Launch 
- t2 microservice
- Select storage
- Select SG 

Dealing with Demand
Big advantage of AWS and similar cloud services is the ability to scale with traffic
AWS does provide the ability to automatically scale with demand
Start with monitoring with Cloudwatch
This raises when a level is reached
Spin up autosclaing group
A load balancer then rebalances the demand.
It is also possible to deploy architecture in multiple availability zones to defend against potential data center problems.
Have to create a listener group that checks machines are up and running.

#### Basics of Setting up monitoring
- When viewing an instance, select monitoring.
- This shows stats such as CPU utlisation percentage, disk write, and so forth
- Can add information to a dashboard
- need to enable detailed montioring under manage detailed monitoring
- this does cost more, so use with caution
- add the monitoring to a dashboard of choice
- next, in instances, either select the + sign next to your instances "alarm status" field, or enter the alarm creation menu via `actions -> monitor and troubleshoot ->Manage CloudWatch Alarms`
- Name your alarm, and set the threshold you would like to be notified by
- if you have an SNS group already set up, you can link it here
- Otherwise, enter the Cloudwatch dashboard and edit the alarm
- Add a new SNS group, and add the email addresses you would like to have notified when the alarm is triggered
- You should now receive an email asking you to confirm the subscription
- AWS will now let you know when your instance triggers an alarm!

Full guide to editing or setting up an alarm here

More on SNS groups here

#### Monitoring Concepts
![Alt text](C:\Users\abdul\Downloadsaws-pic.png?raw=true "Title")

- A variety of things may need to be monitored
- This depends on the app and infrastructure, but a general guideline (applicable to our example app) might be:
  - CPU utilisation
  - Number of requests, response times, latency
  - The Firewall
- Which particular resources are to be monitored and and how frequently is also important. For example, some resources may only need to be checked over once every couple of hours
- Other questions include the choice of tools, and who will be responsible for keeping track of monitoring and responding
- Also need to ensure the correct people are notified when alarms are triggered

#### The 4 Golden Signals of Monitoring
These are considered the basics of monitoring virtual infrastructure. They are:

- Latency
  - the time taken to service a request.
  - Important because slow responses indicate performance degradation or insufficient resources

- Traffic
  - Number and type of requests with time
  - Important as this shows which services are beign used and how often (e.g. how many database requests an app is havign to make or how many sessions are active concurrently)

- Errors
  - The rate of requests returning an error code

- Saturation
  - How close to maximum utilisation resources are
  - Very important as ability to provide service may decrease the closer to full utilisation an instance is

#### Responding to Monitoring
AWS' default monitoring service is Amazon Cloudwatch, which can be used for most of their resources. Key is to attempt to automate responses to monitoring. This can be done most easily with auto-scaling groups. For example, if demand peaks and services go beyond a particular utilisation, it would be useful to spin up additional instances. Defence against DDoS attacks and similar types of attempts by potentially malicious users is also available as a service, though the technical details are beyond the scope of these notes.

#### Amazon offers notifications to the user, which were implemented as previously described.
- There are also services to queue requests (SQS, or Simple Queueing Service)
  - This holds requests and processes them in turn, avoiding reqturning error codes.
- Amazon Lambdas are a way of increasing capacity by only the amount used.

A good idea is to split various metrics into separate dashboards, so that particular signals or instance types might be monitored by dedicated teams (for example a team dedicated to monitoring and analysing traffic, or a team concerned with saturation of a database server)

#### Automating the sample app
- Application Load Balancer

- Autoscaling Group

- Launch template configuration - how many instances should be running at all times
  - Minimum and maximum required (e.g. min=2, max=3)

- Policy on scaling otu and scaling in
  - Scaling inwards towards minimum number of instances as demand drops

- Scaling on Demand (Terminology)
  - Scaling Up versus scaling out: Scaling up means making components on an instance bigger to meet demand (e.g. increasing CPU capacity). Scaling means increasing the number of instances
  - Scaling to demand is generally best done by sxcaling out, as the previous configuration is known to be working.

#### Setting Up EC2 for creating S3 bucket
```
- sudo apt-get Update
- sudo apt-get upgrade
- sudo apt-get install python -y
- sudo apt-get install python-pip -y
- sudo pip install awscli
- sudo apt install python3-pip
- alias python=python3
```

#### S3
  - `aws s3 ls` to list buckets
  - `aws --version`
  - `aws configure` to add our keys and config
  - `aws s3 mb s3://name --region name`
  - `aws s3 cp s3://name/ file.md`
  - `aws s3 cp file/md s3://name/`
  - `aws s3 rm s3://bucketname --recursive`
  - `aws s3 rb s3://bucketname`
  - `aws s3 sync s3:bucketname/ test` sync from bucket to local host
  
#### AWSCLI
- AWSCLI can be used to create any `aws` resource required

#### install boto3
```
- sudo pip install virtualenv   
- $ git clone https://github.com/boto/boto3.git
- cd boto3
- virtualenv venv
- . venv/bin/activate
- python -m pip install -r requirements.txt
- python -m pip install -e .
- python -m pip install boto3
```

#### Autoscaling and Load Balancing
##### Application Load Balancer
- Autoscaling automatically adjusts the amount of computational resources based on the server load
- Load Balancing distributes traffic between EC2 instancec so that no on instance gets overwhelmed

- ASG: Launch Template or Launch Configuration
- ALB: Target group HTTP 80
- AWS Keys
- VPC - Subnets - SG
