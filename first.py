import time

tupleExample = ('Savith', 123, 88.88)
dictExample = {'name':'Savith', 'address':'123 Blue street'}
listExample = ['Kumar', 456, 99.99]

print(dictExample)
print(dictExample.keys())
print(dictExample.values())
print(dictExample['name'])

print(tupleExample)
print(tupleExample[2])

print(listExample)
print(listExample[2])

print(len(listExample))

for x in listExample:
	print(x)

'''
Test comment block line 1
Test comment block line 2
'''

dictExample = {'Fname':'Savith', 'Lname':'Kumar', 'Address Line 1':'123 Blue St', 'City':'Green City', 'Zip':'12345'}

print(dictExample)

for x in dictExample :
    print(x, ' : ', dictExample[x])

listExample = ['abc', 123, 45.67]

for x in listExample :
    print(x)

tupleExample = ('xyz', 456, 89.01)

print(time.strftime("%m/%d/%Y"))

print("Removed the EOF comment")

def firstFunction():
    print("Statement within firstFunction()")
    print("Second statement from within firstFunction()")
print("Statement right after firstFunction()")

firstFunction()

print("Editing from personal laptop - local IDE (sublime)")

pi = 3.14
radius = 5
result = float(4/3*pi*radius**3)
print('Volume of a sphere of radius %(rad)d is %(res)f' %{'rad':radius, 'res':result})

print('{:+<30}'.format('Savith'))
print('{:+^30}'.format('Savith'))
print('{:+>30}'.format('Savith'))

strTest = "       test:string        "

print(strTest.lstrip())
print(strTest.rstrip())
print(strTest.strip())

print(strTest.partition(':'))

print("Savith".rjust(30,'+'))

print("Last instruction in the program.")
