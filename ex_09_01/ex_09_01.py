fname = input('Enter file: ')
if len(fname) < 1: fname = 'clown.txt'

fhand = open(fname)

# empty dictionary
many = dict()

for line in fhand:
    line = line.rstrip()
    
    # break the lines into words
    wds = line.split()
    # print(wds)
    
    for w in wds:
        # print('======>',w)
        # print('before', many)
        
        # oldvalue = 0
        # if w in many: oldvalue = many[w]
        # oldvalue = many.get(w,0)
        
        many[w] = many.get(w,0) + 1

        
# print(many)

# Find the word with the largest count

largest = None
bigword = None

for cle, valeur in many.items():
    # print(cle,valeur)
    if largest is None or valeur > largest :
        largest = valeur
        bigword = cle
        
        
print(bigword, largest)