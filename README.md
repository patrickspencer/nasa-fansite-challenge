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

# Bad parts

What makes this program slow is, one, it's written in python, and, two, we
read the entire list into memory. One way we could improve this is by reading
the file by chunks with something like the following 
(taken from http://stackoverflow.com/a/8009942)

Just reading the log.txt file line by line and regexing for something like
byte count takes about 60 seconds on my laptop.
