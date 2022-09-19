import pytest

# mark every test method in this module as 'fe' and 'slow'
pytestmark = [pytest.mark.fe, pytest.mark.slow]


# setting 'module' scope will make pytest only execute this method once
@pytest.fixture(scope="module")
def also_my_setup():
    print("")
    print(">>>> ALSO MY SETUP <<<<")
    return {'id': 20, 'name': 'Meeeee'}


# mark every test method in this class as 'smoke'
@pytest.mark.smoke
@pytest.mark.abc
class TestCheckout(object):

    def test_checkout_as_guest(self, also_my_setup):
        print("checkout as guest")
        print("Class: 111111")
        print("Name: {}".format(also_my_setup.get('name')))

    def test_checkout_with_existing_user(self, also_my_setup):
        print("checkout with existing user")
        print("Class: 2222222222")
        print("Name: {}".format(also_my_setup.get('name')))
