""" -------------------------------------------------------------------------------------------------
    Merge Value from Excel
    -------------------------------------------------------------------------------------------------
    
    Source:  https://github.com/d-insight/code-bank.git
    License: MIT License - https://opensource.org/licenses/MIT 
    
    -------------------------------------------------------------------------------------------------

"""
#pip3 install pandas
import pandas as pd

#specify the files location (or path)
#excel_files = ['files path here']
DIR = 'data/'
excel_files = [DIR + 'SampleData.xlsx', DIR + 'SampleData2.xlsx']

#create a blank dataframe
merge = pd.DataFrame()

#loop through every file in the list
for file in excel_files:
  #read files into a dataframe and skip the first row (header)
  df = pd.read_excel(file, skiprows = 1)
  #append results to merge
  merge = merge.append(df, ignore_index = True)

#create final workbook with merged results
merge.to_excel(DIR + 'Merged_Files.xlsx')
