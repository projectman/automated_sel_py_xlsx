from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from XlsxTest import XlsxTest as ResXlsx


class RunTestSafari():

    def __init__(self):

        self.data = ResXlsx().found_row()
        print ("found data", self.data)

    def test(self):

        link = self.data[2]
        fld_xpath = self.data[3]
        fld_text_rt = self.data[4]
        # fld_text_rt = "dsldjfal;gh"   # NOT FOUND
        btm_xpath = self.data[5]
        no_text = self.data[6]

        driver = webdriver.Safari()
        driver.get(link)


        element = driver.find_element_by_xpath(fld_xpath)
        element.clear()
        element.send_keys(fld_text_rt)
        # print ("found element: ", element.tag_name )
        driver.find_element_by_xpath(btm_xpath).click()

        time.sleep(3)
        if fld_text_rt not in driver.page_source:
            print ("Text '", fld_text_rt, "' haven't found on page!")


        print (driver.title)
        print ("Test passed")
        #driver.quit()


# ff = res_xlsx()
# ff = XlsxTest()
#print("result ff: ", ff.found_row())

ff = RunTestSafari()

ff.test()