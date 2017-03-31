#!/usr/bin/env python3
import sys
import gavin_brimhall_chris_langan_task1_hw7

def main():
	"""
	Main function, controls the other module, cleans input
	"""

	#COMMENT FOR PROFESSOR/GRADER
	#At the time of writing this program, the required csv file, minivanTest.csv
	#is inaccessable. When attempting to get to the file via the url provided in the
	#homework description the webpage 404's. Because of this, the program runs off of
	#a local copy of the file, which is included

	i = 1
	with open('minivanTest.csv','r') as minivanFile:
		for line in minivanFile:
			print ('Reading record ', i)
			lineWords = line.split()
			lineWords = [w.replace(',', '') for w in lineWords]
			if lineWords[0] == 'H1':
				print ('Header found, skipping')
				del lineWords
			elif lineWords[0] == 'R1':
				del lineWords[0]
				gavin_brimhall_chris_langan_task1_hw7.CheckDoors(lineWords)	
			else:
				print("something is weird")
			i += 1

if __name__== '__main__':
	main()
	exit(0)