#!/usr/bin/python3

import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("#usage python", sys.argv[0],"<fastq>")
		sys.exit()
	InFASTQ = sys.argv[1]
	lQual = []
	iCnt = 0
	with open(InFASTQ) as fr:
		for line in fr:
			iCnt += 1
			if iCnt % 4 == 0:
				sQual = line.strip()
				iQual = 0
				for s in sQual:
					iQual += ord(s)-33
				fQual = iQual/len(line)
				lQual.append(fQual)
	lQual = list(map(lambda x: round(x,2), lQual))
	print(lQual)

