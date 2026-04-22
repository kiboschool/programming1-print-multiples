# Write your code here

# Print numbers 1 to 100
for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print (i, "is a multiple of 3 and 5")
    elif i % 3 == 0:
        print (i, "is a multiple of 3")
    elif i % 5 == 0:
        print (i, "is a multiple of 5")
    else:
        print(i)

# For multiples of 3, print "X is a multiple of 3"
# For multiples of 5, print "X is a multiple of 5"