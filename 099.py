#!/usr/bin/python

import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("#usage: python",sys.argv[0],"<vcf>")
		sys.exit()
	InVCF = sys.argv[1]
	iTs, iTv = 0, 0
	d = {}
	with open(InVCF) as fr:
		for line in fr:
			if line.startswith("#"):
				pass
			else:
				lLine = line.split("\t")
				sRef = lLine[3]
				sAlt = lLine[4]

				if len(sRef) == 1 and len(sAlt) == 1:
					sRA = sRef+"_"+sAlt
					try:
						d[sRA] += 1
					except KeyError:
						d[sRA] = 1

					if sRef == "A":
						if sAlt == "G":
							iTs += 1
						else:
							iTv += 1
					elif sRef == "C":
						if sAlt == "T":
							iTs += 1
						else:
							iTv += 1
					elif sRef == "G":
						if sAlt == "A":
							iTs += 1
						else:
							iTv += 1
					elif sRef == "T":
						if sAlt == "C":
							iTs += 1
						else:
							iTv += 1

	print(d)

	print("Transition:",iTs)
	print("Transversion:",iTv)
	print("Ts/Tv ratio:",float(iTs)/iTv)




