# Project Title

Python parser for Work4Share

## Getting Started & Installation

- ```git clone``` this repo
- make a ```venv```, run ```pip install requirements.txt```
- run ```python manage.py migrate```
- run ```python manage.py runserver``` to run the server
- run ```python manage.py scrape glassdoor -c 2``` to run scraping
- run ```python manage.py match -m -t 5 -p 50``` to run matching

## How to run scrape
run ```python manage.py scrape``` with additional params:
* You need to specify a site for scraping. Available variants: **glassdoor, stepstone**. 
This is a required parameter.
* ```-c (--count)``` determines the number of vacancies for parsing. The default is 20. This is an optional parameter.

Example: ```python manage.py scrape glassdoor -c 2```

## How to run match
Before run match create file **local_settings.py** in folder **JobParser** and fill it your email settings like this:

    EMAIL_HOST = 'smtp.google.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'mymail@gmail.ru'
    EMAIL_HOST_PASSWORD = 'mypassword'

run ```python manage.py match``` with additional params:
* ```-m (--mail)``` if you need send mails. The default is False.
* ```-t (--top)``` maximum number of most suitable vacancies to found. The default is 10.
* ```-p (--percent)``` minimum percentage of suitable vacancies to foundd. The default is 70.0.

Example: ```python manage.py match -m True -t 5 -p 50```

## How it works

The server accepts new Employee data on the ```/api/v1/employees/``` endpoint. POST requests only. Fields schema can be found in scraping/models.py

There's a command that processes every employee in the database with status ```active```. It should be run on a minute basis in production.

ADMIN LOGIN:PASS - admin:admin123

### Prerequisites

```
Python 3, pip, virtualenv
```

## Running the tests

Explain how to run the automated tests for this system

## Deployment

Add additional notes about how to deploy this on a live system

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Stepan Filonov** - *Initial work* - [stepacool](https://github.com/stepacool)
* **Bohdan Holoborodko** - *Change scrape and API* - [HoloborodkoBohdan](https://github.com/HoloborodkoBohdan)
* **Andrey Konovalov** - *Parse Lithuania and German job sites* - [Loveskyrim](https://github.com/Loveskyrim)
* **Sergey Lavrov** - *Integrate, change scrape and matching* - [lavsexpert](https://github.com/lavsexpert)

## License

This project is licensed under the Creative Commons - see the [Creative Commons — CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) for details
