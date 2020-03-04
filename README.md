# OpenPaymentAPI

Implemented a RESTful API to provide role-based access control for the database.

## Introduction
Today there are no projects or applications that don't have a REST API for the creation of professional services based on their software. REST API provides interfaces for users to grant their access to data. However, how to manage who have rights to access which part of the data becomes more and more important as the data grows large and complicated. 

As a result, design the REST API based on permission policy can solve the above problem. Permissions are used to grant or deny access for different classes of users to different parts of the API. Which means, the authenticated user can only access the data associted to his/her class, and has no permission to access other class of user's data. 


### Dataset
[OpenPayment Dataset](https://www.cms.gov/OpenPayments/Explore-the-Data/Dataset-Downloads)

### Use Cases
- Payment records are associated with a company and a physician or hospital.
- Only authenticated companies may create payment records.
- Only the physician or hospital who is associated with the payment records may update or delete it.
- Unauthenticated requests should have full read-only access.


## Architecture
![Image of architecture](https://github.com/Lavden/OpenPaymentAPI/blob/master/img/architecture.jpg)

- Django/ Django Rest Framework

- AWS API Gateway + AWS Lambda

- Zappa

## Usage

|               | GET           | PUT  |POST | DELETE |
| ------------- |:-------------:| -----:| -----:| -----:|
| records       | retrieve all payment records |   | | |
| record/:id    | retrieve payment record with record_id = :id |  | | |
| profiles/     | retrieve all user profiles   |     | | |
| profile/:id   | retrieve user profile with record_id = :id   |    | | |



## Engineering challenges - Schema Design
![Image of schema](https://github.com/Lavden/OpenPaymentAPI/blob/master/img/schema.jpg)

The OpenPayment Dataset is in .csv format with hundreds of in each file. The major columns I used to identify user class are type of users: company, hospital, physician. Each row in the file contains infomration about financial relationships between the health care industry(companys), physicians, and teaching hospitals. 
1. Figure out the relationships between health care industry and pyhsicians/ teaching hospitals. 
 * One health care industry can pay to multiple physicians and teaching hospitals.
 * One physician/ teaching hospital can receive sponsor from multiple health care industries.
  The health care indutry and physician/teaching hospital has many to many relationship. 
2. Django Rest Framework already provide User model for the authenticated system. This can only used to identy user authentication (user name + password), without any permission check based on user class.
<!-- ## Trade-offs: Lambda vs. Elastic Beanstalk -->

## Links
[Presentation Slides](https://docs.google.com/presentation/d/1CIblp7mv2DxjX0ypKoIAFmMNTRQMO3svQVtcke1DneY/edit?usp=sharing)

[Demo]()

[Install Zappa](https://www.agiliq.com/blog/2019/01/complete-serverless-django/)

[QuickStart of Django-Rest_Framework](https://blog.lawrencemcdaniel.com/serve-a-django-app-from-an-aws-lambda-function/)

[Configure RDS with AWSLambda + Django](https://www.codingforentrepreneurs.com/blog/rds-database-serverless-django-zappa-aws-lambda)

