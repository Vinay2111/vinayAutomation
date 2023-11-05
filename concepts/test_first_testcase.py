import pytest

'''in order to avoid writing the same print statment in every test cases, we can use a concept called as "fixtures" like shown below '''
'''these fixtures can be setup at function level as well as module level'''

'''module level'''
def setup_module(module):
    print("starting the server")

def teardown_module(module):
    print("ending the server")


'''below code is for function level'''
def setup_function(function): #setup_function is used to print some texts before starting the test
    print("launching app")

def teardown_function(function): #teardown_function is used to print some texts before ending the test
    print("app closed successfully")
def test_login():
    #print("launching app")
    print("Login successful")

def test_demo():
    #print("launching app")
    print("M vinay Kumar IAS ")
