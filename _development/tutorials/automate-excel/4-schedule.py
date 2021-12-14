""" -------------------------------------------------------------------------------------------------
    Schedule Excel Automation
    -------------------------------------------------------------------------------------------------
    
    Source:  https://github.com/d-insight/code-bank.git
    License: MIT License - https://opensource.org/licenses/MIT 
    
    -------------------------------------------------------------------------------------------------

"""
import shutil
import os
import pandas as pd
import openpyxl 
import schedule
import time


def job():

	#Get List of all processed files in the past
	processed_files = [file for file in os.listdir('data/ProcessedData/') if file.endswith('.xlsx')]
	processed_path = os.path.join(os.getcwd(),'data/ProcessedData/',''.join(processed_files))

	#Check if any new files appeared in drop folder
	dropped_files = [file for file in os.listdir('data/NewData/') if file.endswith('.xlsx')]
	drop_path = os.path.join(os.getcwd(),'data/NewData/',''.join(dropped_files))

	#if there is a new file lets load it to a dataframe and prepare it to write
	if dropped_files:
		df=pd.read_excel(drop_path, usecols= ['Month', 'Dept', 'Sales'])

		#Find the current number of entries in the main file
		df_main=pd.read_excel('data/main.xlsx', sheet_name="Sheet1",usecols= ['Month', 'Dept', 'Sales'])
		current_rows=df_main.shape[0]

		#Load the main workbook
		workbook_name = 'data/main.xlsx'
		wb = openpyxl.load_workbook(workbook_name)
		page=wb['Sheet1']
		#page = wb.active         # Would have opened the last sheet that I used

		#Write new entries to the main workbook
		new_etries = df.values.tolist()
		for i in new_etries:
			page.append(i)
		wb.save(filename=workbook_name)
		df_main_new=pd.read_excel('data/main.xlsx', sheet_name="Sheet1", usecols= ['Month', 'Dept', 'Sales'])
		new_rows=df_main_new.shape[0]

		#Check to see if old rows+appended rows = total new rows in updated excel

		if new_rows == current_rows+df.shape[0]:
			shutil.move(drop_path, os.path.join(os.getcwd(),'data/ProcessedData/'))
		print('All Files Processed. Completed')

	else:
		print('No New Files')


#job()
schedule.every().day.at("17:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute