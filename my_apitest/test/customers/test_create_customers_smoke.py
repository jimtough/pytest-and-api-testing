import pytest
import logging as logger

from my_apitest.src.utilities.generic_utils import generate_random_email_and_password


# instructor wants to name this "test case id 29" for some reason. Why 29?? whatever...
@pytest.mark.tcid29
def test_create_customer_only_email_and_password():

    logger.info("TEST: Create new customer with email and password only.")
    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']
    logger.debug("generated test values | email: [%s] | password: [%s]", email, password)

    # create payload
    payload = {'email': email, 'password': password}

    # make the call

    # verify status code

    # verify email in the response

    # verify customer is created in database
