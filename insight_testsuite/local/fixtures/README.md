`domain_freq.txt`: a file for testing that the function for counting the
frequency of domains is actually working. The file lookes lik this:

```
domain_a - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
domain_a - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
domain_a - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
domain_a - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
domain_a - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
domain_b - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
domain_b - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
domain_b - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
domain_b - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
.
.
.
domain_m - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/technology/images/sts_spec_6-small.gif HTTP/1.0" 200 47145
```

the frequency chart of the domains is the following:

```
domain_a: 5
domain_b: 4
domain_c: 2
domain_d: 1
domain_e: 7
domain_f: 6
domain_g: 1
domain_h: 8
domain_i: 1
domain_j: 3
domain_k: 12
domain_l: 9
domain_m: 11
domain_n: 14
```

so the top 10 most frequent domains should be the following:
```
domain_n: 14
domain_k: 12
domain_m: 11
domain_l: 9
domain_h: 8
domain_e: 7
domain_f: 6
domain_a: 5
domain_b: 4
domain_j: 3
```

