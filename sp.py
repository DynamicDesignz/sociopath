import os
import sys
import random
def main():
	random.seed()
	y = 16
	for x in range(1,30):
		y = 16
		#for fifteen simulations
		for x in range(1,y): #for all passengers
			prob = random.randint(1,25)
			if(prob<3): #if they don't
					y=y-1	#subtract passengers
		print(y)
if __name__ == "__main__":
	main()
