seq = ""

with open('059.fasta','r') as fr:
    for line in fr:
        if line.startswith(">"):
            pass
        else:
            seq += line.strip()

compDic = {"A":"T","C":"G","G":"C","T":"A"}
compSeq = ""
for s in seq:
    compSeq += compDic[s]

revCompSeq = compSeq[::-1]
print(revCompSeq)
