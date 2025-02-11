from selenium.webdriver.common.by import By
class UploadResume:
    upload_path = "//input[@id='inline-resume']"
    def __init__(self,driver):
        self.driver = driver
    def resume_upload(self,input_path):
        self.driver.find_element(By.XPATH, self.upload_path ).send_keys(input_path)