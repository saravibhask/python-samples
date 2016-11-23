import time

tupleExample = ('Savith', 123, 88.88)
dictExample = {'name':'Savith', 'address':'123 Blue street'}
listExample = ['Kumar', 456, 99.99]

print (dictExample)
print (dictExample.keys())
print (dictExample.values())
print (dictExample['name'])

print (tupleExample)
print (tupleExample[2])


print (listExample)
print (listExample[2])

print (len(listExample))

for x in listExample:
	print (x)


dictExample = {'Fname':'Savith', 'Lname':'Kumar', 'Address Line 1':'123 Blue St', 'City':'Green City', 'Zip':'12345'}

print(dictExample)

for x in dictExample :
    print (x, ' : ', dictExample[x])

listExample = ['abc', 123, 45.67]

for x in listExample :
    print (x)

tupleExample = ('xyz', 456, 89.01)


print("Hello, World!")

print (time.strftime("%m/%d/%Y"))

print ("Removed the EOF comment")


