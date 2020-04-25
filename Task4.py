"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
Telemarketers=set()  #set storing the numbers which could be telemarketers
avoid=set() # numbers which cannot be telemarketers, numbers to be avoided to be counted in telemarketers

for number in range(0,len(texts)): # adding all the numbers to be avoided from texts.csv
    avoid.add(texts[number][0])
    avoid.add(texts[number][1])
    
for number in range(0,len(calls)): # adding all the numbers to be avoided from calls.csv
    avoid.add(calls[number][1])
for number in range(0,len(calls)): #finding all Telemarketer numbers
    call=calls[number][0]
    if call not in avoid:
        Telemarketers.add(call)
SortTelemarketers=sorted(Telemarketers) #sorting the set

print("These numbers could be telemarketers: ")

for number in range(0,len(SortTelemarketers)): #printing telemarketer numbers
    print(SortTelemarketers[number])

#Shambhavi Awasthi Data Structures and Algorithms - NanoDegree
