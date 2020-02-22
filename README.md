## Description
This is my program wrote for CS50x Pset6 on edX in Python. It checks an user input of a credit card number is valid or not and further evaluates it to the card's corresponding company or lack thereof. The program incorporated mathematical calculation based on Luhn’s Algorithm by Hans Peter Luhn from IBM. Only 4 outputs are available: VISA, AMEX(American Express), MASTERCARD, and INVALID. With the power of python, the program is now ever more succinct and efficient compared to the previous hundreds of lines!

## Usage
```
$ python credit.py
Number: [Input a credit card number from American Express, MasterCard(first digit being 5), Visa(13 digit or 16 digit)]
```

## What I have learned 
* By transfering each digit in the number into an array of integers, I found that I can directly access each digit of a number intuitively using the array
* Applying Luhn's Algorithm in Python
