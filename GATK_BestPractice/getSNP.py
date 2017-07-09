#!/usr/bin/python

import sys

if __name__ == "__main__":
	iCnt = 0
	with open(sys.argv[1],'r') as fr:
		for line in fr:
			if line.startswith("#"):
				pass
			else:
				lLine = line.split("\t")
				if len(lLine[3]) == 1 and len(lLine[4]) == 1:
					iCnt += 1
	print iCnt
