#!/usr/bin/python3

import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("#usage python", sys.argv[0],"<fastq>")
		sys.exit()
	InFASTQ = sys.argv[1]
	lLane = []
	iCnt = 0
	iCntA, iCntC, iCntG, iCntT = 0,0,0,0
	with open(InFASTQ) as fr:
		for line in fr:
			iCnt += 1
			if iCnt % 4 == 2:
				sSeq = line.strip()
				iCntA += sSeq.count("A")
				iCntC += sSeq.count("C")
				iCntG += sSeq.count("G")
				iCntT += sSeq.count("T")
	print("A:",iCntA)
	print("C:",iCntC)
	print("G:",iCntG)
	print("T:",iCntT)
