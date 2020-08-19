#!/usr/bin/env python
# coding: utf-8

# In[97]:


# Module sys has to be imported:
import sys                

# Iteration over all arguments:

#print(sys.argv[1])

input_file = str(sys.argv[1])
length_min = int(sys.argv[2])
length_max = int(sys.argv[3])
output_file = str(sys.argv[4])


# input_file = "inputfile"
# length_min = 100
# length_max = 150
# output_file = "outputfile"


# In[98]:


from numpy.random import choice
import random
# def randsplit(lst):
#     out = [[]]
#     for item in lst:
#         out[-1].append(item)
#         if random.choice((True, False)):
#             out.append([])
#     return [l for l in out if len(l)]


# In[1]:


from itertools import islice
from random import randint

def random_chunk(li, min_chunk, max_chunk):
    it = iter(li)
    while True:
        nxt = list(islice(it,randint(min_chunk,max_chunk)))
        if nxt:
            yield nxt
        else:
            break


# In[2]:


from random import randint

def random_list_split(data):
    split_list = []
    L = len(data)
    i = 0
    while i < L:
        r = randint(1,L-i)
        split_list.append(data[i:i+r])
        i = i + r
    return split_list


# In[101]:


# from Bio import SeqIO

# fasta_sequences = SeqIO.parse(open(input_file),'fasta')
# with open(input_file) as in_file:
#     for fasta in fasta_sequences:
#         name, sequence = fasta.id, str(fasta.seq)
#         new_sequence = some_function(sequence)
#         write_fasta(outputfile)


# In[102]:


# from Bio import SeqIO
# seq_dict = {rec.id : rec.seq for rec in SeqIO.parse("inputfile.fasta", "fasta")}


# In[103]:


# seq_dict
# dictlist = []
# for key, value in seq_dict.items():
#     temp = [value]
#     dictlist.append(temp)

# dictlist


# In[104]:


# rand_list = randsplit(dictlist)


# In[105]:


# len(rand_list)
# rand_list


# In[106]:


seq_list =[]
input_file = input_file + ".fasta"
ofile = open(input_file, "r")
ofile_content = ofile.read()
#print(ofile_content)
words = str.split(ofile_content)
#print(words)
for i in range(len(words)):
    if("S" not in words[i]):
        #print("hello")
        seq_list.append(words[i])
ofile.close()


# In[107]:


#len(seq_list)


# In[108]:


partitioned_list = []
for i in range(len(seq_list)):
    temp_list = []
    temp_list = list(random_chunk(seq_list[i], min_chunk=length_min, max_chunk=length_max))
    #temp_list = random_list_split(seq_list[i])
    partitioned_list.append(temp_list)
    


# In[109]:


#len(partitioned_list[3])


# In[110]:


#flattened list of 10 partitions
#len(partitioned_list)
flat_list = [item for sublist in partitioned_list for item in sublist]
#flat_list
#len(flat_list)


# In[111]:


#going through flattened list to check for sequences within the min and max
new_list = []
count = 0
for item in flat_list:
    if len(item) >= length_min and len(item) <= length_max:
        count = count + 1
        new_list.append(item)
        #print(len(item))
#       if len(item) > length_max:
#         print(len(item))
        
#print(count)


# In[112]:


#len(new_list)


# In[113]:


name_list = []
for i in range(len(new_list)):
    name_list.append("Seq:" + str(i+1))


# In[114]:


#len(name_list)


# In[115]:


output_file = output_file + ".fasta"
o_file = open(output_file, "w")

for i in range(len(new_list)):

    o_file.write(">" + name_list[i] + "\n" +''.join(new_list[i]) + "\n")

o_file.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




