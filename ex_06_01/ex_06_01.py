# text = "X-DSPAM-Confidence:    0.8475"

# ipos = text.find(':')
# # print(ipos)
# sl=float(text[ipos+1:].strip())
# print(sl)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])