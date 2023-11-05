import pytest
@pytest.fixture(scope='module')
def setup():
    print("starting the server")

    yield                         '''here yield acts like a teardown function'''
    print("ending the server")

@pytest.fixture(scope='function')
def setup2():
    print("starting the programme")

    yield
    print("ending the programme")

def test_login(setup,setup2):              #can call those 2 functions or even call a single function
    print("Tests are working fine")



def test_demo(setup,setup2):
    print("M vinay Kumar IAS ")
