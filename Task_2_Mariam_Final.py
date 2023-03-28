#!/usr/bin/env python3

#All files are in same dirctory 

import os
import csv
import json
import pandas as pd
import time
import argparse

print("Hello to Task 2 - Mariam Mamdouh - DM ") 
print("This script will convert a JSON file to CSV")

parser = argparse.ArgumentParser()
parser.add_argument("path", help ="Please enter the json file path:")
parser.add_argument("-u", action="store_true", dest="json", default=False, help="Please use json path.")


args = parser.parse_args()


if args.json: 

	start_time = time.time()
	
	records = [json.loads(line) for line in open(args.path)]
	df=pd.DataFrame(records)
	print("JSON file is loaded to a DataFrame.")
	col_df = ['tz','r','u','a','ll','cy','t','hc']
	df=df[col_df]
	df.rename(columns = {'a':'web_browser2', 
							'r':'from_url',
							'u':'to_url',
							'tz':'Time_Zone',
							'll':'longitude_latitude',
							'cy':'City',
							't':'time_in',
							'hc':'time_out'}, inplace = True)

	#Modifing Data
	
	df['City'] = df['City'].replace('','NA')
	df=df.replace('NaN','NA')
	
	df["Time_Zone"].fillna("NA", inplace = True) 
	df["longitude_latitude"].fillna("NA", inplace = True) 
	#Functions to crop operating_sys and web_browser
	
	def operating_dis(x):
		if 'Windows' in x:
			x='Windows'
			return x
		elif 'Macintosh' in x:
			x='Macintosh'
			return x
		else :
			x='Ubuntu'
			return x
		
	def web_dis(x):
		if 'Safari' and 'Chrome' in x:
			x='Safari,Chrome'
			return x
		elif 'Chrome' in x:
			x='Chrome'
			return x
		elif 'Firefox' in x  :
			x='Firefox'
			return x
		elif 'Presto' in x:
			x='Presto'
			return x
		elif 'Safari' in x  :
			x='Safari'
			return x
		else:
			x='NA'
			return x
		
	df['from_url'].replace('http://', '', regex=True, inplace=True)
	df['from_url'].replace("(/).*","", regex=True , inplace=True)
	
	df['operating_sys']=df.web_browser2.apply(operating_dis)
	df['web_browser']=df.web_browser2.apply(web_dis)
	
	df['longitude_latitude']=df['longitude_latitude'].astype(str)
	
	df=df.loc[:, ~df.columns.isin(['Country','web_browser2'])]
	
	dfcol=['web_browser','operating_sys','from_url','to_url','City','longitude_latitude','Time_Zone','time_in','time_out']
	df=df[dfcol]
	
	file_name=input('Please enter the name of csv file: ')
	
	file_name='jason_csv_converted'+'.csv'
	
	df.to_csv(file_name, index=False)
	
	with open(file_name, 'r') as fp:
		for count, line in enumerate(fp):
			pass
	countcsv=count
	
	#Print a message after converting each file with the number of rows transformed and the path of this file

	print("File Name Converted:", file_name)
	print('Total number of rows transferred:', countcsv)
	print('The Path of the file is : ', os.getcwd())
	
	#read the csv file 
	dfinal = pd.read_csv(file_name)
	
	#remove Null Values 
	
	dfinal=dfinal.replace('NaN','NA')
	dfinal["Time_Zone"].fillna("NA", inplace = True) 
	dfinal["longitude_latitude"].fillna("NA", inplace = True) 
	dfinal["City"].fillna("NA", inplace = True) 
	dfinal["web_browser"].fillna("NA", inplace = True) 
		
	print(dfinal)
	
	#Print the total excution time.
	print("Total excution time: %s" %(time.time() - start_time))
	
else:
	records = [json.loads(line) for line in open(args.path)]
	df=pd.DataFrame(records)
	print("JSON file is loaded to a DataFrame.")
	col_df = ['tz','r','u','a','ll','cy','t','hc']
	df=df[col_df]
	df.rename(columns = {'a':'web_browser2', 
							'r':'from_url',
							'u':'to_url',
							'tz':'Time_Zone',
							'll':'longitude_latitude',
							'cy':'City',
							't':'time_in',
							'hc':'time_out'}, inplace = True)
	
	#Modifing Data
	
	df['City'] = df['City'].replace('','NA')
	df=df.replace('NaN','NA')
	
	df["Time_Zone"].fillna("NA", inplace = True) 
	df["longitude_latitude"].fillna("NA", inplace = True) 
	#Functions to crop operating_sys and web_browser
	
	def operating_dis(x):
		if 'Windows' in x:
			x='Windows'
			return x
		elif 'Macintosh' in x:
			x='Macintosh'
			return x
		else :
			x='Ubuntu'
			return x
		
	def web_dis(x):
		if 'Safari' and 'Chrome' in x:
			x='Safari,Chrome'
			return x
		elif 'Chrome' in x:
			x='Chrome'
			return x
		elif 'Firefox' in x  :
			x='Firefox'
			return x
		elif 'Presto' in x:
			x='Presto'
			return x
		elif 'Safari' in x  :
			x='Safari'
			return x
		else:
			x='NA'
			return x
		
	df['from_url'].replace('http://', '', regex=True, inplace=True)
	df['from_url'].replace("(/).*","", regex=True , inplace=True)
	
	df['operating_sys']=df.web_browser2.apply(operating_dis)
	df['web_browser']=df.web_browser2.apply(web_dis)
	
	df['longitude_latitude']=df['longitude_latitude'].astype(str)
	
	df=df.loc[:, ~df.columns.isin(['Country','web_browser2'])]
	
	dfcol=['web_browser','operating_sys','from_url','to_url','City','longitude_latitude','Time_Zone','time_in','time_out']
	df=df[dfcol]
	
	
	file_name=input('Please enter the name of csv file: ')
	
	file_name=file_name+'.csv'
	
	df.to_csv(file_name, index=False)
	
	with open(file_name, 'r') as fp:
		for count, line in enumerate(fp):
			pass
	countcsv=count
	
	#Print a message after converting each file with the number of rows transformed and the path of this file
	
	print("File Name Converted:", file_name)
	print('Total number of rows transferred:', countcsv)
	print('The Path of the file is : ', os.getcwd())
	
	#read the csv file 
	dfinal = pd.read_csv(file_name)
	
	#remove Null Values 
	
	dfinal=dfinal.replace('NaN','NA')
	dfinal["Time_Zone"].fillna("NA", inplace = True) 
	dfinal["longitude_latitude"].fillna("NA", inplace = True) 
	dfinal["City"].fillna("NA", inplace = True) 
	dfinal["web_browser"].fillna("NA", inplace = True) 
	
	print(dfinal)
	
	#Print the total excution time.
	print("Total excution time: %s" %(time.time() - start_time))
	
	