import re

name = input("Enter file: ")
if len(name) <1:
    name = "regex_sum_2096331.txt"
handle = open(name)

many = list()
for line in handle:
    line = line.rstrip()
    findnum=re.findall('[0-9]+', line)
    
    if len(findnum) <1 : continue
    
    
    many.extend(map(int, findnum))
    
total = sum (many)
print(total)
