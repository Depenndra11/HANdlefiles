import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):

    if browser=="chrome":
        driver = webdriver.Chrome(executable_path="E:\\Browsers\\chromedriver.exe")
        print("launch chrome browser---")

    else:
        print("launch firefox browser---")
        driver= webdriver.Firefox(executable_path="E:\\Browsers\\geckodriver.exe")
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")




# # html report
# #hook for adding enviornmet
# def pytest_configure(config):
#     config._metadata['project Name'] = '0rangeHrm'
#     config._metadata['Module Name'] = 'Coustomers'
#     config._metadata['Tester Name'] = 'Dependra Singh'
# # #
# # # #hook for remove information
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("java home", None)

#
