from selenium.webdriver.common.by import By
class LoginPage:
    email_xpath = "//input[@type='text' and contains(@placeholder,'Email')]"
    password = "//input[@type='password']"
    login_button = "//button[@type='submit' and text()='Login']"
    profile_path = "//div[@class='view-profile-wrapper']/a"
    def __init__(self,driver):
        self.driver = driver

    def set_email(self,email_address="sompradeep.p@gmail.com"):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email_address)
    def set_password(self,pwd="Pradeep@4163."):
        self.driver.find_element(By.XPATH, self.password).send_keys(pwd)
    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def go_to_view_profile(self):
        self.driver.find_element(By.XPATH, self.profile_path).click()


