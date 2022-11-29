import datetime
import pytest
from library.config import Config
from library.exel_lib import ReadExcel
from POM.facebook_profile import Facebookprofile


class Testfacebookprofile:
    read_xl = ReadExcel()
    data = read_xl.read_testdata()

    def test_datas(self):
        print(self.data)

    @pytest.mark.parametrize('username,pwd,status', data)
    def test_registration(self, init_driver, username, pwd,status):
        driver = init_driver
        # try:

        fb = Facebookprofile(driver)
        fb.user_name(username)
        fb.pass_word(pwd)
        fb.login()
        fb.profile_icon()
        fb.click_edit_profile()
        fb.edit()
        fb.select_profile_picture()
        fb.save_profile_picture()
        fb.edit_profile()
        fb.edit_cover_photo()
        fb.back_cover_photo()
        fb.add_bio()
        fb.describe(status)
        fb.back_bio()
        fb.customise_details()
        fb.back_details()
        fb.add_Hobbies()
        fb.back_hobbies()
        fb.add_features()
        fb.back_features()
        fb.back_to_profile()
        fb.add_to_story()
        fb.back_story()
        fb.profile()
        fb.log_out()



