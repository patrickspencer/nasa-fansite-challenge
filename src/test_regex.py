# str1 = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'
# str2 = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/" 200 6245'
# str3 = '215.145.83.92 - - [01/Jul/1995:00:00:41 -0400] "GET /shuttle/missions/sts-71/movies/movies.html" 200 3089'
# str4 = '220.169.39.23 - - [01/Jul/1995:00:00:41 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204'
# str5 = 'ppp-mia-30.shadow.net - - [01/Jul/1995:00:00:41 -0400] "GET /images/USA-logosmall.gif HTTP/1.0" 200 234'
str1 = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'
str2 = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/" 200 6245'
regex = '(.*?) - - \[(.*?)\] "(\w*?)\s(.*?)" (\d\d\d)\s(.+)'
groups1 = re.match(regex, str1).groups()
groups2 = re.match(regex, str2).groups()
# groups2 = re.match(regex, str2).groups()
# groups3 = re.match(regex, str3).groups()
# groups4 = re.match(regex, str4).groups()
# groups5 = re.match(regex, str5).groups()
print(groups1[3].split(' '))
print(groups2[3].split(' '))
# print(groups2)
# print(groups3)
# print(groups4)
# print(groups5[4].lstrip(' '))

# This was the regex that I used when I was just trying to capture the bytes
# It didn't show any performance increase from the other regex
# regex = '(.*)\"(.*)\"(.*)\s(\S*|-)(?:\n)'
