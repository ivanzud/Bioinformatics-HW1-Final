#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Module sys has to be imported:
import sys                

# Iteration over all arguments:

#print(sys.argv[1])

input_file = str(sys.argv[1])
p1 = int(sys.argv[2]) #match score
p2 = int(sys.argv[3]) #replace score
p3 = int(sys.argv[4]) #delete score
output_file = str(sys.argv[5])

#for debugging purposes
# p1 = 1
# p2 = -1
# p3 = -3


# input_file = "partitionedfile"
# output_file = "Final_outputfile"


# In[6]:


#opens and stores fasta sequences in list

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


# In[8]:


#len(seq_list[0])
# seq_list = list(dict.fromkeys(seq_list))


# In[9]:


# new_frag
# seq_list = seq_list[20:30]
# print(seq_list)


# In[10]:


# from Bio import pairwise2
# from Bio.pairwise2 import format_alignment

# seq1 = 'AGCTTAGCCTAATAAA'
# seq2 = 'TTAGCATAATCAGAAA'

# alignments = pairwise2.align.globalms(seq1, seq2, 1, -1, -3, -3,
#                                       penalize_end_gaps=False, one_alignment_only=True)
# print(format_alignment(*alignments[0]))


# In[11]:


# formatted = format_alignment(*alignments[0])
# for alignment in alignments:
#     print(alignment)
def consensus(sequence_1, sequence_2):
    consensus_sequence = ''
    for index, amino_acid in enumerate(sequence_1):
        if amino_acid == sequence_2[index]:
            consensus_sequence += amino_acid
        elif amino_acid == '-' and sequence_2[index] != '-':
            consensus_sequence += sequence_2[index]
        elif sequence_2[index] == '-' and amino_acid != '-':
            consensus_sequence += amino_acid
        elif amino_acid != sequence_2[index]:
            consensus_sequence += sequence_2[index]
    return consensus_sequence


# In[12]:


# alignments[0][0]
# cp = consensus(alignments[0][0], alignments[0][1])


# In[13]:


# cp


# In[14]:


# cleaned_alignments = pairwise2._clean_alignments(alignments)
# print(format_alignment(*alignments[0]))


# In[15]:


# for alignment in cleaned_alignments:
#     print(alignment)


# In[16]:


new_frag = []


# In[17]:


from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import time
#start_time = time.time()

length_of_seq = len(seq_list)

max_alignment_score = 0
first_seq_index = 0
second_seq_index = 0
max_alignment = 0
for i in range(length_of_seq):
    
    for j in range(length_of_seq):
        alignment_temp = pairwise2.align.globalms(seq_list[i], seq_list[j], p1, p2, p3, p3,
                                              penalize_end_gaps=False, one_alignment_only=True)
        length = alignment_temp[0][2]
        #print("Iterated %s times" % j)
        
        if(length > max_alignment_score):
            max_alignment_score = length
            max_alignment = alignment_temp
            first_seq_index = i
            second_seq_index = j
            #print("Iterated max %s times" % j)
            
#cp gets consensus sequence of two sequences with max alignment score
cp = consensus(max_alignment[0][0], max_alignment[0][1])
new_frag = cp
seq_list.pop(first_seq_index)
seq_list.pop(second_seq_index)


#print("--- %s seconds ---" % (time.time() - start_time))


# In[18]:


#new_frag


# In[19]:



import time

def calc_merge_seq(new_frag, max_Score, seq_list_temp):
    start_time = time.time()
    length_of_seq = len(seq_list_temp)       
    count = 0
    max_alignment_score = 0
    max_alignment = 0
    for i in range(length_of_seq):
        
        alignment_temp = pairwise2.align.globalms(new_frag, seq_list_temp[i], p1, p2, p3, p3,
                                              penalize_end_gaps=False, one_alignment_only=True)
        length = alignment_temp[0][2]
        
        
        if(length > max_alignment_score):
            max_alignment = alignment_temp
            max_Score = length
            count = i

        
    
    if(max_Score > 0):
            # print("Max score is:", max_Score)
            # print("Old Frag:", new_frag)
            # print("Original length of Fragment:", len(new_frag))
            # print("Length of popped sequence: ", len(seq_list_temp[count]))
            # print("Popped a new sequence:", seq_list_temp[count])
            
            cp = consensus(max_alignment[0][0], max_alignment[0][1])
            new_frag = cp
            # print("New length of Fragment:", len(new_frag))
            
            # print("New Frag:", new_frag)
            seq_list_temp.pop(count)
            # print("Length of seq_list", len(seq_list_temp))
            length_of_seq = length_of_seq - 1    
            # print("--- %s seconds ---" % (time.time() - start_time))
            
    elif(max_alignment_score < 0):
        # print("Returns if max < 0") 
        return new_frag
        
    if(length_of_seq > 1):
        # print("Runs recursion")
        return calc_merge_seq(new_frag, max_Score, seq_list_temp)
    
    elif(length_of_seq == 1):
        # print("Returns if length == 1") 
        return new_frag
    
new_list = []
new_list = calc_merge_seq(new_frag, max_alignment_score, seq_list)


# In[17]:


#new_list


# In[18]:


# check_list = "ATAGACGTGTCCTGAGCTATATCGACTCGTGTTGCGTGGGTGGTTAAGATCGCAATATTTTGGCCCTAGACTCTGCGCCCGTAGAAGCTAACACAGGGGTTAATGGAGCCGCGGGCGCGGCTAAAATCTCTCTCTACGCATTTTTCGAAGTATGACGTATGTGAGGATACTCATCACGCAAATCTGTCCTCTGAATCGGC"
# new_list == check_list


# In[ ]:


output_file = output_file + ".fasta"
o_file = open(output_file, "w")

o_file.write(">" + "CombinedSequence1" + "\n" +''.join(new_list) + "\n")

o_file.close()


# In[ ]:


# seq_list =[]
# output_file = "Final_outputfile.fasta"
# ofile1 = open(output_file, "r")
# ofile_content1 = ofile1.read()
# #print(ofile_content)
# words1 = str.split(ofile_content1)
# #print(words)
# for i in range(len(words1)):
#     if("S" not in words1[i]):
#         #print("hello")
#         seq_list.append(words1[i])
# ofile1.close()


# In[ ]:


# words1


# In[ ]:




