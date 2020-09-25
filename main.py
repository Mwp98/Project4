import requests
import datetime
import re
import os.path
from os import path
list = []
Z = 0
K = 0
Oct_24_94_requests = 0
week_requests = 0
month_requests = 0
errors = 0
redirect = 0
files = {}

return_code = 0
if path.isfile('http_access_log.txt') == False:
  url='https://s3.amazonaws.com/tcmg476/http_access_log'
  r = requests.get(url, allow_redirects=True)
  open ('http_access_log.txt','wb').write(r.content)
  print('downloading file')


else:
 print ('File Log has already been downloaded')
 
  
logfile = open('http_access_log.txt', 'r')

print("Accessing Lines...:")
for line in open('http_access_log.txt'):
    
    regex = re.compile(r".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+? ) (HTTP.*\"|\") ([2-5]0[0-9]) .*")
    elements = regex.split(line)
return_code = elements[5]    
print("The total number of requests made each day were:")    
for line in open('http_access_log.txt'):
     if "24/Oct/1994" in line:
      Oct_24_94_requests += 1
     print(Oct_24_94_requests)
    
print("The total number of requests made each week were:")  
for line in open('http_access_log.txt'):
     if "24/Oct/1994" or "25/Oct/1994" or "26/Oct/1994" or "27/Oct/1994" or "28/Oct/1994" or "29/Oct/1994" or "30/Oct/1994" or "31/Oct/1994 " in line:
      week_requests += 1
     print(week_requests)
print("The total number of requests made each month were:") 
for line in open('http_access_log.txt'):
     if "/Oct/1994" in line:
      month_requests += 1
     print(month_requests)
print("The percentage of requests that failed were:") 
for line in open('http_access_log.txt'):
     if int(return_code) >= 400 and int(return_code) <= 499:
      errors += 1
     print(errors)
print("The percentage of requests that redirected were:") 
for line in open('http_access_log.txt'):
     if int(return_code) >= 300 and int(return_code) <= 399:
      redirect += 1
     print(redirect)
filename = elements[4]
for line in open('http_access_log.txt'):

     if filename in files:
   
      files[filename] += 1

     else:
      files[filename] = 1
print("The most requested file was:", sorted(files, key = files.get, reverse = True)[:1])
print("The least requested file was:", sorted(files, key = files.get, reverse = False)[:1])

print("Breaking Files...") 