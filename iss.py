#!/usr/bin/env python

__author__ = 'jmsMaupin1'

import requests
import json
import turtle
import time


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


def draw_iss_position():
    wn = turtle.Screen()
    wn.addshape('iss.gif')
    wn.bgpic('map.gif')
    wn.setup(720, 360)
    wn.setworldcoordinates(-90, -180, 90, 180)
    wn.title('turtle time!')

    pen = turtle.Turtle()
    pen.shape('iss.gif')
    while True:
        iss_location = get_iss_location()
        print(iss_location)
        pen.penup()
        pen.goto(
            float(iss_location['latitude']),
            float(iss_location['longitude'])
        )
        time.sleep(5)
    turtle.done()


def next_time_over(lat, long):
    api_string = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'
    print_str = 'The ISS will at your location on {} for {} mins and {} secs'

    res = requests.get(api_string.format(lat, long))
    res.raise_for_status()
    over_times = json.loads(res.text)['response']

    for t in over_times:
        date_time = time.ctime(t['risetime'])
        duration_minutes = int(t['duration']) / 60
        duration_seconds = int(t['duration']) % 60

        print(print_str.format(
            date_time,
            duration_minutes,
            duration_seconds
        ))


def main():
    astronauts_in_space()
    next_time_over(lat=39.7684, long=86.1581)

    draw_iss_position()


if __name__ == '__main__':
    main()
