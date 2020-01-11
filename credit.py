Input = input("Number: ")
try:
   val = int(Input)
except ValueError:
   print("INVALID")
   exit()
Number = int(Input)
# Check if the card is even eligible to be in the range of a 13 digit to 16 digit credit card type
if Number >= 1000000000000 and Number < 10000000000000000:
    Card = []
    # Create a list storing each digit as integer
    for digit in Input:
        num = int(digit)
        Card.append(num)
    # Check if the card is a VISA
    if Number >= 1000000000000 and Number < 10000000000000:
        # Applying Luhn's Algorithm
        sum1 = 0
        for i in range(0, 14, 2):
            sum1 += Card[i]
        for i in range(1, 13, 2):
            if (2 * Card[i]) >= 10:
                new = (2 * Card[i]) % 10 + 1
            else:
                new = 2 * Card[i]
            sum1 += new
        # Checking the Result of the Algorithm and the numbering convention for 13 digit VISA
        if sum1 % 10 == 0 and Card[0] == 4:
            print("VISA")
        else:
            print("INVALID")
    # Check if the card is a American Express
    elif Number >= 100000000000000 and Number < 1000000000000000:
        # Applying Luhn's Algorithm
        sum2 = 0
        for i in range(0, 16, 2):
            sum2 += Card[i]
        for i in range(1, 15, 2):
            if (2 * Card[i]) >= 10:
                new = (2 * Card[i]) % 10 + 1
            else:
                new = 2 * Card[i]
            sum2 += new
        # Checking the Result of the Algorithm and the numbering convention for AMEX
        if sum2 % 10 == 0 and Card[0] == 3 and (Card[1] == 4 or Card[1] == 7):
            print("AMEX")
        else:
            print("INVALID")
    # Check if the card is a MasterCard or perhaps a 16 digit VISA
    elif Number >= 1000000000000000 and Number < 10000000000000000:
        # Applying Luhn's Algorithm
        sum3 = 0
        for i in range(1, 17, 2):
            sum3 += Card[i]
        for i in range(0, 16, 2):
            if (2 * Card[i]) >= 10:
                new = (2 * Card[i]) % 10 + 1
            else:
                new = 2 * Card[i]
            sum3 += new
        # Checking the Result of the Algorithm and the numbering convention for MasterCard
        if sum3 % 10 == 0 and Card[0] == 5 and (Card[1] == 1 or Card[1] == 2 or Card[1] == 3 or Card[1] == 4 or Card[1] == 5):
            print("MASTERCARD")
        # Checking the Result of the Algorithm and the numbering convention for 16 digit VISA
        elif sum3 % 10 == 0 and Card[0] == 4:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")
else:
    print("INVALID")
