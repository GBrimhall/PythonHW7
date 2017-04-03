#!/usr/bin/env python3
import sys
import re

def printDigit(d):
    """
    Function that prints the digit to bar code
    """



def printBarCode(zipCode):
    """
    Function that validates input, and parses the numbers
    calls printDigit to print the zip code numbers and the checkDigit
    """
    
    for i in zipCode:
        checkDigit = (10 - sum(zipCode[i])%10)


    #Zip code validation
    if (re.match("^[0-9]*$", zipCode): 
        if(Len(zipCode) == 5):
            print("|")
            printDigit(zipCode)
            print(checkDigit + "|" )
            else:
                print("Zip is not all numeric")
    else:
        print("Zip code is not all numeric")








#Main function
def main():
    """
    Main function
    """

if __name__=='__main__':
