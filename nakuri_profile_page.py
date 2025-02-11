from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage:
    res_up = "//input[@type='button' and contains(@value,'Update resume')]"
    success_msg = "//div[@class ='cnt']/p[2]"
    def __init__(self,driver):
        self.driver = driver
    def resume_upload(self):
        self.driver.find_element(By.XPATH, self.res_up).click()
    def get_success_msg(self):
        #time.sleep()
        success_msg_ele = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.success_msg)))
        return success_msg_ele


