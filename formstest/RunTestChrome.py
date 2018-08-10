from selenium import webdriver
import os



class RunTestSafari():
    # http://chromedriver.storage.googleapis.com/index.html
    link = "https://letskodeit.teachable.com/p/practice"

    def test(self):
        driverLocation = "/usr/local/bin/chromedriver"
        #os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(executable_path=driverLocation)
        # Open the provided URL
        driver.get(link)

ff = RunTestSafari()
ff.test()