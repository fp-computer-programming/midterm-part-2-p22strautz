# Author: SCT (AMDG) 12/14/21

import random

def cloning():
    num = random.randint(0, 9999)
    if num <= 9:
            print("CT-000" + str(num))
    elif num <= 99:
            print("CT-00" + str(num))
    elif num <= 999:
        print("CT-0" + str(num))
    else:
        print("CT-" + str(num))


answer = input("Do you want to create a clone? (Y/N):")
clone =  cloning()
if answer == "y" or "Y":
    print("New clone trooper created... name:" + str(clone))
elif answer == "n" or "N":
    print("No clone will be made.")
            



