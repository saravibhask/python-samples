import time
import fibonacci
import pprint

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

print('Print using pprint()')
pprint.pprint(dictExample)

print('Print using regular print()')
print(dictExample)

for x in dictExample :
	print(x, ' : ', dictExample[x])

for i in dictExample.items():
	print(i)

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


def sumOfSeries(a, d, n):
	sumSeries = n*((2*a)+((n-1)*d))/2
	return sumSeries;


def printSeries(a, d, n):
	listSeries = []
	for x in range(1, n):
		listSeries.append(a)
		#print(str(a)  + ',', sep=',')
		a = a + d
	print(listSeries)

firstFunction()

print("Before calling sumOfSeries()")
sos = sumOfSeries(1,3,50)
print(sos)
printSeries(1,3,50)
print("After calling sumOfSeries()")

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

fibonacci.fib(100)

b = None

print(b is None)

if b is None:
	print('b is None')

a = int(0)
if a > 0:
	print('a is greater than 0')
elif a < 0:
	print('a is less than 0')
elif a == 0:
	print('a is 0')
else:
	print('a is unknown or "None"')


def spam():
	eggs = 99
	bacon()
	print(eggs)

def bacon():
	eggs = 0

spam()


myList = ['a', 'b', 'c', 'd', 'e']
print(myList[int(int('3' * 2) / 11)])

print("Inserting new statement to test GIT integration from Eclipse-Oxygen")

print("Last instruction in the program.")
