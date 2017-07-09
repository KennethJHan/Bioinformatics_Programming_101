#!/usr/bin/python3

import sys

def readSeq(InFASTA):
	(sHeader, sSeq) = ("","")
	with open(InFASTA) as fr:
		for line in fr:
			if line.startswith(">"):
				sHeader += line.strip()
			else:
				sSeq += line.strip()
	return (sHeader, sSeq)
#end: def readSeq

def countSeq(sSeq, sBase):
	return sSeq.count(sBase)
#end: def countSeq

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("#usage: python", sys.argv[0],"<fasta>")
		sys.exit()
	InFASTA = sys.argv[1]
	(sHeader, sSeq) = readSeq(InFASTA)
	iCntA = countSeq(sSeq, "A")
	iCntC = countSeq(sSeq, "C")
	iCntG = countSeq(sSeq, "G")
	iCntT = countSeq(sSeq, "T")
	print("A:", iCntA)
	print("C:", iCntC)
	print("G:", iCntG)
	print("T:", iCntT)
#end: if __name__
