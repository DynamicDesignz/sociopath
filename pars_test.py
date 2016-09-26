import sys
import os
def parseText(filename):
	if not os.path.isfile(filename):
		print("File not found.");
		exit(0)
	if not os.access(filename, os.R_OK):
		print("Access denied.");
		exit(0)
	f=open(filename,'r')
	for line in f.readlines():
		print(line)
def main():
	if len(sys.argv)==2:
		parseText(sys.argv[1])
if __name__ == "__main__":
	main()
