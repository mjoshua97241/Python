fname = input("Enter file name: ")
fh = open(fname)
txt=fh.read()

#empty for storing string later
lst = list()

words=txt.split()
unique = set(words)
# print(unique)

for line in unique:
    lst.append(line)
# print(words)
sort=sorted(lst)
print(lst)
print(sort)

# loop over the lists
# for line in fh:
#     sline=line.rstrip()
#     words = [sline.split()]
#     # print(sline)
#     print(words)
    
# print(line.rstrip())

# # The content of romeo.txt as a multi-line string
# text = """But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief"""

# # Step 1: Split the words into a list
# words = text.split()

# # Step 2: Sort the words alphabetically (case-insensitive sorting)
# sorted_words = sorted(words)

# # Print the sorted list
# print(sorted_words)
