Code = {'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
             'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
             'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*',
             'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W',
             'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
             'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
             'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
             'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
             'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
             'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
             'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
             'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
             'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
             'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
             'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
             'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
            }

seq = ""

with open('059.fasta','r') as fr:
    for line in fr:
        if line.startswith(">"):
            pass
        else:
            seq += line.strip()
seqPtn = ""
for i in range(0,len(seq)-3+1,3):
    seqPtn += Code[seq[i:i+3]]

print(seqPtn)
