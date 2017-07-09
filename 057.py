import sys
import urllib.request
import json

def readRSNumToJson(sRSNum):
    sURL = "http://grch37.rest.ensembl.org/variation/human/"+sRSNum+"?content-type=application/json"
    dRSNum = json.loads(urllib.request.urlopen(sURL).read().decode('utf-8'))
    return dRSNum
#end: def readRSNumToJson

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python3",sys.argv[0],"<rs Number>")
        sys.exit()
    sRSNum = sys.argv[1]
    dRSNum = readRSNumToJson(sRSNum)
    print("#rsId\tLocation\tAncestral_allele\tMinor_allele")
    print(dRSNum['name']+"\t"+dRSNum['mappings'][0]['location']+"\t"+dRSNum['ancestral_allele']+"\t"+dRSNum['minor_allele'])
#end: if __name__

