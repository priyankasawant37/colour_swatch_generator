from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
import colorsys

#method to get list of all possible Endpoints
@api_view(['GET'])
def routes(request):
    routes = [
        {
            'Endpoint': '/generate_colours/',
            'method': 'GET',
            'body': None,
            'description': 'Returns Five Random Colours'
        },
        {
            'Endpoint': '/show_swatch/',
            'method': 'GET',
            'body': None,
            'description': 'Displays Five Colours Swatch'
        },
        {
            'Endpoint': '/rgb_to_hls?r={}&g={}&b={}',
            'method': 'GET',
            'body': None,
            'description': 'Returns RGB to HSL codes'
        },
        {
            'Endpoint': '/hsl_to_rgb?h={}&s={}&l={}',
            'method': 'GET',
            'body': None,
            'description': 'Returns HSL to RGB codes'
        },

    ]
    return Response(routes)




#extra method: converts hls to rgb
@api_view(['GET'])
def rgb_to_hls(request):
    red = round(int(request.GET['r'])/100,1)
    green = round(int(request.GET['g'])/100,1)
    blue = round(int(request.GET['b'])/100,1)
    print(red, blue, green)
    response = {'scheme':'hls', 'value' : 'hls({:.1f}, {:.2f}%, {:.2f}%)'.format(*colorsys.rgb_to_hls(red, green, blue))}
    return Response(response)

#extra method: converts hls to rgb
@api_view(['GET'])
def hls_to_rgb(request):
    hue = round(int(request.GET['h'])/100,1)
    light = round(int(request.GET['l'])/100,1)
    saturation = round(int(request.GET['s'])/100,1)
    response = {'scheme':'rgb', 'value' : 'rgb({:.1f}, {:.2f}%, {:.2f}%)'.format(*colorsys.hls_to_rgb(hue, light, saturation))}
    return Response(response)

#method to generate random float or int number
def random_num_generator(low, high):
    if type(high) == int:
        return random.randint(low,high)
    elif type(high) == float:
        return round(random.uniform(low,high), 1)
    return 0

#decorator to generate random n numbers where n is length of  parameters_list
#in the range of each number in parameters_list as a highest possible value
def meta_decorator(arg):
    def random_num_deco(func):
        def random_nums(parameters_list):
            random_parameters = [random_num_generator(low, i) for i in parameters_list]
            return func(random_parameters)
        return random_nums
    if callable(arg):
        low = 0
        return random_num_deco(arg)
    else:
        low = arg
        return random_num_deco

#Method for hsl colour space
#parameters_list : list of highest possible value for each parameter in the RGB colour space i.e [255, 255, 255]
@meta_decorator
def rgb(parameters_list):
    colour = {'scheme': 'rgb',
                'value': 'rgb({}, {}, {})'.format(*parameters_list)}
    return colour


#Method for hsl colour space
#parameters_list : list of highest possible value for each parameter in the HSL colour space i.e [360, 100, 100]
@meta_decorator
def hsl(parameters_list):
    colour = {'scheme': 'hsl',
                'value': 'hsl({}, {}%, {}%)'.format(*parameters_list)}
    return colour


#MExtra ethod: for rgba colour space
@meta_decorator(0.0)
def rgba(parameters_list):
    colour = {'scheme': 'rgba',
                'value': 'rgba({}, {}, {}, {})'.format(*parameters_list)}
    return colour


#uncomment this to test brgb colourspace and add
# @meta_decorator
# def brgb(red_max, green_max, blue_max):
#     colour = {'scheme': 'brgb',
#                 'value': 'brgb({}, {}, {})'.format(red_max, green_max, blue_max)}
#     return colour
#functions = {rgb:[255, 255, 255], hsl:[360, 100, 100], brgb:[255,255, 1000]}

functions = {rgb:[255, 255, 255], hsl:[360, 100, 100]}

#generates random five colours in RGB and HSL colour spaces using rgb(), hsl() function defined above
@api_view(['GET'])
def generate_colours(request):
    colours = []
    for i in range(5):
        key  = random.choice(list(functions.keys()))
        value = functions[key]
        colours.append(key(value))
    return Response(colours)

#renders generated colours into swatch
def show_swatch(request):
    return render(request, 'api/swatches.html')
