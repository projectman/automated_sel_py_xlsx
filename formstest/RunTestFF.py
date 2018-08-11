from selenium import webdriver
from selenium.webdriver.common.by import By

class RunFFTests():

    def test(self):
        link = "https://letskodeit.teachable.com/p/practice"
        fld_xpath = "//form[@name='frm_search']/input[@name='s']"
        fld_text = "christmas tree"
        btm_xpath = "//input[@value='search']"

        # Instantiate FF Browser Command
        driver = webdriver.Firefox()
        # Open the provided URL
        driver.get(link)

        elementXpath = driver.find_element((By.name, "name"))
        if elementXpath is not None:
            print ("We found elemement by Xpath: ", fld_text)

        element = driver.find_element_by_xpath(fld_xpath)
        element.clear()
        element.send_keys(fld_text)
        print("found element: ", element.tag_name)
        driver.find_element_by_xpath(btm_xpath).click()

ff = RunFFTests()
ff.test()
