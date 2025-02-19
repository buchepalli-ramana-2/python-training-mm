'''
write a program to display the below IP addresses

192.168.0.1
192.168.0.2
192.168.0.3
..
..
192.168.0.10
192.168.1.1
192.168.1.2
192.168.1.3
..
..
192.168.1.10
'''
print("Hello" + "python") # concatenating two string values

print("hello" + str(5)) #to concatenate the int value to string we need Type casting
print([10,20] + list((30,40)))

#To print ip addresses as given above

#method1
fixedip = "192.168.0."
for i in range(1,11):
    finalip = fixedip + str(i)
    print(finalip)

#Method2 we can use the string format
ip ="192.168.0.{}"
for i in range(1,11):
    print(ip.format(i))

# Print the ip like below
# 192.168.0.0 ..192.168.0.10...192.168.1.0.. 192.168.1.10
ip2 = "192.168.{}.{}"
for i in range(0,2):
    for j in range(1,11):
        print(ip2.format(i,j))