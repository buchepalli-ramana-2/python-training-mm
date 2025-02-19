# IF the file is not existing ... the file will be created in the current directory
# If the file is already existing... it overrites the existing content

fobj = open("clients.txt","w")

fobj.write("google\n")
fobj.write("microsoft\n")
fobj.write("oracle\n")

for val in range(1,11):
    fobj.write(str(val)  + "\n")


fobj.close()

# pythonic way  # context manager
# what is context manager?
# If any line starts with keyword with ... we call it context manager
# ADvantage: the file gets closed automatically ... it can write or read or append mode.

with open("clientinfo.txt","w") as fobj:
    fobj.write("tcs\n")
    fobj.write("infy\n")
    fobj.write("mm\n")


# method1   - reading the file line by line
# fobj acts like pointer or cursor
with open("clientinfo.txt","r") as fobj:
    for line in fobj:
        print(line.strip())


# method2
import csv
with open("clientinfo.txt","r") as fobj:
    reader = csv.reader(fobj)  # converting file object to csv understandable format
    for line in reader:
        print(line)    # each line is automatically converted to the list



# method3
with open("clientinfo.txt","r") as fobj:
    print(fobj.readlines()) # reading all the lines at once in list form

######################################################
