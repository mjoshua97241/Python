name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# empty dict()
pro = dict()

# look for 'From' lines
for line in handle:
    line = line.strip()
    wds = line.split()
    if len(wds) < 3 or wds [0] != 'From':
        continue
    sender = wds[1]
    pro[sender] = pro.get(sender, 0)+1

# print(pro)
# take the 2nd word from 'From' lines

# read the dict() using the max loop
largest = None
bigword = None

for email, value in pro.items():
    if largest is None or value > largest:
        largest =value
        bigword = email

print(bigword, largest)
