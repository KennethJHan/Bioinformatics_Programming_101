#!/usr/bin/python

with open("047.csv",'r') as fr:
    arrFile = fr.readlines()

for i in arrFile[1:]:
    print(i.split(",")[0], end="\t")
print('')
for i in arrFile[1:]:
    print(i.split(",")[1], end="\t")
