#!/usr/bin/python3

import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("#usage python", sys.argv[0],"<fastq>")
		sys.exit()
	InFASTQ = sys.argv[1]
	with open(InFASTQ) as fr:
		lRead = fr.readlines()
	print(len(lRead)/4)
