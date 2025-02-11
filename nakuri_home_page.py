from selenium.webdriver.common.by import By
class Home:
    login_link = "Login"
    def __init__(self,driver):
        self.driver = driver
    def go_to_login(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link).click()

