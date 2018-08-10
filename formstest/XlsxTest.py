"""
Read the text from xlsx file with name ...
on the known sheet

return list of data: 1. ID, 2. name of web, 3. link to web.
4.... row of data for testing.
"""

import openpyxl

FILE_NAME = 'webFillExсel.xlsx'
SH_NAME = 'Sheet 1'  # Name of sheet in file.


class XlsxTest():

    def gen_rows(self):
        # create object

        rows =[]
        try:
            rows = openpyxl.load_workbook(FILE_NAME)[SH_NAME].rows
        except:
            print('File ', FILE_NAME, ' cannot be opened, are you shure it exists?')
            exit()

        return rows

    def form_input(self):
        """
        :return: chosen ID for chose name
        """
        print("\nYour list of webs for testing: \n")

        # print the names
        for el in self.gen_rows():
            print(el[0].value, "| ", el[1].value, "| ", el[2].value)

        # input() function
        chosen_id = int(input("\nPlease enter ID No. of web for testing: "))

        return chosen_id


    def found_row(self):
        """
        print list of web sites by ID | name | web address
        :return: chosen name of row will be chosen for fillings.
        """

        # chose right line with chosen ID No.
        chosen_id = self.form_input()
        #print("chosen_id", chosen_id)

        right_row = []
        for row in self.gen_rows():

            # Search the right row with searching ID No.
            if row[0].value == chosen_id:
                # print("ID of found row: ", row[1].value, row[2].value)
                # Create right row with values

                for cell in list(row):
                    right_row.append(cell.value)
                break

        #print("\n right_row out: ", right_row)

        return right_row


# found_row()

