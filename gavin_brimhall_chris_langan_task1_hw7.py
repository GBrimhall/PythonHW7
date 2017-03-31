#!/usr/bin/env python3
import sys

def CheckDoors(junk, LDa, RDa, CLa, MLa, LIa, LOa, RIa, ROa, GSa):
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
	GS = 'Z' #Gear shift

	LD = LDa
	RD = RDa
	CL = CLa
	ML = MLa
	LI = LIa
	LO = LOa
	RI = RIa
	RO = ROa
	GS = GSa

	if GS == 'P':
		#Car is in park
		if ML == 1:
			#Master lock is active
			if CL == 1:
				#Child lock is active, ignore inside door handles
				#Check left door first
				if LI == 1:
					#left inside handle pulled
					print ("Left door does not open")
				elif LD == 1:
					#left dashboard switch pressed
					print ("Left door opens")
				elif LO == 1:
					#left outside handle pulled
					print ("Left door opens")
				else:
					#Nothing is trying to open the left door
					print ("Left door does not open")

				#Check right door
				if RI == 1:
					#right inside door handle pulled
					print ("Right door does not open")
				elif RD == 1:
					#Right dashboard switch pressed
					print ("Right door opens")
				elif RO == 1:
					#Right outside handle pulled
					print ("Right door opens")
				else:
					#Nothing is trying to open the right door
					print ("Right door does not open")
			else:
				#Child lock is not active
				#Check left door first
				if LI == 1:
					#left inside handle pulled
					print ("Left door opens")
				elif LD == 1:
					#left dashboard switch pressed
					print ("Left door opens")
				elif LO == 1:
					#left outside handle pulled
					print ("Left door opens")
				else:
					#Nothing is trying to open the left door
					print ("Left door does not open")

				#Check right door
				if RI == 1:
					#right inside door handle pulled
					print ("Right door does opens")
				elif RD == 1:
					#Right dashboard switch pressed
					print ("Right door opens")
				elif RO == 1:
					#Right outside handle pulled
					print ("Right door opens")
				else:
					#Nothing is trying to open the right door
					print ("Right door does not open")

		else:
			#Master lock is not active
			print("Doors do not open")
	else:
		#Car is not in park
		print ("Doors do not open")

if __name__ == '__main__':
	CheckDoors(sys.argv[1:])
