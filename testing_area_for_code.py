# Chapter 1  - Ptyhon cookbook - focus is on collections module

# Python

file2 = open("test_non_csv.txt")

# unpacking test
q,e,r,t,y,u,i,o,b = file2.read() # this matches text in file "testnocsv"
# Reading from file
print(file2.read())

file2.close()


# binary file unpacking





file = open("document.bin","wb")
sentence = bytearray("T".encode("ascii"))
file.write(sentence)
file.close()


file = open("document.bin","rb")
print(file.read())
file.close()


##
file=open("array.bin","wb")
t=1
array=bytearray(t)
file.write(array)
file.close()

file=open("array.bin","rb")
#number=file.read()
q = file.read()
#print(number)
file.close()


data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]

_, shares, price, _ = data


