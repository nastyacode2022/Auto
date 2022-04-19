import os
import logging as logger


class CredentialsUtility:

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')
        if wc_key is None or wc_secret is None:
            raise Exception("The API credentials 'WC_KEY' or 'WC_SECRET' must be in env variable")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():

        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        if db_user is None or db_password is None:
            raise Exception("The DB credentials 'DB_USER' or 'DB_PASSWORD' must be in env variable")
        else:
            return {'db_user': db_user, 'db_password': db_password}
