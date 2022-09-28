
from my_apitest.src.utilities.generic_utils import generate_random_email_and_password
from my_apitest.src.utilities.requests_utils import RequestsUtils


class CustomerHelper(object):

    def __init__(self):
        self.requests_utils = RequestsUtils()

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

        self.requests_utils.post('customers', payload=payload)

        return True
