import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


class Test_Home(BaseTest):
    def test_registration_link_visible(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_registration_link_visible()
        assert flag

    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE