from cookie_parser import cookie_parser  as parser
from request import makeRequest
from soup import linkextract
from request import makeRequestLink 
from soup import verificationlinkSaver
from createExcel import createExcel
import json
import math
num=int(input('How many certificates you have: '))
count=math.ceil(num/10)
cookie=input("Enter your Coursera Cookie:")
print("Process starting....\n")
parsed_cookie=parser(cookie)

for i in range(0,(count*10)+1,10):

    response=makeRequest(i,parsed_cookie)
    print(response)
    linkextract(json.loads(response))
#Verification link extract
print("Certificates' names and target_urls saved ")
print("Verification links' saving is starting.....")
with open('target_urls.txt','r') as file:
   for target in file.read().split():
    response = makeRequestLink(target)
    context=json.loads(response)
    verificationlinkSaver(context)
print("Verification links saved")
print("Generating Excel file ....")
createExcel()
print("Excel file created succesfully!!!")

