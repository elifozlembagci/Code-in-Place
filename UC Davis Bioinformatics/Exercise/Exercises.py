#Exercise 1 - Counting bases

#Now that you’ve learned the basics of programming, it’s time to write some beginning code. Let’s write a program that will print the count for each nucleotide in a DNA sequence. You will need to use loops and a dictionary. You are not allowed to use the “count” string method. Create the program in a new file called “counts.py”. You can use this sequence to begin with:

#CGGTAGTCGAGCTGCGGATATAATATGCATATAGATCGCACGCTAGCTCATAAAAGCATGCATGCGGCTAGCTGCTGATCGTGTCG

#Hints:

#First put the sequence in a variable. 
#Iterate over each character in the sequence using a loop.
#Add the counts of each letter to a dictionary where the keys are the letters and the counts are the values.
#Print out the dictionary using a loop.


seq = "CGGTAGTCGAGCTGCGGATATAATATGCATATAGATCGCACGCTAGCTCATAAAAGCATGCATGCGGCTAGCTGCTGATCGTGTCG"

counts={}
for letter in seq:
    if (letter not in counts):
        counts[letter] = 1
    else:
        counts[letter] += 1

for letter in counts.keys():
    print(letter+" "+str(counts[letter]))


import this