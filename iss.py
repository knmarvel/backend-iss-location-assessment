#!/usr/bin/env python
import requests

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
    print(" ")
    print("The ISS is at longitude {} and latitude {} as of {}.".format(
        coords[u"iss_position"][u"longitude"],
        coords[u"iss_position"][u"latitude"],
        coords[u"timestamp"]))


def main():
    get_astronauts()
    get_iss_coordinates()


if __name__ == '__main__':
    main()
