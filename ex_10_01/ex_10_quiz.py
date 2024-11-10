# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# many = dict()
# # Pull the hour out from line that starts with "From"
# for line in handle:
#     line = line.strip()
#     wds = line.split()
#     if len(wds)<3 or wds[0] != 'From':
#         continue
#     time = wds[5]
#     hour=time[:2]
#     many[hour] = many.get(hour, 0)+1
    
#     # print(hour)


# # Sort them from lowest to highest
# # tmp = dict()
# newlist = list()
# for k,v in many.items():
#     tup=(k,v)
#     newlist.append(tup)

# top=sorted(newlist)

# for v,k in top:
#     print(v,k)
    
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])