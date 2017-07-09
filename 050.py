#!/usr/bin/python

ageSum = 0
female = 0

with open("047.tsv",'r') as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            lLine = line.strip().split("\t")
            if lLine[2] == "female":
                age = int(lLine[1])
                ageSum += age
                female += 1
print(ageSum/female)


