# A web dev homepage project
<img src="https://img.shields.io/badge/django-2.2-green"><img src="https://img.shields.io/static/v1?label=licence&message=GPL&color=blue"><img src="https://img.shields.io/static/v1?label=build&message=passing&color=green">

<!-- begin toc -->
## Table of content
* [The project](#the-project)
* [Dependecies](#dependecies)
* [Usage](#usage)

<!-- end toc -->

## The project
This is my web dev homepage repository and I build it using Django and Bootstrap framework and font awesome for the style.   

For the contact email service I used SendGrid API service.  

## Dependecies
* Django
* django-sendgrid-v5

## Usage
### create project directory
```bash
mkdir project && cd project
```

## create python virtual environment and activate it
```bash
python3 -m venv venv
source venv/bin/activate
```

## clone project
```bash
git clone https://github.com/thalesbruno/thalesbruno.me
```

## change dir name to src
```bash
mv thalesbruno.me src
```

## install dependencies
```bash
cd src
pip install -r requirements/local.txt
```

## SendGrid integration
First of all, you must create an account in SendGrid.com and generate an API Key.
So, you must create the sendgrid.env file with `SENDGRID_API_KEY` environment variable.
## create sendgrid.env file end export SENDGRID_API_KEY variable
```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
source ./sendgrid.env
```

## run the migrates
```bash
python manage.py makemigrations
python manage.py migrate
```

## run the server
```bash
python manage.py runserver
```