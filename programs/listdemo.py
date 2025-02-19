#List methods
alist = [10,34,27,78,10,39,48,89,63]
alist.append(100)
print("alist after appending",alist)

alist.extend([51,59,96])
print("alist after extending",alist)

num_of_occurance= alist.count(48)
print("no.of iccurance of an element in list",num_of_occurance)

alist.insert(0,25)#to insert element in particular position. .insert("index","value")
print("alist after insert",alist)

aindex = alist.index(25)
print("index of element 25:",aindex)

alist.sort()
print("alist after sorting",alist)
alist.reverse()
print("alist after reverse",alist)