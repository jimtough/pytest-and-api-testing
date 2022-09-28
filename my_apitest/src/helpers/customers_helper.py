
from my_apitest.src.utilities.generic_utils import generate_random_email_and_password


class CustomerHelper(object):

    def __init__(self):
        pass

    def create_customer(self, email=None, password=None, **kwargs):
        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = "Password1"
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        # add all the dict key/value pairs from kwargs into the 'payload' dict
        payload.update(kwargs)

        # TODO actually make an API call to create the customer...

        return True
