print ("Python terms")
puzzel = """
fjvfloatdy
yopxednins
mspfycnnal
xeaeeukgei
slufryprlc
abeeiagcoi
buclqttbon
gojlivxobg
admyahgerj
stringwvrs
"""
print(puzzel)
print("word list")
word_list="float, while, if, boolean, double, operators, string, slicing, index"
print (word_list)

word1 = input("enter the index positions of float")

word1_length=len("float")
word2_length=len("while")
word3_length=len("if")
word4_length=len("boolean")
word5_length=len("double")
word6_length=len("operators")
word7_length=len("string")
word8_length=len("slicing")
word9_length=len("index")


i=0
foundword=""
while i < word1_length:
    index=word1[i]
    index=int(index)
    foundword = foundword+puzzel[index+1]
    i+=1
print(foundword)

input("press enter to exit")
