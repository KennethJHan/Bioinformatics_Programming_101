SNP, INS, DEL = 0, 0, 0

with open("070.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            lLine = line.split("\t")
            sRef = lLine[3]
            lAlt = lLine[4].split(",")
            for sAlt in lAlt:
                if len(sRef) == len(sAlt):
                    SNP += 1
                elif len(sRef) > len(sAlt):
                    DEL += 1
                else: # len(sRef) < len(sAlt)
                    INS += 1
print("SNP:", SNP)
print("Insertion:", INS)
print("Deletion:", DEL)
