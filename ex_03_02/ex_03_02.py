sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh=float(sh)
    fr=float(sr)
except:
    print("Error, please enter numeric input")
    
    # To avoid continue on the next line of block
    quit()

print(fh,fr)
if fh>40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr *0.5)
    xp=reg+otp
else:
    #print("Regular")
    xp=fh*fr

#convert to int by using float()
xp = float(sh) * float(sr)
print("Pay:",xp)