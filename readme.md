# Django-Soap-Api

Example of a REST Api in Django.

Installation tested on Windows.

## Create Virtual  Environment

It's assumed that Python is installed and added in Windows' PATH.

Install or upgrade pip:
```bash
python -m pip install --upgrade pip
```

Install virtual env:
```bash
pip install virtualenv
```
  
Create virtual env in .venv folder:
```bash
virtualenv .venv
```

## Install Dependencies

Activate virtual environment:
```bash
.venv\Scripts\activate
```
  
Install requirements:
```bash
pip install -r requirements.txt
```

## Run Server
To run the server locally we use the following command:
```bash
python manage.py runserver
```
This will start running the API in the local host on port 8000 (http://localhost:8000/).
