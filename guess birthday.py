NUM128 = 128
NUM64 = 64
NUM32 = 32
NUM16 = 16
NUM8 = 8
NUM4 = 4
NUM2 = 2
NUM1 = 1


day_set1 = ""
day_set2 = ""
day_set4 = ""
day_set8 = ""
day_set16 = ""



whatsLeft = 0



for i in range(1,32):
    bia_num=""
    input_num=i
    whatsLeft=input_num
    if input_num >= NUM128:
        whatsLeft = whatsLeft - NUM128
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"
    if whatsLeft >=NUM64:
        whatsLeft = whatsLeft - NUM64
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if whatsLeft >=NUM32:
        whatsLeft = whatsLeft - NUM32
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if whatsLeft >=NUM16:
        whatsLeft = whatsLeft - NUM16
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if whatsLeft >=NUM8:
        whatsLeft = whatsLeft - NUM8
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if whatsLeft >=NUM4:
        whatsLeft = whatsLeft - NUM4
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if whatsLeft >=NUM2:
        whatsLeft = whatsLeft - NUM2
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if whatsLeft >=NUM2:
        whatsLeft = whatsLeft - NUM2
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    if whatsLeft >=NUM1:
        whatsLeft = whatsLeft - NUM1
        bia_num = bia_num + "1"
    else:
        bia_num = bia_num + "0"

    xnum7 = bia_num[7]
    xnum6 = bia_num[6]
    xnum5 = bia_num[5]
    xnum4 = bia_num[4]
    xnum3 = bia_num[3]
    xnum2 = bia_num[2]
    xnum1 = bia_num[1]
    xnum0 = bia_num[0]

    
    x=str(i)
    
    if xnum3 == "1":
        day_set16 = day_set16 +x+" "
    if xnum4 == "1":
        day_set8 = day_set8 +x+" "
    if xnum5 == "1":
        day_set4 = day_set4 +x+" "
    if xnum6 == "1":
        day_set2 = day_set2 +x+" "
    if xnum7 == "1":
        day_set1 = day_set1 +x+" "

#print(day_set1)
print(day_set2)
print(day_set4)
print(day_set8)
print(day_set16)



##list1 = input("is your birthday in the first set of numbers y/n")
##list2 = input("is your birthday in the second set of numbers y/n")
##list3 = input("is your birthday in the third set of numbers y/n")
##list4 = input("is your birthday in the fourth set of numbers y/n")
##list5 = input("is your birthday in the fifth set of numbers y/n")














