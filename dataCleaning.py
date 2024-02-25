import numpy as np
import matplotlib.pyplot as plt

#here i open the file data and save it to list while taking the first index out as that is instuctions.
file = open("monroe county car crach 2003-2015.csv", "r")
lines = file.readlines()



file.close()
my_dict = {}
counter = 0

for line in lines:
    without = line.split(",")
    without = str(without[7])
    if without in my_dict:
        continue
    else:
       my_dict[without] = str(counter)
       counter += 1
    

for i in range(len(lines)):
    without = lines[i]
    without = without.split(",")
    del without[5]
    del without[5]
    del without[6]
    if without[3] == "Weekend":
        without[3] = "0"
    elif without[3] == "Weekday":
        without[3] = "1"
    if without[5] in my_dict:
        without[5] = my_dict[without[5]]
    
    lines[i] = without

    
file = open("monroe county car crash 2003-2015.csv", "w")
for i in range(len(lines)):
    num = 0
    for z in lines[i]:
        if num < 7:
            file.write(str(z) + ",")
            num+=1
        else:
            file.write(str(z))
    
    file.write("\n")
    
file.close
print(my_dict)
print("finished")
    



    
    


    

