#!/usr/bin/python3
""" Module containing the city class """


from models.base_model import BaseModel


class City(BaseModel):
    """ Class representing a city """
    state_id = ""
    name = ""
