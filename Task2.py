"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
time={}
for i in range(0,len(calls)):
    if calls[i][0] in time:
        time[calls[i][0]] += int(calls[i][3])
    if calls[i][1] in time:
        time[calls[i][1]]+=int(calls[i][3])
    if calls[i][0] not in time:
        time[calls[i][0]]=int(calls[i][3])
    if calls[i][1] not in time:
        time[calls[i][1]]=int(calls[i][3])
    
max_key = max(time, key=time.get) #finding max key
print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(max_key, time[max_key]))

#Shambhavi Awasthi
#Data Structures and Algorithms - NanoDegree