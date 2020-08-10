# Courses Application

This project is created in order to understand Simple REST API by using Django and Django Rest Framework. 
There are POST and GET requests for <b> courses list </b> with GET, PUT, and DELETE for <b> course detail </b>.

## Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 
*(Commands are written for Windows.)*

### Requirments

After downloading the repository, get virtual environment and activate it in your directory:
```
pip install virtualenv
python -m venv venv
venv\Scripts\activate
```

Now that you're inside a virtual environment, install project's package requirements:

```
pip install -r requirements.txt
```

## Getting started

There is an overview on how it works:
```
cd courses_app
python manage.py runserver
```
Go to localhost:
* for courses list to http://127.0.0.1:8000/courses/
* for course detail to http://127.0.0.1:8000/course/ {course_id}

## Running the tests

## Documentation

[Courses Application's API](https://coursesapi4.docs.apiary.io/#)

APIs for:
* Course List [/courses/](http://private-a67b02-coursesapi4.apiary-mock.com/courses)
* Course Detail [/courses/{course_id}](https://private-a67b02-coursesapi4.apiary-mock.com/courses/course_id/)
    
## Deployment

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) which was used in order to learn REST API
* [RESTful API guidelines](https://opensource.zalando.com/restful-api-guidelines/)

## Versioning

There are no other versions

## Authors

* <b>Sardar Sultanaliev</b> - *initial work* - [pawtny](https://github.com/pawtny)
