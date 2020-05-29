#!/usr/bin/env python
import requests
import turtle
import time

__author__ = 'knmarvel'


def get_astronauts():
    astronauts = requests.get('http://api.open-notify.org/astros.json')
    astronauts = astronauts.json()
    print("Astronauts: ")
    for person in astronauts["people"]:
        print("  {} is currently on the {}.".format(
            person["name"], person["craft"]))
    print("There are {} people on the ISS right now.".format(
        len(astronauts["people"])))


def get_iss_coordinates():
    coords = requests.get("http://api.open-notify.org/iss-now.json")
    coords = coords.json()
    longi = coords[u"iss_position"][u"longitude"]
    lat = coords[u"iss_position"][u"latitude"]
    print(" ")
    print("The ISS is at longitude {} and latitude {} as of {}.".format(
        longi,
        lat,
        time.ctime(coords[u"timestamp"])))
    return [float(longi), float(lat)]


def draw_iss(coords):
    """Draws the ISS on the map where it is on program run
    and also the dot over Indy with the next time the ISS will
    be over Indy."""
    screen = turtle.Screen()
    screen.register_shape("iss.gif")
    screen.setup(width=720, height=360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    iss_turtle = turtle.Turtle()
    iss_turtle.shape("iss.gif")
    iss_turtle.screen.bgpic("map.gif")
    iss_turtle.screen.title("ISS locator")
    iss_turtle.penup()
    iss_turtle.goto(coords[0], coords[1])
    iss_turtle.pendown()
    iss_over_indy(screen)
    if screen is not None:
        print('Click on screen to exit ...')
        screen.exitonclick()


def iss_over_indy(screen):
    """establishes a dot over Indianapolis with the title
    of the date and time the ISS will next pass over Indy"""
    pass_api = "http://api.open-notify.org/iss-pass.json?"
    kenzie_lat = 39.76
    kenzie_longi = -86.15
    coords = requests.get("{}lat={}&lon={}".format(
        pass_api, kenzie_lat, kenzie_longi))
    coords = coords.json()
    pass_time = time.ctime(coords[u'response'][0]["risetime"])
    kenzie_turtle = turtle.Turtle()
    kenzie_turtle.shape("circle")
    kenzie_turtle.color("yellow", "yellow")
    kenzie_turtle.penup()
    kenzie_turtle.goto(kenzie_longi, kenzie_lat)
    kenzie_turtle.write(pass_time, align=("left"), font=(30))
    kenzie_turtle.penup()


def main():
    get_astronauts()
    coords = get_iss_coordinates()
    draw_iss(coords)


if __name__ == '__main__':
    main()
