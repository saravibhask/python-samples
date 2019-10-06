# Author : Savith K
# Date : 9/21/2019
# Learning Python programming following Microsoft python tutorials

from array import array; 

## Collections
atomicFamily1 = ["Nikhil", "Rachana", "Savith"];
atomicFamily2 = ["Appaji", "Amma", "Sunil"];
atomicFamily3 = ["Swarna", "Suresh", "Samarth"];

jointFamily = [atomicFamily1, atomicFamily2, atomicFamily3];
print(jointFamily);
jointFamily.sort();
print(jointFamily);

family = ["Nikhil", "Rachana", "Amma","Appaji", "Sunil", "Swarna", "Savith"];
family.insert(7, "Suresh");
print(family);
family.sort();
print(family);

atomicFamily = family[2:5];
print(atomicFamily);

## Arrays
scores = array('d'); 
scores.append(99);
scores.append(98);
scores.append(89);

print(scores);
print(scores[1]);

## Dictionary -- mainly used for key value pairs
person = {"firstName":"Savith", "lastName":"Kumar", "age":45};
print(person);
print(person["firstName"], person["age"]);
