#!/usr/bin/python

import xml.etree.ElementTree as ET
tree = ET.parse('053.xml')
root = tree.getroot()
for i in root.findall('snp'):
    ancestral_allele = i.find('ancestral_allele').text
    minor_allele = i.find('minor_allele').text
    location = i.find('location').text
    print(location+"\t"+ancestral_allele+"\t"+minor_allele)
