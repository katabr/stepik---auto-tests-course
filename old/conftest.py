

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=en,
                     help="Choose language: chrome or firefox")


@pytest.fixture(scope="function")
def language(request):
	language = request.config.getoption("language")
    browser = None
    if language == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()



options = Options()
options.add_experimental_option(
    'prefs', {'intl.accept_languages': user_language})
print("\nstart chrome browser for test..")
browser = webdriver.Chrome(options=options)



    self.driver = webdriver.Firefox()

    # открываем браузер
    browser = self.driver
    browser.implicitly_wait(5)
    browser.get("http://localhost:8080/#/")