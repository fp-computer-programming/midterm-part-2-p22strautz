# Author: SCT (AMDG) 12/14/21

final_velocity = int(input("Enter the final velocity in m/s:"))

inital_velocity = int(input("Enter the inital velocity in m/s:"))

time = int(input("Enter the time in seconds:"))

accel = (final_velocity - inital_velocity) / time

print("The average acceleration is {0}".format(accel))

