# Author : Savith K
# Date : 9/20/2019
# Learning Python programming following Microsoft python tutorials

x = 23;
y = 0;


try:
    print(x/y)
except ZeroDivisionError as e:
    print("Not allowed to divide by Zero.");
else:
    print("Something else went wrong.");
finally:
    print("In finally block, cleaning up complete.")