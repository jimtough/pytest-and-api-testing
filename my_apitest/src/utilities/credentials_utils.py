import os


class CredentialsUtils(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception("The API credentials 'WC_KEY' and 'WC_SECRET' must be set as environment variables")
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_database_credentials():
        db_username = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASS')

        if not db_username or not db_password:
            raise Exception("The API credentials 'DB_USER' and 'DB_PASS' must be set as environment variables")
        else:
            return {'db_username': db_username, 'db_password': db_password}

