from selenium import webdriver
from selenium.webdriver.common.by import By

class RunTestCss():

    def test(self):
        link = "https://letskodeit.teachable.com/p/practice"
        fld_xpath = "//input[@id='name']"
        btm_xpath = "//input[@value='search']"
        ccs_select = "#displayed-text"

        # Instantiate FF Browser Command
        driver = webdriver.Firefox()
        # Open the provided URL
        driver.get(link)

        element = driver.find_elements_by_class_name('btn-style')

        if element is not None:
            print ("Found element: ", len(element))

        element2 = driver.find_element(By.TAG_NAME, "h1")
        if element2 is not None:
            print ("Found element2: ", element2)

        driver.close()



ff = RunTestCss()
ff.test()
