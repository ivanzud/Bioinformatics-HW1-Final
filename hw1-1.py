#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Module sys has to be imported:
import sys                

# Iteration over all arguments:

#print(sys.argv[1])
import numpy as np
from numpy.random import choice
import pandas as pd

#seq_len, int_a, int_c, int_g, int_t, num_seq, mutation_p, output_file = input().split()
seq_len = int(sys.argv[1])
int_a = int(sys.argv[2])
int_c = int(sys.argv[3])
int_g = int(sys.argv[4])
int_t = int(sys.argv[5])
num_seq = int(sys.argv[6])
mutation_p = float(sys.argv[7])
output_file = str(sys.argv[8])

# seq_len = 10000
# int_a = 25
# int_c = 25
# int_g = 25
# int_t = 25
# num_seq = 10
# mutation_p = 0.005
# output_file = "outputfile"

sum = int_a + int_c + int_g + int_t
seq_list = []
seq_def = ['A','C','G','T']
probabilities = [int_a/sum, int_c/sum, int_g/sum, int_t/sum]


# In[2]:


#probability of replace or delete
bool_list = ["replace", "delete"]
bool_prob = [0.5, 0.5]
#choice(bool_list, p = bool_prob)

#probability of mutate or not
mutate_choice = [True, False]
mutate_prob = [mutation_p, (1-mutation_p)]
#choice(mutate_choice, p=mutate_prob)


# In[ ]:





# In[3]:


#creates first sequence
for l in range(1):
    temp_list = []
    for x in range(seq_len):    
        
        temp_list.append(choice(seq_def, p=probabilities))
    
    seq_list.append(temp_list)


# In[4]:


import copy
#copies first seq to others
for a in range(num_seq - 1):
    seq_list.append(copy.deepcopy(seq_list[0]))


old_list = copy.deepcopy(seq_list)


# In[5]:



#from itertools import islice


# In[6]:


# len(seq_list[0])
for x in range(1, num_seq):    
   # print(x)
    for b in range(len(seq_list[x])):
        check_mutate = choice(mutate_choice, p=mutate_prob)
        
        if(b <= len(seq_list[x])):
            
            if (check_mutate):
                #print("mutate")
                #print(b)
                check = choice(bool_list, p = bool_prob)
                #check == "replace"
                if(check == "replace"):
#                         print("length of list replace", len(seq_list[x]))
#                         print("index of replace",b)
#                         print("replace")
    #                     print("sequence", x)
    #                     print("Index,",b)
    #                     print("Original:",seq_list[x][b])
                        seq_list[x][b] = choice(seq_def, p=probabilities)
    #                     print("Modified:",seq_list[x][b])
                elif (check == "delete"):
                        #print("delete")
                        #print("")
#                         print("index",b)
                        seq_list[x].pop(b)

                        #index
                        #seq_len = seq_len - 1
#                         print(len(seq_list[x]))
    #seq_len = 10000
        


# In[7]:


#old_list == seq_list
len(seq_list[8])


# In[8]:


name_list = []
for i in range(num_seq):
    name_list.append("Seq:" + str(i+1))


# In[9]:


# print(name_list)
#def sequence_generator():
    


# In[10]:


output_file = output_file + ".fasta"
ofile = open(output_file, "w")

for i in range(num_seq):

    ofile.write(">" + name_list[i] + "\n" +''.join(seq_list[i]) + "\n")

ofile.close()


# In[11]:



# ofile = open(output_file, "r")
# ofile_content = ofile.read()
# # print(ofile_content)
# ofile.close()


# In[12]:


# from Bio import SeqIO
# #help(SeqIO.convert)


# In[13]:


# from Bio import SeqIO
# input_filename = "input.txt"
# output_filename = "outputfile.fasta"
# count = SeqIO.convert(input_filename, "gb", output_filename, "fasta")
# print(str(count) + " records converted")


# In[ ]:




