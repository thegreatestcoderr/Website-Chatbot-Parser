orignum = int(input("Enter the number to test if it is an Armstrong number: "))
counter = 0
d = orignum
while d != 0:
     d /= 10
     counter += 1

orignum = str(orignum)
x = int(orignum[0])
y = int(orignum[1])
z = int(orignum[2])
orignum = int(orignum)
a = x ** counter + y ** counter + z ** counter
if a == orignum:
    print("This is an Armstrong number.")
else:
    print("This is not an Armstrong number.")
