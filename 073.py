cntVAR = 0

with open("070.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            lLine = line.split("\t")
            for i in lLine[4].split(","):
                cntVAR += 1
print(cntVAR)
