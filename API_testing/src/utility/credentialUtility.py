import os

class CredentialsUtility:

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')
        if not wc_key or not wc_secret:
            raise Exception("The API credentials 'WC_KEY' or 'WC_SECRET' must be in env variable")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

