# Colour Swatch Generator

## Function

A service that could be easily used, and also easily extended, by all the teams in the company.
The service should be able to render a "swatch" of five colors, each color being potentially represented in a different color space (RGB, HSL, etc).


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


## Brief about code implementation

Frontend is implemented in simple jquery and ajax in colour.js and colour swatches can be accessed through http://127.0.0.1:8000/show_swatch/ url

Backend is using djangorestframework

API Endpoints

* GET /
 Gives list of possible actions

* GET /generate_colours/
Gives list of 5 randomly generated colours in rgb and hsl colourspaces
Eg.
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "scheme": "rgb",
        "value": "rgb(53, 218, 170)"
    },
    {
        "scheme": "rgb",
        "value": "rgb(37, 108, 54)"
    },
    {
        "scheme": "rgb",
        "value": "rgb(217, 26, 33)"
    },
    {
        "scheme": "hsl",
        "value": "hsl(214, 71%, 78%)"
    },
    {
        "scheme": "rgb",
        "value": "rgb(157, 107, 16)"
    }
]

Decorator random_num_deco in api/views.py file is used to generate a list of random numbers (int and floats) depending on the parameters used in colour colourspaces
For eg. RGB uses 3 colours with 0 as min value and 255 as max value for Red, Green, Blue respectively
so to create single random rgb colour parameter list would be [255,255,255] where 255 is highest number possible for R,G,B.


Function rgb(parameters_list) returns the colour in {scheme: 'rgb', value: 'rgb(x, y, x)'} format which is passed to Frontend to render in the swatch

## To add new colour space eg. brgb

Add a new function which takes parameter lists as a list of maximum colour code value for each colour in the colourspace and the function name as key and parameter_list as value
in following line in views.py
functions = {rgb:[255, 255, 255], hsl:[360, 100, 100]}
eg. functions = {rgb:[255, 255, 255], hsl:[360, 100, 100], brgb:[255,255, 1000]}

## Limitations:
Though using current code we can generate other colour codes like rgba, it's not possible to generate hex colour code
