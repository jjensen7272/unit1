name = input("type in your fist and last name")
x = name.find("")
fistName = name[:x]
lastName = name[x+1:]
print(fistName)
print(lastName)
