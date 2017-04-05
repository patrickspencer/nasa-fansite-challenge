Added folders:

`insight_testsuite/local/`: tests used my own use, as opposed to grading
purposed on Insight's side


## Feature 2

We are supposed to find the 10 resources that take up the most bandwidth. We
use the simple formula `(bytes per resource)(times the resources were
downloaded)`. The time period is the whole period covered by the logs. We
don't measure bandwidth used over an arbitrary time interval but this would be
a useful feature in the future.

We take the first resource in the first request and search the entire file for
all requests with that resource and take out each line with that resource. We
count up the amount of bytes used for that resource and then look for all
request for the next resources over this pruned list. This algorithm is
O(nlog(n)).

# Feature 4


Running this is feature is the fastest of all the features in this program. It
takes about 8.5 seconds to run after each line from the log file has been
loaded into memory.

## Explanation of algorithm

For this feature, we can view the log as an increasing sequence of unix timestamps 
l = (t[0], t[1], ..., t[n]).

The algorithm is the following:

d = time delta in seconds (we will use 3600 for an hour)

s = starting time
e = ending time = s+3600
I = current interval = [s, e]
current 

while ending time is less t[n]
    delete all t[i] in I that shouldn't be there
    find all t[i] not in I that should be in I
    count elements in I
    Compare count to a top 10 list
    s = s+1

max_time = t[n]
s = t[m]
e = t[m] + 3600

while e < max_time
    
    Find largest i so that t[i] < e
    find all t[i] not in I that should be in I
    count elements in I
    Compare count to a top 10 list
    s = s+1
    e = t[m] + 3600

# Bad parts

What makes this program slow is, one, it's written in python, and, two, we
read the entire list into memory. One way we could improve this is by reading
the file by chunks with something like the following 
(taken from http://stackoverflow.com/a/8009942)

Just reading the log.txt file line by line and regexing for something like
byte count takes about 60 seconds on my laptop.
