#!/usr/bin/env python3
import sys

def CheckDoors(args):
	"""
	Takes care of all the logic
	"""
	LD = 0 #Left dashboard switch
	RD = 0 #Right dashboard switch
	CL = 0 #Child Lock
	ML = 0 #Master unlock switch
	LI = 0 #Left inside handle
	LO = 0 #Left outside handle
	RI = 0 #Right inside handle
	RO = 0 #Right outside handle
	GS = 'P' #Gear shift
	print 'Arg list: ', str(sys.argv)
