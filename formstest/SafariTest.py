from selenium import webdriver
import time

url = 'https://google.com'

class SafariTest:


    def TestIt(self):

        driver = webdriver.Safari()
        driver.get(url)
        driver.implicitly_wait(10)
        # print(help(driver))

        el1 = driver.find_element_by_xpath("//input[@id='lst-ib']")
        el1.send_keys("What is the weather in Dallas today?")
        el1.submit()

        time.sleep(7)




ff = SafariTest()
ff.TestIt()