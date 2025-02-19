'''
Use the file ../csvfiles/adults.csv

write a program to display all the lines from the file to the screen.
######################################################
write a program to display age and workclass columns data only
######################################################
write a program to display all the distinct workclasses

Stage-gov
Private
Self-emp-not-inc
..
..
..
######################################################
'''
#C:\\Users\\Admin\\Desktop\\Python-training-mm\\python-training-mm\\csvfiles\\adult.csv"
import csv

# with open("adult.csv", "r") as adults:
#     for line in adults:
#         print(line)

# with open("adult.csv","r") as adult:
#     print(adult.readlines())
# method1
import csv
workset = set()
with open("adult.csv") as fobj:
    reader = csv.reader(fobj)  # converting fobj to csv readable format
    for line in reader:
        workclass = line[1]
        workset.add(workclass)
    #print(workset)
    for work in workset:
        print(work)


#method2
import csv
worklist = []
with open("adult.csv") as fobj:
    reader = csv.reader(fobj)  # converting fobj to csv readable format
    for line in reader:
        workclass = line[1].strip()
        if workclass not in worklist:
            worklist.append(workclass)
    #print(workset)
    for work in worklist:
        print(work)
