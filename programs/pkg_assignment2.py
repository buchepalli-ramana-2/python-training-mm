'''
write a script to perform the below operations :

1. display current working directory
2. display login name
3. display all environment variables
4. display today's date ( timestamp )
5. display sep months calendar
6. display all .py files and its size in bytes
7. display the modified time of employees.csv file
8. display current process id
9. set an environment variables. ( Eg.    TEST_PATH = "C:/Users/Admin/")
10. Lock and unlock a file using os.open and os.close
11. Retrieve the current system's load average.
12. display python version
'''
import os
from datetime import date

# print current directory
print("Current directory",os.getcwd())

#print login name
print("currently lgoin user: ",os.getlogin())

#display all environment variables
print("environment variables: ",os.environ)

#display today's date
print("Date is:", date.today())

#display particular month's calendar
import calendar
print("Month calendar", calendar.month(2025,9))

#display all .py files and each size
import pathlib
files = {}

for fl in os.listdir():
    if os.path.isfile(fl):
        if pathlib.Path(fl).suffix == ".py":
            files[fl] = os.path.getsize(fl)
            
for file, size in files.items():
    print(f"{file} {size} bytes")

# get the modified time of particular file
import time
m_time = time.gmtime(os.path.getmtime("listdemo.py"))
print("File modification time",time.strftime('%Y-%m-%dT%H:%M:%SZ', m_time))
# print(os.stat_result(m_time))

#Get the current porocess id
# import psutil
# print("Current pid: ",os.getpid())
# psutil.Process(os.getpid())
# prss_name = psutil.process(os.getpid()).name
# print(os.getpid() ,":", prss_name)
# os.

#Set environmental variables 
os.environ["test_path"] = "C:\\Users\\Admin"
print(os.environ.get("test_path"))

#Lock and unlock a file using os.open and os.close

