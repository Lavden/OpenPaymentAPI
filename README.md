# OpenPaymentAPI

Implemented a RESTful API to provide role-based access control for the database.

## Introduction

### Dataset
OpenPayment

### Architecture
![Image of architecture](https://github.com/Lavden/OpenPaymentAPI/blob/master/img/architecture.jpg)

- Django/ Django Rest Framework

- AWS API Gateway + AWS Lambda

- Zappa

## Get Start

## Usage

|               | GET           | PUT  |POST | DELETE |
| ------------- |:-------------:| -----:| -----:| -----:|
| records       | retrieve all payment records |   | | |
| record/:id    | retrieve payment record with record_id = :id |  | | |
| profiles/     | retrieve all user profiles   |     | | |
| profile/:id   | retrieve user profile with record_id = :id   |    | | |



## Engineering challenges

## Trade-offs: Lambda vs. Elastic Beanstalk

## Links
[Presentation Slides](https://docs.google.com/presentation/d/1CIblp7mv2DxjX0ypKoIAFmMNTRQMO3svQVtcke1DneY/edit?usp=sharing)

[Install Zappa](https://www.agiliq.com/blog/2019/01/complete-serverless-django/)

[QuickStart of Django-Rest_Framework](https://blog.lawrencemcdaniel.com/serve-a-django-app-from-an-aws-lambda-function/)

[Configure RDS with AWSLambda + Django](https://www.codingforentrepreneurs.com/blog/rds-database-serverless-django-zappa-aws-lambda)

