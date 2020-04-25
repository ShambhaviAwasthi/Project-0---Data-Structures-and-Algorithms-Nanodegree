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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
Different_numbers=set() #creating a set to store unique numbers

number_call=0 # a variable with a number from call.csv
number_text=0  # a variable with a number from text.csv

for number_call in range(0,len(calls)-1): # loop to find unique numbers in call.csv and store them in set
    Different_numbers.add(calls[number_call][0])
    Different_numbers.add(calls[number_call][1])
    
for number_text in range(0,len(texts)-1): # loop to find unique numbers in text.csv and store them in set
    Different_numbers.add(texts[number_text][0])
    Different_numbers.add(texts[number_text][1])
    
NoOfDifferentNumbers=len(Different_numbers) #size of set gives the number of different telephone numbers
print("There are {} different telephone numbers in the records.".format(NoOfDifferentNumbers))

#Shambhavi Awasthi
#Data Structures and Algorithms - Nanodegree