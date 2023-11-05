import pytest

'''use -k testname to use markers for running ine function here'''
'''examples-> "pytest test_markers.py -s -v -k signup"   '''


'''use -k nottestname to run all test except the no tagged function'''

'''markers: here we need to use -m instead of -k'''

@pytest.mark.regression
def test_signup():
    print("signup test successful")

@pytest.mark.sanity
def test_login():
    print("login test successful")

@pytest.mark.regression
def test_mobile():
    print("mobile signup successful")

@pytest.mark.skip
def test_skip():
    print("skip this test")

