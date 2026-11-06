#!/usr/bin/python3

###################
# local sequence: #
###################

exon_list=[]; intron_list=[]

with open("plain_genomic_seq.txt") as conn:
    sequence = conn.read()

    exon_list.append(sequence[:64]); exon_list.append(sequence[91:].strip()) # strip \n from end
    intron_list.append(sequence[64:91])

exon = ("".join(exon_list)).upper() # join list into one string; and ensure in uppercase
intron = ("".join(intron_list)).upper()

# remove invalid (non-ATCG) characters from sequences:
invalid_nt=[]

for i in [exon, intron]:
    for nt in i: # check every nt in each of 'exon' and 'intron'
        if nt not in ["A","T","C","G"]:
            invalid_nt.append(nt) # if invalid characters, append to list

invalid_nt = set(invalid_nt) # convert list to set ('non-redundant list')

for nt in invalid_nt:
    exon = exon.replace(nt, "") # remove all instances of the invalid characters from each sequence
    intron = intron.replace(nt, "")

exon_length = len(exon)
intron_length = len(intron)

with open("localsequence_exon.fasta", "w") as conn:
    conn.write(f">Local sequence, exon, length: {exon_length}\n{exon}")

with open("localsequence_intron.fasta", "w") as conn:
    conn.write(f">Local sequence, intron, length: {intron_length}\n{intron}")

####################
# Remote sequence: #
####################

# esearch -db nucleotide -query "AJ223353[accession]" | efetch -format fasta | grep -v ">" > AJ223353.fasta
# esearch -db nucleotide -query "AJ223353[accession]" | efetch -format gb > AJ223353.gb
# grep "CDS" AJ223353.gb > CDS.txt

with open("CDS.txt") as conn:
    CDS = conn.read().strip().replace(" ", "") # remove \n and all whitespace, CDS="CDS29..409"
    CDS = CDS[3:].split("..") # remove 'CDS' and split into ['29', '409']

start = int(CDS[0]); stop = int(CDS[1]) # 'start' and 'stop' position of exon

with open("AJ223353.fasta") as conn:
    sequence = conn.read().replace("\n", "") # remove all instances of \n

exon = sequence[start:stop].upper() # extract exon from the sequence; and ensure uppercase

# extract introns from the sequence, and append to list:
intron_list=[]
intron_list.append(sequence[:start]) # i.e. from start of sequence, to start of exon
intron_list.append(sequence[stop:]) # i.e. from end of exon, to end of sequence

intron = "".join(intron_list).upper() # join the list into one string; and ensure uppercase

exon_length = len(exon)
intron_length = len(intron)

with open("remotesequence_exon.fasta", "w") as conn:
    conn.write(f">AJ223353 Remote sequence, exon, length: {exon_length}\n{exon}")

with open("remotesequence_intron.fasta", "w") as conn:
    conn.write(f">AJ223353 Remote sequence, intron, length: {intron_length}\n{intron}")

##########
# BLAST: #
##########

# Generate local BLAST database from nem.fasta:
# makeblastdb -in nem.fasta -dbtype prot -out nem

import shutil, os, subprocess

for i in ["local", "remote"]:
    for j in ["exon", "intron"]:
        shutil.copy(f"{i}sequence_{j}.fasta", f"database/{i}sequence_{j}.fasta") 

os.chdir("database")

# Run BLAST search of the sequence files, against the local database:
# -outfmt 6 (tabular format)
# -num_alignments 1 (show 1 alignment)

for i in ["local", "remote"]:
    for j in ["exon", "intron"]:
        subprocess.call(f"blastx -db nem -query {i}sequence_{j}.fasta -outfmt 6 -num_alignments 1 > {i}sequence_{j}.out", shell=True)
        
        shutil.copy(f"{i}sequence_{j}.out", f"../{i}sequence_{j}.out") # move output back into parent directory
        os.remove(f"{i}sequence_{j}.out"); os.remove(f"{i}sequence_{j}.fasta") # clean up 'database' directory 

os.chdir("..")

