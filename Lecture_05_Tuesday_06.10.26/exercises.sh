#!/bin/bash

######
# Q1 #
######

unset counter

while IFS=$'\t' read name email city birth_day birth_month birth_year country
do
	if test "${name}" != "name" && test ${#name} != 0
	then
		counter=$((counter+=1))
		echo -e "$counter \t $country"
	fi
done < example_people_data.tsv

######
# Q2 #
######

unset counter

while IFS=$'\t' read name email city birth_day birth_month birth_year country
do
        if test "${name}" != "name" && test ${#name} != 0
        then
                counter=$((counter+=1))
                echo -e "$counter \t $name \t $city \t $country"
        fi
done < example_people_data.tsv

######
# Q3 #
######

#unset counter

#while IFS=$'\t' read name email city birth_day birth_month birth_year country
#do
#        if test "${name}" != "name" && test ${#name} != 0
#        then
#                counter=$((counter+=1))
#                echo -e "$counter \t $name \t $city \t $country" >> "Question_3/${country}.txt"
#        fi
#done < example_people_data.tsv

######
# Q4 #
######

unset counter

while IFS=$'\t' read name email city birth_day birth_month birth_year country
do
        if test "${name}" != "name" && test ${#name} != 0; then
                if test ${birth_month} == 10; then
			counter=$((counter+=1))
			people=$(echo -e "${people}\n${name}\t${country}")
		fi
        fi
done < example_people_data.tsv
echo -e "Number of people born in October: $counter"
echo "${people:1}" # do not echo first \n

######
# Q5 #
######

######
# Q6 #
######
