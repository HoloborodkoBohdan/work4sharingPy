# Project Title

Python parser for Work4Share

## Getting Started & Installation

- ```git clone``` this repo
- make a ```venv```, run ```pip install requirements.txt```
- run ```python manage.py migrate```
- run ```python manage.py runserver``` to run the server
- run ```python manage.py scrape glassdoor -c 2``` to run scraping
- run ```python manage.py match``` to run matching

## How to run scrape
run ```python manage.py scrape``` with aditional params:
* You need to specify a site for scraping. Available variants: **glassdoor, stepstone**. 
This is a required parameter.
* ```-c (--count)``` determines the number of vacancies for parsing. The default is 20. This is an optional parameter.

Example: ```python manage.py scrape glassdoor -c 2```

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

* **Stepan Filonov** - *Initial work, create API, matching and parse Lithuanian job site* - [stepacool](https://github.com/stepacool)
* **Bohdan Holoborodko** - *Change scrape and begin to parse German job site* - [HoloborodkoBohdan](https://github.com/HoloborodkoBohdan)
* **Sergey Lavrov** - *Some fixes and parse German job site* - [lavsexpert](https://github.com/lavsexpert)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
