#!/usr/bin/env python3
import sys
from urllib.request import urlopen
import gavin_brimhall_chris_langan_task2_hw7

def openFile(url):

    #COMMENT FOR PROFESSOR/GRADER
    #At the time of writing this program, the required csv file, barCodeData.txt
    #is inaccessable. When attempting to get to the file via the url provided in the
    #homework description the webpage 404's. Because of this, the program runs off of
    #a local copy of the file, which is included

    url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt"
    
    #open file and parse the zip code
    with urlopen(url) as barCode:
    #with open('barCodeData.txt','r') as barCode:
        for line in barCode:
            print(line.decode("utf-8").strip()) 
            gavin_brimhall_chris_langan_task2_hw7.printBarCode(line.decode("utf-8").strip())
            print('')
        
    #Prompt the user to input a zip code
    getZip = input("Enter in a zip code: ")
    gavin_brimhall_chris_langan_task2_hw7.printDigit(getZip)
    print('')

#main function
def main():
    """
    Main function -> controls other module
    """
    
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "http//icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt"
        openFile(url)
        print('')


if __name__=='__main__':
    main()
    exit(0)


