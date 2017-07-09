import json

lFile = []
dTSV = {}

with open("058.tsv",'r') as fr:
    for line in fr:
        lFile.append(line.split("\t"))

for i in range(len(lFile[0])):
    dTSV[lFile[0][i].strip()] = lFile[1][i].strip()

with open("058.json",'w') as fw:
    json.dump(dTSV, fw)
