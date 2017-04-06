# NASA Fansite Challenge for Insight

This program is a pure python3 program. To run the file enter `python3
src/process_log.py`

Tests are included at `src/tests.py`

I know python isn't the fastest language and if I could I would write this in
a language like go but for now it seems. Fast enough. It takes about 5
minutes to process the whole log file with all 4 features, about 2 minutes of
this is reading `log.txt` into a memory. This isn't ideal but it was easier
to program doing this. In the future I would work on reading the log file in
as a stream.

## Features

Only the original four features were implemented. I have ideas for more
features but I didn't have time to put them in. 

One interesting thing you can do is find the busiest time interval for any
length of time. This feature (number 3) is actually pretty fast too, even for
python. On my computer it takes less than a second to find the busiest hours
in the full log file. To change the time interval length, change the attribute
`time_interval = 3600` in `src.process_log` line 51 to the number of seconds
you want the interval to be.

### Feature 1

This takes about 5 seconds on my computer.

#### Explanation of algorithm

### Feature 2

This takes about 2 minutes on my computer. This is by far the longest time of
all the features.

#### Explanation of algorithm

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

### Feature 3

This takes about 2 seconds on my computer

Running this is feature is the fastest of all the features in this program. It
takes about 8.5 seconds to run after each line from the log file has been
loaded into memory.

#### Explanation of algorithm

For this feature, we can view the log as an increasing sequence of unix timestamps 
l = (t[0], t[1], ..., t[n]).

The algorithm is the following:

d = time delta in seconds (we will use 3600 for an hour)

s = starting time
e = ending time = s+3600
I = current interval = [s, e]

while ending time is less t[n]
    delete all t[i] in I that shouldn't be there
    find all t[i] not in I that should be in I
    count elements in I
    Compare count to a top 10 list
    s = s+1

I was able to turn this into a indices counting game which is why this
particular feature is so fast. This algorithm is implemented in the
function `src.lib.find_busiest_intervals()`.

### Feature 4

This takes about 2 seconds on my computer

