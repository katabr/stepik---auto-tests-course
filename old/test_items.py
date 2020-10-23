


from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)





link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"






def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_xpath('//button[text()="Добавить в корзину"]')