#!/usr/bin/python3

import sys, argparse, os

parser = argparse.ArgumentParser( # initialise instance of the parser
        description="Script that, given any DNA sequence and k-mer length, will print all k-mers that occur more than a given number of times. Please use example_sequence_file.fasta to try out the script."
) 

parser.add_argument("sequence", help="Plaintext file containing the sequence only")
parser.add_argument("k_mer", type=int, help="Length of k-mer")
parser.add_argument("n", type=int, help="Minimum number of occurrences of the k-mer (exclusive)")

arguments = parser.parse_args() # parse arguments from the 'parser' object

sequence_file = arguments.sequence; k_mer = arguments.k_mer; n = arguments.n # store argument values

# check that sequence file exists, and that it contains only ATCG:
try:
    with open(sequence_file) as conn:
        sequence = conn.read()
        sequence = "".join(sequence.split()) # remove all whitespace characters
        
        for i in sequence.lower(): # for every character in sequence...
            if i not in ["a","t","c","g"]: # if sequence contains non-ATCG characters...
                sys.exit("Sequence contains non-ATCG characters. Please edit the sequence file and try again.")

except Exception: # handles all exceptions excluding system exit
    sys.exit("Could not open file ''. Please check whether path exists, and whether the file has the correct read permissions.")

if n < 0 or n > len(sequence):
    sys.exit("Minimum number of occurrences of the k-mer must be positive integer, and cannot exceed length of sequence. Please try again.")

elif k_mer < 0 or k_mer > len(sequence):
    sys.exit("Length of k-mer must be positive integer, and cannot exceed length of sequence. Please try again.")

else:
    pass

start = 0; stop = k_mer # initialise start and stop position of the sliding window, where stop is length of k-mer
all_k_mers=[]

for i in range(0, (len(sequence)-k_mer+1), 1): # len(sequence)-length of k-mer (to avoid producing partial k-mers)+length of offset (to include final window)
    
    all_k_mers.append(sequence[start:stop])
    start += 1; stop += 1 # increment start and stop positions by the offset

all_k_mers = set(all_k_mers) # convert list to set (non-redundant list)

output = [f"{k_mer}-mers that occur >{n} times in '{sequence_file}':"]

for i in all_k_mers:
    if sequence.count(i) > n: # if number of occurrences of each k-mer exceeds the specified value...
        output.append("{0}\tNumber of occurrences: {1}".format(i, sequence.count(i)))

for i in output:
    print(i)


