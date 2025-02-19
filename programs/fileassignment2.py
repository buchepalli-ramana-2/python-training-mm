'''
write a program to display the total count of men and women:

Total male count : xxxx
Total female count : xxx
'''
'''
import csv
workset = set()
malecount = 0
femalecount = 0
with open("adult.csv") as fobj:
    reader = csv.reader(fobj)  # converting fobj to csv readable format
    for line in reader:
        gender = line[9].strip()
        if gender == "Male":
            malecount+=1
        else:
            femalecount+=1
    print("Total male count :",malecount)
    print("TOtal female count:",femalecount)
'''
import csv
malecount = 0
femalecount = 0
with open("adult.csv", "r") as fobj:
    reader = csv.reader(fobj) # Converting file object as readable format
    #print(reader)
    for line in reader:
        gender = line[9].strip()
        if gender == "Male":
            malecount += 1
        elif gender == "Female":
            femalecount += 1

print("male count:", malecount)
print("female count:",femalecount)

