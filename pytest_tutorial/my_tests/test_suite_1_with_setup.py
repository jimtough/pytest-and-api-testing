import pytest

# mark every test method in this module as 'be' and 'slow'
pytestmark = [pytest.mark.be, pytest.mark.slow]


# setting 'module' scope will make pytest only execute this method once
@pytest.fixture(scope="module")
def my_setup():
    print("")
    print(">>>> MY SETUP <<<<")


@pytest.mark.smoke
@pytest.mark.xx
# notice how the fixture function needs to be passed
# to the test function as a parameter
def test_login_page_valid_user(my_setup):
    print("")
    print("Logging in with valid user...")
    print("Function: xxxxxxxx")


@pytest.mark.regression
def test_login_page_wrong_password(my_setup):
    print("")
    print("Logging in with incorrect password..")
    print("Function: yyyyyyyy")
    # assert 1 == 2, "one is not equal to two"
