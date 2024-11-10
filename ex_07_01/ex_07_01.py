# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
add=0

# def addfloat(floatlist):
#     total=0.0
#     for num in list:
#         total +=num
#     return total

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        fnum=line.find(':')
        count=count+1
        # print(count)
        
        slnum=[float(line[fnum+1:].strip())]
        for value in slnum:
            add = add + value
            # print(add)
        
        
        
        # total = slnum + slnum
        
        # print(total)
    # print(line)
 
print(add/count)   
# Extract the floating value from each line

# Add the floating values (do NOT use sum) then get the average (count those lines)

print("Done")