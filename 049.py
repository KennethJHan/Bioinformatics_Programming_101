def writeResult(lst):
    with open("049.csv",'a') as fw:
        result = ""
        for i in lst:
            result += (i+",")
        fw.write(result[:-1]+"\n")


Header = ["SampleID", "Site1", "Site2", "Site3"]
Sample1 = ["Sample1", "GG", "AT", "CC"]
Sample2 = ["Sample2", "GT", "AA", "CC"]
Sample3 = ["Sample3", "TT", "TT", "CT"]
Sample4 = ["Sample4", "GG", "AT", "TT"]

writeResult(Header)
writeResult(Sample1)
writeResult(Sample2)
writeResult(Sample3)
writeResult(Sample4)

