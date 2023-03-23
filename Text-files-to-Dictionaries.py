#! /usr/bin/env python3
import os
import requests


directoryTXT = '/data/feedback/'
files = os.listdir(directoryTXT)
URL = 'http://35.238.163.206/feedback/'

for file in files:
  file_obj = open(os.path.join(directoryTXT, file), 'r')

  lines = [ line.replace('\n', '') for line in file_obj ]

  feedback_dict = { "title": lines[0], "name": lines[1], "date": lines[2], 
"feedback": lines[3] }

  res = requests.post(URL, data=feedback_dict)

  if not res.status_code == 201:
    print('Something went wrong')

  file_obj.close()

