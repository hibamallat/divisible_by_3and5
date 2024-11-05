try:
    #The user should enter a number
    num_check = int(input("Enter a number to check all numbers from 1 to your input that are divisible by 3 and 5: "))
    if num_check < 0:
        print("INVALID: Enter a positive number")

    for i in range (1, num_check + 1):
        # Check if the current number i is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0 :
            print(i, end = ' ') # Print i without a newline
    print("\nThe following numbers are divisible by both 3 and 5. Thank you for your input")
except ValueError:
    print("INVALID: Enter a number")