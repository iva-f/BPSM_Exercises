#!/usr/bin/python3

#######
# Q1: #
#######

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

A = seq.count("A"); T = seq.count("T")

AT = ((A+T) / len(seq)) * 100
AT = str(round(AT,2)) # round to 2 d.p.

output = ("A content: {}\nT content: {}\nProportion of A+T: {}%").format(str(A), str(T), AT)
print(output)

#######
# Q2: #
#######

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

# index position of each base; then print the complement
index = seq.replace("A", "0").replace("T", "1").replace("C", "2").replace("G", "3")

complement = index.replace("0", "T").replace("1", "A").replace("2", "G").replace("3", "C")
print("Sequence:  ", seq+"\nComplement:", complement)

#######
# Q3: #
#######

seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
EcoRI = "GAATTC" # G/AATTC

p = seq.find(EcoRI) # find *start* position of the restriction site
# therefore position of cut is p+1

f1 = len(seq[:p+1]) # length of fragment up to the cut
f2 = len(seq[p+1:]) # length of fragment after the cut

output = ("Length of fragment 1: {}\nLength of fragment 2: {}").format(f1, f2)
print(output)

#######
# Q4: #
#######

seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1 = seq[0:63]; exon2 = seq[90:] # exon1 up to 63rd char; exon2 from 91st char

output = ("Coding region: {}").format(exon1 + exon2)
print(output)

p = (len(exon1 + exon2) / len(seq)) * 100
p = str(round(p,2)) # round to 2 d.p.

output = ("Proportion of coding sequence: {}%").format(p)
print(output)

intron = seq[63:90]
print(exon1+"["+intron.lower()+"]"+exon2)

