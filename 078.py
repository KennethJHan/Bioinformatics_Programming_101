
with open("077.bed","r") as fr:
    for line in fr:
        lLine = line.strip().split("\t")
        sChr = lLine[0]
        sStart = lLine[1]
        sEnd = lLine[2]
        print(sChr+":"+str(int(sStart)+1)+"-"+sEnd)


