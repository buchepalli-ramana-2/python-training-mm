name = "Python programming"
print(name)
print("I Love", name)

'''
#slicing
# string[start:stop:increment]
print(len(name)) # number of chars in string
print(name[0]) # first string
print(name[-1]) # laast string
print(name[:-1]) # exclude last string
print(name[::-1]) # String in reverse order
print(name[:-3]) #Exclude last three strings
print(name[0:5]) #Print first 5 items('left' value colon includes and 'right' is excluded)
print(name[2:5]) #print from third item till 4th index.
print(name[::]) # all string
print(name[:]) #All strings
print(name[0:10:2]) #print every second char starting from 0 to 10 index
'''

#String Methods
print(name.capitalize())#first letter will be Uppercase
print(name.title())#Every first letter of word in sentence will be upper case
print(name.replace("Python","java"))#replace substring with other string
print(name.count("p"))#Give the number of occurances of particular string or word
print(name.upper())#Change all strings into Uppercase
print(name.lower())#Change all strings into lowercase
print(name.count("o"))#give the no. of occurances for 'o' in given string
print(name.startswith("P"))#print the word which starts with given letter
print(name.endswith("g"))#print the word which ends with given letter
print(name.isalpha())#Check does it have alpha numeric
print(name.center(40))#print 40 spaces before and after the string
print(name.center(40,"*"))#print 40 * before and after the string
print(name.split(" "))#split the string into multiple items wherever finds the given value

aname = "  Python "

print(len(aname))
print(len(aname.lstrip()))#remove the left side whitespaces
print(len(aname.rstrip()))#remove right side whitespaces

## Conditional statemnts
name = "python"
# simple if
if name.startswith("p"):
    print("string is python")
    print("inside if")
    print("still inside if")
print("regular lines")



#if-else
if name.startswith("p"):
    print("string is python")
else:
    print("string is something elses")

#example
if name.isupper():
    print("string is upper")
else:
    print("string is lower")


# instead of hardcoding .. we arereading input from keyboard
color = input("Enter any color:")
print("you entered:", color)
if color == "green":
    print("you entered green")
elif color == "red":
    print("you entered red")
elif color == "blue":
    print("Enter entered blue")
else:
    print("you entered something else")

