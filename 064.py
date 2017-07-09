#!/usr/bin/python3

import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("#usage python", sys.argv[0],"<fastq>")
		sys.exit()
	InFASTQ = sys.argv[1]
	lLane = []
	iCnt = 0
	with open(InFASTQ) as fr:
		for line in fr:
			iCnt += 1
			if iCnt % 4 == 1:
				lLane.append(line.split()[0].split(":")[3])
	print(list(set(lLane)))
