# Filename: master_or_visa.py
# Author: Liu Yunzhu
# Centre No/Index No:
# Description: Test if the input credit card number belongs to MasterCard or VISA

import re

card = input("enter card number: ")
card = re.sub("[^0-9]", "", card)
pattern = re.compile("^[4-5][0-9]{12,15}$")

if len(card)!=13 and len(card)!=16:
    print ("input card number is neither MasterCard nor VISA")

else:
    if not pattern.match(card):
        print("input card number is neither MasterCard nor VISA")

    else:
        if int(card[0]) == 4:
            print ("input card number is VISA")
        elif int(card[0]) == 5:
            print("input card number is MasterCard")
        else:
            print("input card number is neither MasterCard nor VISA")

