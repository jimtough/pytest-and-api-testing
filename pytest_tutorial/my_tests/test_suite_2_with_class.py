import pytest

# mark every test method in this module as 'fe' and 'slow'
pytestmark = [pytest.mark.fe, pytest.mark.slow]


# mark every test method in this class as 'smoke'
@pytest.mark.smoke
class TestCheckout(object):

    def test_checkout_as_guest(self):
        print("checkout as guest")
        print("Class: 111111")

    def test_checkout_with_existing_user(self):
        print("checkout with existing user")
        print("Class: 2222222222")
