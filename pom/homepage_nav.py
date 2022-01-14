from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'
        self.NAV_LINK_TEXT = 'Gifts,Women,Men,Kids & Baby,Beauty,Home,Furniture,Shoes,Jewelry,Handbags & Accessories,Now Trending,Sale'

    def get_nav_links(self) -> List[WebElement]:
        '''Return WebElements for nav links'''
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        '''Return all nav links text. Return format is a String with comma separated values'''
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return ','.join(nav_links_text)

    def get_nav_link_by_name(self, name: str) -> WebElement:
        '''Return a nav link WebElement, the input is a link's name'''
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)
