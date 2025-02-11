from selenium.webdriver.common.by import By
class OpenPage:
    go_tologin = "//div[@class='flex gap-4']/button[1]"

    def __init__(self,driver):
        self.driver = driver

    def go_to_login(self):
        self.driver.find_element(By.XPATH, self.go_tologin).click()
