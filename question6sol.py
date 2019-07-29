

list=[1,2,-8,-2,0]

min1=list[0]
min2=list[0]

for i in list:
    if(i<min1):
        min1=i
    elif(i<min2 and i>min1):
         min2=i

print("second minimum = " +str(min2))














