iBedRange = 0

with open("077.bed","r") as fr:
    for line in fr:
        lLine = line.strip().split("\t")
        iStart = int(lLine[1])
        iEnd = int(lLine[2])

        iBedRange += iEnd - iStart

print(iBedRange)

