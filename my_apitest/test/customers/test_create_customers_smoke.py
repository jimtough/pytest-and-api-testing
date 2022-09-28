import pytest
import logging as logger


# instructor wants to name this "test case id 29" for some reason. Why 29?? whatever...
@pytest.mark.tcid29
def test_create_customer_only_email_and_password():

    logger.info("TEST: Create new customer with email and password only.")
    email = ""
    password = ""

    # create payload

    # make the call

    # verify status code

    # verify email in the response

    # verify customer is created in database
