from selenium import webdriver

class RunFFTests():

    def test(self):
        link = "https://www.theestatesale.com/site/"
        fld_xpath = "//form[@name='frm_search']/input[@name='s']"
        fld_text = "christmas tree"
        btm_xpath = "//input[@value='search']"

        # Instantiate FF Browser Command
        driver = webdriver.Firefox()
        # Open the provided URL
        driver.get(link)

        elementXpath = driver.find_element_by_xpath(fld_xpath)
        if elementXpath is not None:
            print ("We found elemement by Xpath: ", fld_text)

        element = driver.find_element_by_xpath(fld_xpath)
        element.clear()
        element.send_keys(fld_text)
        print("found element: ", element.tag_name)
        driver.find_element_by_xpath(btm_xpath).click()

        if driver.find_element_by_xpath()

        #driver.quit()

ff = RunFFTests()
ff.test()
