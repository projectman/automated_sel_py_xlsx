"""
Read the text from xlsx file with name ...
on the known sheet

returns:  
1. list includes 1 list of cell's values If chosen ID from range
2. list of rows lists of cell's values if chosen 0

 with data: 1. ID, 2. name of web, 3. link to web.
Then groups by 3 elements ( Operations flag, rHpath, text for text).

ID must be from 1(2nd line) to N(number of webs) with regular counting.

"""

import openpyxl

FILE_NAME = 'webFillExсel.xlsx'
SH_NAME = 'Sheet 1'  # Name of sheet in file.


class XlsxTest:

    # !!! def ___init___ for the self.rows.

    def __init__(self):

        try:
            gen_rows = openpyxl.load_workbook(FILE_NAME)[SH_NAME].rows
        except:
            print('File ', FILE_NAME, ' cannot be opened, are you shure it exists?')
            exit()

        self.rows = []
        for row in gen_rows:
            out_row = []
            for cell in row:
                out_row.append(cell.value)
            self.rows.append(out_row)

    def form_input(self):
        """
        :return: chosen ID by input to chose name
        """
        print("\nYour list of webs for testing: \n")

        # print the names
        for row in self.rows:
            print(row[0], " "*(8-len(str(row[0]))),
                  "|", row[1], " "*(12-len(str(row[1]))),
                  "| ", row[2])

        # Update list of rows with removing headers.
        self.rows = self.rows[1:]
        # input() function
        chosen_id = input("\nPlease enter ID No. of web for testing."
                     "\nor use 0, if you want to test all lines: ")

        return chosen_id

    def check_rows(self):
        """Check the input data for integer and range.
        It returns right integer inputted data only. """
        chosen_id = self.form_input()
        # is ID is integer and in range 0 ... number of rows -1?
        try:
            chosen_id = int(chosen_id)
        except:
            print('\nEntered ID "%s" is not integer.'
                   % chosen_id)
            exit()

        # debub print (self.rows)
        if len(list(self.rows)) < chosen_id or chosen_id < 0:
            print("\nEntered ID out of the possible range of IDs: 0... %d"
                   % (len(list(self.rows))))
            exit()

        return chosen_id

    def find_row(self, chosen_id):
        """
        get chosen ID by input:
        return: list including one list of values, with chosen row by ID data.
        """
        # debug print("chosen_id", chosen_id)

        result_rows = []
        # debug print('find_row self.rows: ', self.rows[1:])
        for row in self.rows:
            # Search the right row with searching ID No.
            if int(row[0]) == chosen_id:
                # debug print("ID of found row: ", row[0], row[1])
                # Create right row found for chosen_id, with values
                result_rows.append(row)

        return result_rows

    def get_row(self):
        """
        print list of web sites by ID | name | web address
        :return: list of rows with chosen ID: 1 row or all rows.
        """

        chosen_id = self.check_rows()
        # Debug print('chosen_id', chosen_id)

        # check all or 1 row was chosen.
        if chosen_id == 0:
            return self.rows
        else:  # should be from 1 to Number of webs.
            return self.find_row(chosen_id)

        # debug print("\n right_row out: ", right_row)


#  ff = XlsxTest()
#  print('Result: ', ff.get_row())
