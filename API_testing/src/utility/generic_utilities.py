import logging as logger
from random import randrange
import string
import random


def generate_random_email(domain=None, email_prefix=None):

    logger.debug("Generating random email")
    if not domain:
        domain = 'gmail.com'
    if not email_prefix:
        email_prefix = 'test_user'
    random_string = ''.join(random.choices(string.ascii_lowercase, k=randrange(5, 11)))
    email = email_prefix + '_' + random_string + '@' + domain
    logger.debug("Random email is successfully generated")
    return email


def create_random_product_json():

    name = ''.join(random.choices(string.ascii_lowercase, k=5))
    desc = ''.join(random.choices(string.ascii_lowercase, k=10))
    price = str(float(random.choice(range(10, 1000))))
    json_body = dict()
    json_body['name'] = name
    json_body['description'] = desc
    json_body['regular_price'] = price
    return json_body