from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    # By locators

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Page actions/methods
    # Used to check the registration page title
    def get_home_page_title(self, title):
        return self.get_title(title)
