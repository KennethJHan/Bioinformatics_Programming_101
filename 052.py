#!/usr/bin/python

with open("052.tsv",'w') as fw:
    with open("052.csv",'r') as fr:
        for line in fr:
            fw.write(line.replace(",","\t"))

