#!/usr/bin/python3

# Return list of lines in the file using conn.readlines()
# Use indexing to process each line, and store the desired portion in a variable (append to new file)
# len(variable) to obtain new sequence length (append to new file)

import os, sys

# Confirm whether to overwrite output1.txt if it already exists (e.g. the program has been run previously):
if os.path.exists("output1.txt"):
    overwrite = input("output1.txt already exists: overwrite? y/n ")
    if overwrite.lower() in ["y", "yes"]:
        os.remove("output1.txt")
    elif overwrite.lower() in ["n", "no"]:
        sys.exit("Please rename output1.txt and try again") 
    else:
        sys.exit("Invalid input, please enter 'y' or 'n'")

with open("input.txt") as conn:
    counter = 0
    for i in conn.readlines(): # returns list of lines in the file; for each line...
        seq = i[14:] # from 15 (inclusive)
        counter += 1
        length = len(seq)
        
        with open("output1.txt", "a") as output: # append
            output.write(seq)

        print(f"Line no.{counter} has length {length} nt")
