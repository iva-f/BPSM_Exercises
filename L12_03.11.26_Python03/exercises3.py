#!/usr/bin/python3

# note: implement sys.argv for window size and offset

import os

with open("remotesequence_exon.fasta") as conn:
    sequence = conn.readlines()[1:] # remove header
    sequence = "".join(sequence) # convert list into one string

start=0; stop=29 # initialise counter

if os.path.exists("AJ223353exon_allwindows.fasta"):
    os.remove("AJ223353exon_allwindows.fasta") # delete 'AJ223353exon_allwindows.fasta' if already exists (since append, rather than overwrite in the loop)

for i in range(0,len(sequence)-26,3): # len(sequence)-26 since window size is 0:29 (0-30), and +3 to include last window
    window = sequence[start : stop]

    gc_content = ((window.count("G")+window.count("C"))/len(window))*100 # len(window) = 30
    gc_content = round(gc_content,2)

    print(f"Sequence: {window}\nGC content: {gc_content}%")

    if os.path.exists("Q3_output")==False:
        os.mkdir("Q3_output") # create directory Q3_output if it does not exist

    # write each window into individual files:
    with open(f"Q3_output/AJ223353exon_window{start}-{stop}.fasta", "w") as conn:
        conn.write(f">AJ223353 Remote sequence, exon, window: {start}-{stop}\n{window}")

    # write each window; and sequences at the ends of each window into one file
    with open("AJ223353exon_allwindows.fasta", "a") as conn:
        conn.write(f">AJ223353 Remote sequence, exon, window: {start}-{stop}\n{window}\n")
        conn.write(sequence[:start].lower()+f"[{window}]"+sequence[stop:].lower()+"\n\n")

    start += 3; stop += 3 # increment counter by offset 3

gc_seq = ((sequence.count("G")+sequence.count("C"))/len(sequence))*100
gc_seq = round(gc_seq,2)

print(f"GC content of the sequence: {gc_seq}%")

