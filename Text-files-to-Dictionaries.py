#! /usr/bin/env python3
import os
import requests


directoryTXT = '/data/feedback/'
files = os.listdir(directoryTXT)

#This is the URL of the website we will the feedbacks to
URL = 'http://35.238.163.206/feedback/'

#Here we are itirating through the text files inside '/data/feedback/' directory
for file in files:
  file_obj = open(os.path.join(directoryTXT, file), 'r')
  lines = [ line.replace('\n', '') for line in file_obj ]
  
#Here we are converting TXT files to add them to a  dictionary
  feedback_dict = { "title": lines[0], "name": lines[1], "date": lines[2], 
"feedback": lines[3] }
  
#Sending a POST request to the website with the new dictionary containing the TXT files we created 
  res = requests.post(URL, data=feedback_dict)
  
#This will generate an error if the POST request was not successful
  if not res.status_code == 201:
    print('Something went wrong')

  file_obj.close()

