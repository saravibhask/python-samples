# Author : Savith K
# Date : 9/20/2019
# Learning Python programming following Microsoft python tutorials

#importing date and time package
from datetime import datetime, timedelta;

currentDateTime = datetime.now();
print(currentDateTime);

tDelta = timedelta(days=1); #weeks, months
print(currentDateTime - tDelta);

currentDate = datetime.strptime(input("Enter date : "), "%d/%m/%Y");
print(currentDate);
# print(currentDate.MONTH);



