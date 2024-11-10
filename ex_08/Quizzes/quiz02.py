# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"

# fh = open(fname)
# count = 0

# for line in fh:
#     line=line.strip()
#     wds = line.split()
#     if len(wds) <3 or wds[0] != 'From':
#         continue
#     count = count + 1
#     print(wds[1])

# print("There were", count, "lines in the file with From as the first word")

# def find_long(array_string):
#     return print(max([len(string) for string in array_string.split()]))

# find_long('Mathemtacis requires a small does, not a genius, but of imaginative freedom which, in a larger does, would be instantly')

basket = ['apples', 'oranges', 'mangoes']
basket[2] = 'grapes'

print(basket)