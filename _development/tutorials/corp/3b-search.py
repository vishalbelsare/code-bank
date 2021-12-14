""" -------------------------------------------------------------------------------------------------
    Search for Value from Excel
    -------------------------------------------------------------------------------------------------
    
    Source:  https://github.com/d-insight/code-bank.git
    License: MIT License - https://opensource.org/licenses/MIT 
    
    -------------------------------------------------------------------------------------------------

"""
#pip3 install pandas
import pandas as pd
#pip3 install numpy
import numpy as np

#specify the files location (or path)
#files = ['files path here']
DIR = 'data/'
excel_files = [DIR + 'SampleData.xlsx', DIR + 'SampleData2.xlsx']

# Which representative sell Pencils?

#loop through the "files" list
for file in excel_files:
    #read each file in a dataframe
    df = pd.read_excel(file)
    #locate the "Item" column and return the "Rep" where the condition matches "Pencil"
    pencil = df['Rep'].where(df['Item'] == 'Pencil').dropna()
    #print file name
    print(file)
    #print filtered results
    print(pencil)
    