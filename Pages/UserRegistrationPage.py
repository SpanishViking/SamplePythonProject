from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class UserRegistrationPage(BasePage):

    # By locators
    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIPCODE = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")
    EMAIL = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.XPATH, "//input[@value='Register']")

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)

    # Used to check the registration page title
    def get_registration_page_title(self, title):
        return self.get_title(title)

    # Used to create a user
    def create_user(self, first_name, last_name, address, city, state, zipcode, phone, ssn, email, password):
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.ADDRESS, address)
        self.send_keys(self.CITY, city)
        self.send_keys(self.STATE, state)
        self.send_keys(self.ZIPCODE, zipcode)
        self.send_keys(self.PHONE, phone)
        self.send_keys(self.SSN, ssn)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.send_keys(self.CONFIRM_PASSWORD, password)
        self.click(self.REGISTER_BUTTON)