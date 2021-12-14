""" -------------------------------------------------------------------------------------------------
    Get Value from Excel
    -------------------------------------------------------------------------------------------------
    
    Source:  https://github.com/d-insight/code-bank.git
    License: MIT License - https://opensource.org/licenses/MIT 
    
    -------------------------------------------------------------------------------------------------

"""

#pip3 install openpyxl
import openpyxl

#specify the files location (or path)
DIR = 'data/'
excel_files = [DIR + 'SampleData.xlsx', DIR + 'SampleData2.xlsx']

#create an empty list to append values later on
values = []

#loop through the files in the "excel_files" list
for file in excel_files:
    workbook = openpyxl.load_workbook(file)
    #specify worksheet to select
    worksheet = workbook['SalesOrders']
    #locate cell and get its value
    cell_value = worksheet['G11'].value
    #append value to "values" list
    values.append(cell_value)

    #print totals
    print(cell_value)
