import optparse
from socket import *
openPorts = ""
class bcolors:
	success = '\033[92m'
	failure = '\033[91m'
	warning = '\033[93m'
	bold = '\033[1m'
	endc = '\033[0m'
def connScan(tgtHost, tgtPort, verbose):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		print('[+] Port %d is open.'% tgtPort)
		try:
			connSkt.send(' ')
			results = connSkt.recv(100)
			print('[*] '+str(results))
		except:
			print('[-] No banner received.')
		connSkt.close()
	except:
		if(verbose):
			print('[-] Port %d is closed.'% tgtPort);
def portScan(tgtHost, tgtPorts, verbose):
	try:
		tgtIP=gethostbyname(tgtHost)
	except:
		print('[-] Cannot resolve hostname.')
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print('[+] Scanning '+tgtName[0]+'.')
	except:
		print('[+] Scanning '+tgtIP+'.')
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		if(verbose):
			print('[+] Scanning port '+tgtPort+'.')
		connScan(tgtHost, int(tgtPort), verbose)
def main():
	parser = optparse.OptionParser('usage %prog -H'+'<target host> -p <target port>')
	parser.add_option('-H',dest='tgtHost',type="string", help="specify target host")
	parser.add_option('-p', dest="tgtPort", type="string", help='specify target port')
	parser.add_option('-r', dest="rPort", type="string", help='specify range min,max')
	parser.add_option('-s', action="store_false", dest="verbose", default=True, help='specify silent mode')
	(options,args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if(tgtHost == None):
		print('[-] Specify a host')
		exit(0)
	if(tgtPorts[0]=="None"):
		print("[*] Target port is not implicit, switching to range mode.")
		rangePorts = str(options.rPort).split(',')
		if(rangePorts[0] == None):
			print('[-] Specify ports or a range of ports')
			exit(0)
		tgtedPorts=""+rangePorts[0]
		print("[*] Ports list begins at "+rangePorts[0]+" and ends at "+rangePorts[1]+".")
		for x in range(int(rangePorts[0])+1, int(rangePorts[1])+1):
			tgtedPorts=tgtedPorts+","+str(x)
		tgtPorts = str(tgtedPorts).split(',')
	print('[+] Retrieved list of ports to scan.')
	portScan(tgtHost, tgtPorts, options.verbose)
	print("[+] Finished scan.")
if __name__=='__main__':
	main()
