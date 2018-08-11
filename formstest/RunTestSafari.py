from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from XlsxTest import XlsxTest

TD_ADJ = 3  # test data adjuster: select only tet data from ID, name, web-link
D_SGMNT = 3  # test data represents in 3 segments for eac operation


class RunTestSafari:
    """
    Testing with Safari selenium driver.
    """

    def __init__(self):

        self.data = XlsxTest().found_row()
        print("found data", self.data)
        self.driver = webdriver.Safari()

    def fill_it(self, test_data):
        """
        Execute finding field and filling this operation.
        """
        # find the field with rXpath fill the text in field
        self.driver.find_element(By.XPATH, test_data[0]).send_keys(test_data[1])
        # debug print("incoming data: ", test_data)

    def click_it(self, test_data):
        """
        Execute finding field and click this operation.
        """
        # find the field with rXpath and click it.
        self.driver.find_element(By.XPATH, test_data[0]).click()
        # debug print("incoming data: ", test_data)

    def find_it(self, test_data):
        """
         Execute finding required text on page.
         If text should be FOUND:YES, the text should be in page_source.
         If text should not be FOUND:NOT, the text should not be on page
        """
        # find the field with rXpath and click it.
        time.sleep(5) # !!! change it to the wait untill ()
        print( "incoming data: ", test_data )

        if test_data[0] == "YES" and test_data[1] in self.driver.page_source:
            print('Text "%s" exists on page.' % test_data[1])
        elif test_data[0] == "NOT" and test_data[1] not in self.driver.page_source:
            print('Text "%s" does not exist on page as it must be.' % test_data[1])
        else:
            print("Some unelectable data in 'find_in' func.")


    def test(self):
        """
        Main testing function.
        :return:
        """
        self.driver.get(self.data[2])
        # find data's range ratio: number of test data
        # cleaned from ID, name, web-link, field for 3 segments
        d_range = int((len(self.data) - TD_ADJ) / D_SGMNT)

        # Test function selector based on operation type
        # Functions operators: FILL, CLICK, FIND
        for indx in range(d_range):
            curr_segment = TD_ADJ + indx * D_SGMNT
            if self.data[curr_segment] == 'FILL':
                self.fill_it(self.data[curr_segment + 1:curr_segment + 3])
            elif self.data[curr_segment] == 'CLICK':
                self.click_it(self.data[curr_segment + 1:curr_segment + 3])
            elif self.data[curr_segment] == 'FIND':
                self.find_it(self.data[curr_segment + 1:curr_segment + 3])
            else:
                print("Not defined operator of action!")

        print("\nTest %s passed" % self.driver.title)
        self.driver.quit()


# ff = res_xlsx()
# ff = XlsxTest()
# print("result ff: ", ff.found_row())

ff = RunTestSafari()

ff.test()
