#!/usr/bin/python

content = ""

with open("059.fasta",'r') as fr:
    for line in fr:
        if line.startswith(">"):
            header = line.strip()
        else:
            content += line.strip()
print("header\n"+header)
print("\ncontent\n"+content)
