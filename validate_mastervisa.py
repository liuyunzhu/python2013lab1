# Filename: validate_mastervisa.py
# Author: Liu Yunzhu
# Centre No/Index No:
# Description: Validate a user input Master or VISA credit card number

import re

def validate(card):
    total = 0

    #Double the alternate digits starting from the first digit
    for a in range(0,len(card),2):
        # if double of the digit exceeds 9, minus 9 from result
        if int(card[a]) <= 4:
            total = total + int(card[a])*2
        else:
            total = total + int(card[a])*2 -9

    for b in range(1,len(card),2):
        total = total + int(card[b])

    # card is valid if remainder is 0 when total is divided by 10
    if total % 10 == 0:
        print ("credit card number is valid")
    else:
        print ("credit card number is invalid")

#main
card = input("enter card number: ")
card = re.sub("[^0-9]", "", card)
pattern = re.compile("^[4-5][0-9]{12,15}$")


if len(card)!=13 and len(card)!=16:
    print ("invalid input credit card number")

else:
    if int(card[0]) == 4 or int(card[0]) == 5:
        validate(card)
    else:
        print("invalid input credit card number")







