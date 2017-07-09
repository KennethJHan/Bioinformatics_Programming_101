#!/usr/bin/python3

import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("#usage python", sys.argv[0],"<fastq>")
		sys.exit()
	InFASTQ = sys.argv[1]
	lRead = []
	iReadCnt = 0
	iCnt = 0
	with open("067.filtered.fastq",'w') as fw:
		with open(InFASTQ) as fr:
			for line in fr:
				iCnt += 1
				if iCnt % 4 == 1: # Header
					dRead = {}
					dRead["Header"] = line.strip()
				elif iCnt % 4 == 2: # Sequence
					dRead["Sequence"] = line.strip()
				elif iCnt % 4 == 3: # Delimiter
					dRead["Delimiter"] = line.strip()
				elif iCnt % 4 == 0: # Quality
					sQual = line.strip()
					dRead["Quality"] = sQual
	
					iQual = 0
					for s in sQual:
						iQual += ord(s)-33
					fQual = round(iQual/len(line),2)
					
					if fQual >= 35.0:
						iReadCnt += 1
						fw.write(dRead["Header"]+"\n")
						fw.write(dRead["Sequence"]+"\n")
						fw.write(dRead["Delimiter"]+"\n")
						fw.write(dRead["Quality"]+"\n")
	print(iReadCnt)

