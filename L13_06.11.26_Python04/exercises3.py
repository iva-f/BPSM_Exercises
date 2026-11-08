#!/usr/bin/python3

sequences = ["ATTGTACGG", "AATGAACCG", "AATGAACCC", "AATGGGAAT"]

output=[]

# for every sequence 'i' in the list; and for every sequence other than 'i' in the list... (pairwise comparisons):

for i in sequences:
# store index position and length of each sequence in the list
# each sequence spans characters (start = length of sequence * index position) to (start + length of sequence)
    index = sequences.index(i)
    sequences_string = "".join(sequences) # convert the list of sequences to one string
    
    start=len(i)*index; stop=start+len(i)

# remove the sequence currently being processed from the string of sequences:
    other_sequences = sequences_string[:start]+sequences_string[stop:]

# split the string of other sequences into a list, for j in range(0, length of the string, length of each sequence):
    other_list = [other_sequences[j:j+len(i)] for j in range(0, len(other_sequences), len(i))]

    for k in other_list:
# reset counters for each pairwise comparison
# 'counter' tracks index position of each character in the sequence
        counter=0; match=0

        while counter <= (len(i)-1): # len(i)=9, but index from 0-8
            if i[counter] == k[counter]:
                match += 1
            counter += 1

        similarity = round((match/len(i))*100, 2)
        output.append(f"Sequences: {i} & {k}\tPercentage similarity: {similarity}%")

# remove redundant pairwise comparisons:
# n! combinations i.e. for blocks of 3 comparisons, print 123, then x56, then xx9, then xxx

start=0; skip=0

while start < len(output):
    stop = start + len(sequences)-1 - skip # e.g. print comparisons 0-3

    for i in range(start,stop):
        print(output[i])

    start = stop + skip # on next iteration, print comparisons 5-7 (skip 1 sequence)
    skip += 1 # increment number of sequences that are skipped

