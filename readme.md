# Banning System
## Table of Contents
- [Introduction](#introduction)
- [Features of the Banning System](#features-of-the-banning-system)
- [Running the Code in Docker](#running-the-code-in-docker)
  - [Prerequisites](#prerequisites)
  - [Step 1: Build the Docker Image](#step-1-build-the-docker-image)
  - [Step 2: Run the Docker Container](#step-2-run-the-docker-container)
  - [Step 3: Access the Application](#step-3-access-the-application)
- [Usage](#usage)

## Introduction
This project is a banning system designed to prevent abuse and spam on a platform. It uses multiple approaches to detect and ban malicious users. The system also utilizes Redis for storing failed attempts, which allows for faster access compared to making database calls.

## Features of the Banning System
The banning system has the following features:

- **Disposable Email Detection**: Detects and bans users signing up with temporary email addresses using a list of known disposable email providers.
- **Proxy Detection**: Detects and bans users signing up or browsing the platform through proxy/VPN IPs. 
- **Link and Platform Blocking**: Blocks users who try to make multiple failed attempts on some specific order.
- **Platform and IP Blocking**: Blocks IPs/Users/Emails who try to make multiple failed attempts on the platform or some specific order.
- **Efficient Failed Attempt Tracking**: Stores failed attempts in Redis for fast access and efficient monitoring. 

## Note

This code focuses on the logic and structuring of the banning system. It doesn't focus on the integration of the banning system with a real application. There are a few things to note:

* There is no sample code repository available that can be used to easily integrate the banning system with a realistic application.
* The code doesn't include the design of the database and a sample application with the orders/users subapps.
* Instead, it focuses on the very high level details of how a basic banning system can be implemented.
* Considering the timeframe, it is a very basic implementation. The actual production-level feature will have lots of things to be considered, like the security, monitoring, risk level calculations which are not considered in this solution.
* However once I am exposed to the actual code where this has to be integrated, there can be a proper integration and feature development.

## Running the Code in Docker

### Prerequisites
- Docker and Docker Compose installed on your system
- Python 3.13 or higher installed on your system

### Step 1: Build the Docker Image
Run the following command to run the docker container:

```bash
cd ban-app && docker compose up -d --build
```
This command will build a Docker image and start a new container and map port `8000` on the host machine to port `5000` in the container.

### Step 2: Access the Application
Open a web browser and navigate to [http://localhost:8000](http://localhost:8000) to access the application.

## Usage
The application provides several endpoints to interact with the banning system:

- **`/validate_email`**: Validate an email address to check if it is disposable or not.  
  - **Example (Invalid email - Bad DNS)**: [http://localhost:8000/validate_email?email=hello@5ejulyefcfer.org](http://localhost:8000/validate_email?email=hello@5ejulyefcfer.org)  
  - **Example (Disposable email)**: [http://localhost:8000/validate_email?email=hello@4warding.com](http://localhost:8000/validate_email?email=hello@4warding.com)
  - **Example (Valid email)**: [localhost:8000/validate_email?email=hello@hotmail.com](localhost:8000/validate_email?email=hello@hotmail.com)
  

- **`/validate_ip`**: Validate an IP address to check if it is blocked or not.  
  - **Example**: [http://localhost:8000/validate_ip?ip=84.239.49.177](http://localhost:8000/validate_ip?ip=84.239.49.177)

- **`/check_proxy`**: Check if an IP address is a proxy or not.  
  - **Example (Proxy IP)**: [http://localhost:8000/check_proxy?ip=84.239.49.177](http://localhost:8000/check_proxy?ip=84.239.49.177)  
  - **Example (Non-Proxy IP)**: [http://localhost:8000/check_proxy?ip=84.18.167.244.215](http://localhost:8000/check_proxy?ip=84.18.167.244.215)

- **`/failed-attempts`**: Returns recent failed attempts for a given user ID, email, or IP..  
  - **Example**: [http://localhost:8000/failed-attempts?user_id=123&email=user@marketing.com&ip=192.168.1.100](http://localhost:8000/failed-attempts?user_id=123&email=user@marketing.com&ip=192.168.1.100)

- **`/record-failed-attempt`**: Records a failed attempt for a given user ID, email, or IP.  
  - **Example**: ```curl -X POST -H "Content-Type: application/json" -d '{"user_id": "123", "email": "user@marketing.com", "ip": "192.168.1.100"}' http://localhost:8000/record-failed-attempt```

- **`/failed-orders`**: Returns recent failed orders for a given link.  
  - **Example**: [http://localhost:8000/failed-orders?link=https://marketing.com/order/123](http://localhost:8000/failed-orders?link=https://marketing.com/order/123) 

- **`/record-failed-order`**: Records a failed order for a given link.  
  - **Example**: ```curl -X POST -H "Content-Type: application/json" -d '{"link": "https://marketing.com/order/123"}' http://localhost:8000/record-failed-order```


These endpoints can be accessed using `curl` or a web browser.


