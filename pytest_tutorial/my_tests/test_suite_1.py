import pytest

# mark every test method in this module as 'fe' and 'slow'
pytestmark = [pytest.mark.fe, pytest.mark.slow]


# mark one test method as 'smoke'
@pytest.mark.smoke
def test_login_page_valid_user():
    print("Logging in with valid user...")
    print("Function: xxxxxxxx")


# mark one test method as 'regression'
@pytest.mark.regression
def test_login_page_wrong_password():
    print("Logging in with incorrect password..")
    print("Function: yyyyyyyy")
    # assert 1 == 2, "one is not equal to two"
