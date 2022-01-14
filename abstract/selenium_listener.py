from selenium.webdriver.support.events import AbstractEventListener

from base.seleniumbase import SeleniumBase


class MyListener(AbstractEventListener):

    def before_click(self, element, driver):
        '''Deleting a cookie ak_bmsc before a click'''
        SeleniumBase(driver).delete_cookie('ak_bmsc')

    def after_click(self, element, driver):
        '''Deleting a cookie ak_bmsc after a click'''
        SeleniumBase(driver).delete_cookie('ak_bmsc')
