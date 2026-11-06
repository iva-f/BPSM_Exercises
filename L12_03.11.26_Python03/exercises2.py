#!/usr/bin/python3

# exons.txt contains 'start, stop' positions of exons, therefore store each line of exons.txt to variable, and use the variable to index the sequence read from genomic_dna2.txt

with open("genomic_dna2.txt") as conn:
    seq = conn.read()

exons = []

with open("exons.txt") as conn:
    for i in conn.readlines():
        exons.append(i.strip()) # strip \n from each line and append to list 'exons'

sequence_list = []

for i in exons: # e.g. "5,58"
    start = i.split(",")[0]; stop = i.split(",")[1] # split each line into list, and store 'start' and 'stop' positions

    sequence_list.append(seq[int(start):int(stop)]) # use 'start' and 'stop' to slice the sequence, and append to list

sequence_string = "".join(sequence_list) # join exons in 'sequence_list' into one string

with open("output2.txt", "w") as conn:
    conn.write(sequence_string)

