#The user must enter a number x
x= int(input("Enter x: "))

for i in range (x+1):
    # Check if the current number i is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0 : 
        print(i, end = ' ') # Print i without a newline