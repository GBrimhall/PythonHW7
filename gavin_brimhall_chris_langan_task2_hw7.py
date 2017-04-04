#!/usr/bin/env python3
import sys
import re


store_bar_code = [ ("||:::"), (":::||"),("::|:|"), ("::||:"), (":|::|"), (":|:|:"), (":||::"), ("|:::|"), ("|::|:"), ("|:|::") ]

def printDigit(d):
    """
    Function that prints the digit to bar code
    """
    
    for i in d:
        print(store_bar_code[int(i)], end='')

def printBarCode(zipCode):
    """
    Function that validates input, and parses the numbers
    calls printDigit to print the zip code numbers and the checkDigit
    """


    
    #Zip code validation and print
    sbc = store_bar_code
    if zipCode.isdigit(): 
        if len(zipCode) == 5:
            print("|",end='')
            printDigit(zipCode)
            print(sbc[checkDigit(zipCode)] + "|")
        else:
            print("Zip code is not 5 digits")
    else:
        print("Zip code is not all numeric")


def checkDigit(zipCode):
    """
    Function to calculate the checkDigit
    """
    
    #add all the digits
    cd = [ int(i) for i in zipCode ]
    return (10 - sum(cd)) % 10


#Main function
def main():
    """
    Main function
    """

if __name__=='__main__':
    #Call main
    main()
