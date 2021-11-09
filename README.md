# Colour Swatch Generator

## Function

A service that could be easily used, and also easily extended, by all the teams in the company.
The service should be able to render a "swatch" of five colors, each color being potentially represented in a different color space (RGB, HSL, etc).

##Folder Structure

├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── colours.js
│   ├── templates
│   │   └── api
│   │       └── swatches.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── colour_swatch
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── colour_swatch_generator
│   └── README.md
├── db.sqlite3
└── manage.py


## Usage


To setup your virtual environment:

    virtualenv venv

To activate your virtual environment:

    source venv/bin/activate

To install requirements:
    pip install djangorestframework
    pip install markdown

To run:
    python3 manage.py runserver

access on http://127.0.0.1:8000/
