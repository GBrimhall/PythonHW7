#!/usr/bin/env python3
import sys
import re


def printDigit(d):
    """
    Function that prints the digit to bar code
    """

    #Print the bar code according to the number in the zip code
    for j in d:
        if d[j] == 0:
            print("||:::")
        elif d[j] == 1:
            print(":::||")
        elif d[j] == 2:
            print("::|:|")
        elif d[j] == 3:
            print("::||:")
        elif d[j] == 4:
            print(":|::|") 
        elif d[j] == 5:
            print(":|:|:")
        elif d[j] == 6:
            print(":||::")
        elif d[j] == 7:
            print("|:::|")
        elif d[j] == 8:
            print("|::|:")
        elif d[j] == 9:
            print("|:|::")


def printBarCode(zipCode):
    """
    Function that validates input, and parses the numbers
    calls printDigit to print the zip code numbers and the checkDigit
    """
    
    #add all the digits
    for i in zipCode:
        checkDigit = (10 - sum(zipCode[i])%10)


    #Zip code validation and print
    if (re.match("^[0-9]*$", zipCode): 
        if(Len(zipCode) == 5):
            print("|")
            printDigit(zipCode)
            print(checkDigit + "|" )
            else:
                print("Zip code is not 5 digits")
    else:
        print("Zip code is not all numeric")


        
#Main function
def main():
    """
    Main function
    """

if __name__=='__main__':
