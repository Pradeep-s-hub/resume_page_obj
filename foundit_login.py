from selenium.webdriver.common.by import By
class FounditLoginPage:
    password_login = "loginWith"
    email_xpath = "//input[@id='signInName']"
    password = "//input[@type='password']"
    submit_button = "//input[@type='submit']"
    profile_path = "View Profile"
    def __init__(self,driver):
        self.driver = driver
    def login_with_password(self):
        self.driver.find_element(By.CLASS_NAME,self.password_login).click()
    def set_email(self,email_address="sompradeep.p@gmail.com"):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email_address)
    def set_password(self,pwd="Pradeep@4163."):
        self.driver.find_element(By.XPATH, self.password).send_keys(pwd)
    def click_login(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()


