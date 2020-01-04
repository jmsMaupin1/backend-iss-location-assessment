#!/usr/bin/env python

__author__ = 'jmsMaupin1'

import requests
import json
import turtle

def astronauts_in_space():
    res = requests.get('http://api.open-notify.org/astros.json')
    res.raise_for_status()
    astro_dict = json.loads(res.text)['people']
    
    for astro in astro_dict:
        print('{} is on the {}'.format(astro['name'], astro['craft']))

def get_iss_location():
    res = requests.get('http://api.open-notify.org/iss-now.json')
    res.raise_for_status()
    return json.loads(res.text)['iss_position']


def turtle_iss_time():
    iss_location = get_iss_location()

    wn = turtle.Screen()
    wn.addshape('iss.gif')
    wn.bgpic('map.gif')
    wn.setup(720, 360)
    wn.setworldcoordinates(-180, -90, 180, 90)
    wn.title('turtle time!')

    pen = turtle.Turtle()
    pen.shape('iss.gif')
    pen.penup()
    pen.goto(float(iss_location['latitude']), float(iss_location['longitude']))
    turtle.done()


def draw_n_gon_with_functions(n, length, pen, function_list):
    rotation = 360 / n
    for i in range(n):
        pen.forward(length)
        if callable(function_list[i]):
            function_list[i](n, length, pen)
        pen.left(rotation)

def draw_n_gon(n, length, pen):
    if n < 3:
        pen.circle(length)
    else:
        rotation = 360 / n
        for _ in range(n):
            pen.forward(length)
            pen.left(rotation)

def turtle_time():
    wn = turtle.Screen()
    wn.bgcolor('light green')
    wn.title('turtle time!')

    pen = turtle.Turtle()
    pen.fillcolor(0, 0, 0)
    pen.speed(0)

    rotation = 10

    embeded_triangle_func_list = [
        lambda n, length, pen: draw_n_gon(2, length, pen),
        lambda n, length, pen: draw_n_gon(2, length, pen),
        lambda n, length, pen: draw_n_gon(2, length, pen)
    ]

    embedded_square_func_list = [
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
    ]

    func_list = [
        lambda n, length, pen: draw_n_gon_with_functions(4, length, pen, embedded_square_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(4, length, pen, embedded_square_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(4, length, pen, embedded_square_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(4, length, pen, embedded_square_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(4, length, pen, embedded_square_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(4, length, pen, embedded_square_func_list),
        lambda n, length, pen: draw_n_gon_with_functions(3, length, pen, embeded_triangle_func_list),
    ]

    for _ in range(360 / rotation):
        
        draw_n_gon_with_functions(12, 100, pen, func_list)
        pen.right(rotation)
    turtle.done()

def main():
    turtle_iss_time()


if __name__ == '__main__':
    main()
