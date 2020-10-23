import pytest
import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


def test_guest_should_see_basket_button(browser):

    selector = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert selector , "Button 'Add to basket' is absent."
