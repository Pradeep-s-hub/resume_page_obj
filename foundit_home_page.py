from selenium.webdriver.common.by import By
class founditHome:
    go_toProfile_link = "View Profile"
    profile_list_xpath = "//img[@class='rounded-full']"
    def __init__(self,driver):
        self.driver = driver
    def profile_list_view(self):
        self.driver.find_element(By.XPATH, self.profile_list_xpath).click()
    def go_to_Profile(self):
        self.driver.find_element(By.LINK_TEXT, self.go_toProfile_link).click()

