Header, Data = "", ""

with open("070.vcf","r") as fr:
    for line in fr:
        if line.startswith("#"):
            Header += line
        else:
            Data += line

