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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# PART A

areaCodes=[] # for storing all the area codes and mobile prefixes

for number in range(0,len(calls)):  #iterating over the calls.csv
    calling_number=calls[number][0]
    
    if calling_number.startswith("(080)"): #to check if the calling number is from bangalore
        
        receiving_number=calls[number][1]
        
        if receiving_number.startswith("("): # to find the area code for fixed line
            pos1=receiving_number.find("(")
            pos2=receiving_number.find(")")
            prefix=receiving_number[pos1:pos2+1]
            areaCodes.append(prefix)
            
        elif receiving_number.startswith("9") or receiving_number.startswith("7") or receiving_number.startswith("8"): #to check for mobile numbers
            prefix=receiving_number[0:4]
            areaCodes.append(prefix)
            
        elif receiving_number.startswith("140"): # area code for Telemarketers
            areaCodes.append("140")
            
SortedCodes=sorted(set(areaCodes)) #Finding sorted list of area codes with no duplicates

print("The numbers called by people in Bangalore have codes:")
for code in range(0,len(SortedCodes)): #Printing all area codes lexicographically
    print(SortedCodes[code])
    
FixedLineCallsFromBangalore=len(areaCodes)    #number of calls made with Bangalore Area Code

#PART B    

FixedLineCallReceive_frombangalore=0   #number of calls made as well as received from Bangalore area code

for calling in range(0,len(calls)):
    call=calls[calling][0]
    receive=calls[calling][1]
    if call.startswith("(080)"):
        if receive.startswith("(080)"):
            FixedLineCallReceive_frombangalore=FixedLineCallReceive_frombangalore+1
            
percentage = round((FixedLineCallReceive_frombangalore / FixedLineCallsFromBangalore)*100,2)

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))


# Shambhavi Awasthi - Data Structures and algorithms - Nanodegree