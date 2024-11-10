fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'

fhand = open(fname)

# empty dictionary
many = dict()

for line in fhand:
    line = line.rstrip()
    
    # break the lines into words
    wds = line.split()
    
    for w in wds:  
        many[w] = many.get(w,0) + 1

        


# Find the top 5 word by frequency

tmp = dict()
newlist = list()

# go over the tuples to interchange the values and the keys
for k,v in many.items():
    tup=(v,k)
    
    #store in the newlist()
    newlist.append(tup)

# sort them but in reverse - highest to lowest
cool = sorted(newlist, reverse=True)

# revert the values and keys to keys and values, get only the first/top 5
for v,k in cool[:5]:
    print(k,v)

