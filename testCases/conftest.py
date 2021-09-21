import pytest

from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser =='chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    elif browser =='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Rasoun'














