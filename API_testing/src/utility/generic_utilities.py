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

#def choose_element_from_json(search_key,search_value,json):
#    if len(json) > 1:
#        for element in range(len(json)):
#            if json[element][str(search_key)] == search_value:
#                return search_value
#        return None
#    else:
#        if json[str(search_key)] == search_value:
#            return search_value
#        else:
#            return None