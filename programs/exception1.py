'''
exception handling
------------------
'''
import csv
try:
    workset = set()
    malecount = 0
    femalecount = 0
    with open("adult11.csv") as fobj:
        reader = csv.reader(fobj)  # converting fobj to csv readable format
        for line in reader:
            gender = line[9].strip()
            if gender == "Male":
                malecount+=1
            else:
                femalecount+=1
        print("Total male count :",malecount)
        print("TOtal female count:",femalecount)
except FileNotFoundError as error:
    print("file is not found")
    print("system generated error:",error)
except IndentationError as error:
    print("file is not found")
    print("system generated error:",error)
except ValueError as error:
    print("file is not found")
    print("system generated error:",error)
except TypeError as error:
    print("file is not found")
    print("system generated error:",error)
except Exception as error:
    print("file is not found")
    print("system generated error:",error)
