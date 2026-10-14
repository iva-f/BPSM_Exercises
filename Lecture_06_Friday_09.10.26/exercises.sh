#!/bin/bash
#blastx -remote -db nr -query testsequence.fasta -outfmt 7 > remoteblastoutput.out

#######
# Q1: # List subject_ID for all HSPs
#######

while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
	if [[ "${query_ID}" != \#* ]]
	then
		echo ${subject_ID}
	fi
done < blastoutput2.out

#######
# Q2: # List alignment length & percent_ID for all HSPs
#######

while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
        if [[ "${query_ID}" != \#* ]]
        then
                echo -e ${alignment_length} '\t' ${percent_identity}
        fi
done < blastoutput2.out

#######
# Q3: # Show HSPs with >20 mismatches
#######

while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
	if [[ "${query_ID}" != \#* ]] && ((${mismatches} > 20))
        then
                echo -e ${subject_ID} '\t' ${mismatches}
        fi
done < blastoutput2.out

#######
# Q4: # Show HSPs <100aa and >20 mismatches
#######

while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
	if [[ "${query_ID}" != \#* ]] && ((${alignment_length} < 100)) && ((${mismatches} > 20))
        then
                echo -e "Subject ID: "${subject_ID} '\t'\
		       	"Length: "${alignment_length} '\t'\
		       	"Mismatches: "${mismatches}
        fi
done < blastoutput2.out

#######
# Q5: # Show first 20 HSPs that have <20 mismatches
#######

unset counter

while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
        if [[ "${query_ID}" != \#* ]] && ((${mismatches} > 20))
        then
		counter=$((counter+=1))
		if ((${counter} <= 20))
		then
			echo -e "Index: "${counter} '\t'\
			"Subject ID: "${subject_ID} '\t'\
                        "Mismatches: "${mismatches}
		fi
        fi
done < blastoutput2.out

#######
# Q6: # Count number of HSPs shorter than 100aa
#######

number=$(while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
        if [[ "${query_ID}" != \#* ]] && ((${alignment_length} < 100))
        then
		echo -e "Subject ID: "${subject_ID} '\t'\
                "Length: "${alignment_length}
        fi
done < blastoutput2.out | wc -l)

echo "Number of HSPs with length < 100aa: "${number}

#######
# Q7: # List 10 highest-scoring HSPs
#######

unset counter

while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
        if [[ "${query_ID}" != \#* ]]
        then
		counter=$((counter+=1))
		if ((${counter} <= 10))
		then
			echo -e "Index: "${counter} '\t'\
			"Subject ID: "${subject_ID} '\t'\
			"E-value: "${evalue} '\t'\
                	"Bit score: "${bitscore}
		fi
	fi
done < blastoutput2.out

#######
# Q8: # List start position of all HSPs that contain "AEI" in subject_ID
#######

while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
        if [[ "${query_ID}" != \#* ]] && [[ "${subject_ID}" =~ AEI ]] # =~ operator enables use of regex within square brackets
        then
		echo -e "Subject ID: "${subject_ID} '\t'\
		"Start position: "${s_start}
        fi
done < blastoutput2.out

#######
# Q9: # Give the number of subject sequences with >1 HSP
#######

count=$(sort -t$'\t' -k2,2 blastoutput2.out | cut -f2 | uniq -c)

while read count subject_ID
do
	if ((${count} >= 2))
	then
		echo -e "Subject ID: "${subject_ID} '\t'\
		"Number of HSPs: "${count}
	fi
done <<< ${count}

########
# Q10: # Give the percentage of each HSP that is made up of mismatches
########

while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
        if [[ "${query_ID}" != \#* ]]
	then
		percent=$(echo "scale=2; ${mismatches}/${alignment_length}*100" | bc) # bc: calculator that performs integer arithmetic, must specify n decimal places using scale=n option for division to work properly
		echo -e "Subject ID: "${subject_ID} '\t'\
                "Percentage mismatches: "${percent}"%"
	fi
done < blastoutput2.out

########
# Q11: # Allocate HSPs into small number of different groups based on scores
########

while read query_ID subject_ID percent_identity alignment_length mismatches gaps q_start q_end s_start s_end evalue bitscore
do
        if [[ "${query_ID}" != \#* ]]
	then
		evaluate=$(awk -v e=${evalue} 'BEGIN {print (e < 0.05)}') # output is 1/0 not TRUE/FALSE
		if [[ "${evaluate}" == 1 ]]
		then
			good=$(echo -e "${good}\nSubject ID: ${subject_ID}\tE-value: ${evalue}")
		elif [[ "${evaluate}" == 0 ]]
                then
                        bad=$(echo -e "${bad}\nSubject ID: ${subject_ID}\tE-value: ${evalue}") 
		fi
	fi
done < blastoutput2.out

echo "HSPs with E-value < 0.05: ${good}"
echo "HSPs with E-value > 0.05: ${bad}"

