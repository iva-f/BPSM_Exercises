#!/usr/bin/python3

# initialise lists:
Q1=["Species D.melanogaster or D.simulans:"]; Q2=["Sequence length 90-110 nt:"]
Q3=["AT content < 0.5 and expression level > 200:"] 
Q4=["Gene names start 'k' or 'h' and not D.melanogaster:"]
Q5=["AT content high (>0.65), medium (0.45-0.65), low (<0.45):"]

with open("data.csv") as conn:
    data = conn.readlines() # read line-by-line and store as list
    for line in data: # lines contain 4 comma-delimited fields
        line = line.strip().split(",") # strip trailing \n; split into fields
        
        if line[0]=="Drosophila melanogaster" or line[0]=="Drosophila simulans":
            Q1.append(line[2])
                  
        if len(line[1]) > 90 and len(line[1]) < 110:
            Q2.append(line[2])

        AT = (line[1].count("a")+line[1].count("t"))/len(line[1])*100
        if AT < 50 and int(line[3]) > 200:
            Q3.append(line[2]+" (AT content: {0}%, expression level: {1})".format(round(AT,2), line[3]))

        if line[2].lower().startswith(("k","h")) and line[0] != "Drosophila melanogaster":
            Q4.append(line[2])

        if AT > 65:
            Q5.append("AT content of gene {} is high ({}%)".format(line[2], round(AT,2)))
        elif AT < 45:
            Q5.append("AT content of gene {} is low ({}%)".format(line[2], round(AT,2)))
        else:
            Q5.append("AT content of gene {} is medium ({}%)".format(line[2], round(AT,2)))

for i in [Q1,Q2,Q3,Q4,Q5]:
    for j in i:
        print(j)

