#!/usr/bin/python

with open("071.vcf","r") as fr:
    for line in fr:
        if line.startswith("#CHROM"):
            lLine = line.split("\t")
print(len(lLine)-9)
