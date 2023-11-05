import pytest


def get_data():
    return [

        ("vinaykumar.com", "IAS"),
        ("bablu.com", "IPS"),
        ("judefelix.com", "IFS")

    ]


@pytest.mark.parametrize("username,password", get_data())
def test_signup(username, password):
    print(username, "---", password)
