
st = input("Enter String: ")

countDigigt=0
countChar=0

for i in st:
    if i.isalpha():
        countChar=countChar+1
    elif i.isnumeric():
        countDigigt=countDigigt+1


print("characters: "+str(countChar))
print("digits: "+str(countDigigt))

