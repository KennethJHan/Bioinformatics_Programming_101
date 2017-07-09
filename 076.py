#!/usr/bin/python
#[0]     [1]     [2]         [3]     [4]     [5]     [6]     [7]     [8]         [9]             [10]
##CHROM  POS     ID          REF     ALT     QUAL    FILTER  INFO    FORMAT      Sample1         Sample2
#chr20   14370   rs6054257   G       A       29      PASS    .       GT:AD:DP    0/1:44,37:81    1/1:44,37:81
#chr20   17330   .           T       A       3       q10     .       GT:AD:DP    1/1:44,37:81    0/0:44,37:81
#chr20   1110696 rs6040355   A       G,T     29      PASS    .       GT:AD:DP    0/0:44,37:81    1/2:44,37:81
#chr20   1230237 .           TT      T       29      PASS    .       GT:AD:DP    0/1:44,37:81    1/1:44,37:81
#chr20   1234567 .           GT      G,GTC   29      PASS    .       GT:AD:DP    0/1:44,37:81    0/2:44,37,81


print("#CHROM\tPOS\tREF\tALT\tSample1\tGT\tSample2\tGT")
with open("071.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            lLine = line.split("\t")
            sChr = lLine[0]
            sPos = lLine[1]
            sRef = lLine[3]
            lAlt = lLine[4].split(",")
            lRefAlt = [sRef]+lAlt
            sGT1 = lLine[9].split(":")[0]
            lGT1 = list(map(int, sGT1.split("/")))
            sGT2 = lLine[10].split(":")[0]
            lGT2 = list(map(int, sGT2.split("/")))
            
            sGTW1 = lRefAlt[lGT1[0]] + "/" + lRefAlt[lGT1[1]]
            sGTW2 = lRefAlt[lGT2[0]] + "/" + lRefAlt[lGT2[1]]
            

            print(sChr+"\t"+sPos+"\t"+sRef+"\t"+sRef+"\t"+sGT1+"\t"+sGTW1+"\t"+sGT2+"\t"+sGTW2)
            


