#!/usr/bin/python3
""" module containing the review class """


from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
