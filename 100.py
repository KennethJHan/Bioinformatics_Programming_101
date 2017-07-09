#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print("#usage: python",sys.argv[0],"<VCF> <Gene>")
    sys.exit()

fVCF = sys.argv[1]
sGene = sys.argv[2]

with open(fVCF,'r') as fr:
    for line in fr:
        if sGene in line:
            lLine = line.split("\t")
            sChr = lLine[0]
            sPos = lLine[1]
            sRef = lLine[3]
            sAlt = lLine[4]
            print(sChr+'\t'+sPos+'\t'+sRef+'\t'+sAlt)
