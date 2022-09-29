import pytest
import logging as logger

from my_apitest.src.utilities.generic_utils import generate_random_email_and_password
from my_apitest.src.helpers.customers_helper import CustomerHelper
from my_apitest.src.dao.customers_dao import CustomersDAO


# instructor wants to name this "test case id 29" for some reason. Why 29?? whatever...
@pytest.mark.tcid29
def test_create_customer_only_email_and_password():

    logger.info("TEST: Create new customer with email and password only.")
    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']
    logger.debug("generated test values | email: [%s] | password: [%s]", email, password)

    # make the call
    customer_helper = CustomerHelper()
    cust_api_info = customer_helper.create_customer(email=email, password=password)

    # verify email in the response
    assert cust_api_info['email'] == email, \
        f"Create customer API returned wrong email | expected: {email} | returned: {cust_api_info['email']}"
    assert cust_api_info['first_name'] == "", \
        f"Create customer API returned value for 'first_name', but it should be empty"

    # verify customer is created in database
    customer_dao = CustomersDAO()
    customer_info = customer_dao.get_customer_by_email(email)
    customer_id_in_api_response = cust_api_info['id']
    customer_id_in_database = customer_info[0]['ID']
    assert customer_id_in_api_response == customer_id_in_database, \
        f"Customer id in API response does not match id in database" \
        f" | API: {customer_id_in_api_response} | DB: [{customer_id_in_database}]"
