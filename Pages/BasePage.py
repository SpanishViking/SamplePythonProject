from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Parent class of all pages
# Contains generic methods and utils for all pages

class BasePage:
    # By locators
    EMAIL = (By.XPATH, "//input[@name='username']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    REGISTRATION_LINK = (By.LINK_TEXT, "Register")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")
    HOMEPAGE_BUTTON = (By.LINK_TEXT, "home")
    ABOUT_BUTTON = (By.LINK_TEXT, "about")
    CONTACT_BUTTON = (By.LINK_TEXT, "contact")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Page actions/methods
    # Click utility
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

        # Send keys utility
    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # Get element text utility
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    # Is element visible utility
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # Get title utility
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    # Used to check if registration link is visible
    def is_registration_link_visible(self):
        return self.is_visible(self.REGISTRATION_LINK)

    # Used to log in to system
    def login(self, username, password):
        self.send_keys(self.EMAIL, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    # Used to click the home button
    def click_home_button(self):
        self.click(self.HOMEPAGE_BUTTON)

    # Used to click the about button
    def click_about_button(self):
        self.click(self.ABOUT_BUTTON)

    # Used to click the contact button
    def click_contact_button(self):
        self.click(self.CONTACT_BUTTON)