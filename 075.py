cntPOS = 0
cntRSID = 0

with open("070.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            lLine = line.split("\t")
            if lLine[2] != ".":
                cntRSID += 1
            cntPOS += 1
print(cntRSID / cntPOS)
