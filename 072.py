cntPASS = 0

with open("070.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            lLine = line.split("\t")
            if lLine[6] == "PASS":
                cntPASS += 1
print(cntPASS)
