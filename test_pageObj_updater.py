import pytest
from time import sleep
from pynput.keyboard import Controller,Key
from nakuri_home_page import Home
from nakuri_login_object import LoginPage
from nakuri_profile_page import ProfilePage
from foundit_open_page import OpenPage
from foundit_login import FounditLoginPage
from foundit_home_page import founditHome
from foundit_resumeUpload_page import UploadResume


class TestResumeUpload:
    @pytest.mark.nakuri
    # pytest -v -s test_pytest_file_upload_fixtures_modules.py -m nakuri
    # @pytest.mark.run(order=1)
    @pytest.mark.second
    @pytest.mark.parametrize('email,password,resume_path',[("sompradeep.p@gmail.com","Pradeep@4163.","D:\\job\\2_10_years\\sele\\latest\\sompradeep_p_resume.pdf"),("sompradeep.p@gmail.com","Pradeep@4163.","D:\\job\\2_10_years\\sele\\resume_pradeep_p.pdf")])
    def test_nakuri(self,setup,email,password,resume_path):
        self.driver = setup
        self.driver.get("https://www.naukri.com/")
        home_page = Home(self.driver)
        home_page.go_to_login()

        login_obj=LoginPage(self.driver)
        login_obj.set_email()
        login_obj.set_password()
        login_obj.click_login()
        login_obj.go_to_view_profile()

        profile_obj = ProfilePage(self.driver)
        profile_obj.resume_upload()


        sleep(5)
        keyboard = Controller()
        keyboard.type(resume_path)
        sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(5)

        sucess_msg_ele = profile_obj.get_success_msg()
        assert sucess_msg_ele.text == "Resume has been successfully uploaded.", "Resume not uploaded"
        print("File uploaded successfully...")
        sleep(2)
        self.driver.close()



    @pytest.mark.foundit
    # pytest -v -s test_pytest_file_upload_fixtures_modules.py -m foundit
    @pytest.mark.first
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize('email,password,drive_path', [("sompradeep.p@gmail.com", "Pradeep@4163.","D:\\job\\2_10_years\\sele\\latest\\sompradeep_p_resume.pdf")])
    def test_foundit(self,setup,email,password,drive_path):
        self.driver = setup
        self.driver.get("https://www.foundit.in/")
        open_page = OpenPage(self.driver)
        open_page.go_to_login()
        found_it_login = FounditLoginPage(self.driver)
        found_it_login.login_with_password()
        found_it_login.set_email(email)
        found_it_login.set_password(password)
        found_it_login.click_login()
        home_page_obj = founditHome(self.driver)
        home_page_obj.profile_list_view()
        home_page_obj.go_to_Profile()
        resume_page = UploadResume(self.driver)
        resume_page.resume_upload(drive_path)
        self.driver.close()
