#!/usr/bin/env python
# coding: utf-8

# In[7]:


# To view the formal proof and full logic behind this code, please see: https://github.com/webivorous/assignment-1-ai/blob/master/FormalProof.pdf

#Lists all the statements given in the problem

statement1="I am a human being"
statement2="I am good"
statement3="Good graders study well"
statement4="Humans love graders"
statement5="Every human does not study well"

#Here we are taking negation of statement 5 to be used ahead
negate_statement5="Every human study well"

#Explanation behind logic: We take negation of statement 5 i.e., and then take conjunction or AND with statement 3 or in other 
#words "Good graders study well" AND "Every human study well" which says that Every human is good grader and now using basic 
#propositional logic we can determine the truth value of this statement which is our required statement


count=0 #To keep track of truth values and determine number of times count occured


truth_table=[[1,1],[1,0],[0,0],[0,1]]  #List for generation of truth table

for value in truth_table:
    if value[0]==1:
        statement3="T"
    else: 
        statement3="F"
    if value[1]==1:
        statement5="T"
    else:
        statement5="F"
    if statement5=="T":
        negate_statement5="F"
    else:
        negate_statement5="T"

    for i in (statement3 and statement5):
        if i=="T":
            count+=1
            
#As we can see for the statement to be true it must be a tautology i.e., all values should have 'T', even a single 'F' will 
#result it to be not true. Which is the case here.


if count==len(truth_table):
    result="YES"
else:
    result="NO"
print("Is every human is a good grader? : ",result)

