#!/usr/bin/python
import os, sys, string, telnetlib, time
from optparse import OptionParser

############
# LOGIN
############
def login():
	#print "->Send CR"
	tn.write("\r")
	tn.read_until("IBM CORP",5)
	#print "<-Got screen login"
	tn.write(options.username + "\t")
	tn.write(options.password + "\r")
	#print "->Login sent"
	try:
		VAR = tn.read_until("===>",5)

	except:
		print "UNKNOWN - Connection error"
		sys.exit(3)

	if bool("===>" in VAR):
		logout()
	else:
		print "CRITICAL - Login failed"
		sys.exit(2)
		#print "++Closing connection"
		tn.close()

############
# LOGOUT
############
def logout():	
	print "OK - Login successful"
	#print "->Logging out"
	tn.write("signoff *nolist")
	#print "++Logged out"
	tn.close()
	sys.exit(0)

##############
# MAIN
# ###########

parser = OptionParser(version="%prog 0.1")

parser.add_option("-u", "--username", dest="username", 
   default='NAGIOS', help="The AS400 username [default: %default] ")

parser.add_option("-p", "--password", dest="password", 
   default='NAGIOS', help="The password [default: %default] ")

parser.add_option("-H", "--hostname", dest="hostname", 
   default='as400', help="The AS400 hostname/address [default: %default]")

(options, args) = parser.parse_args()

#print options.username +  options.password + options.hostname

#print "++Opening connection ..."
# Crea l'oggetto connessione telnet
tn = telnetlib.Telnet()
#tn.set_debuglevel(1)
try:
	# apre la connessione
	tn.open(options.hostname)
except:
	# ritorna uknown se fallisce la connessione
	print "UNKNOWN - Connection error"
	sys.exit(3)

#print "++Connection opened"

login()

