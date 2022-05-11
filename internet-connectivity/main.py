import urllib.request as urec

def checkthe_connection():
	host = "http://www.google.com"
	try:
		urec.urlopen(host)
		return True
	except :
		return False

if checkthe_connection():
	print("You're connected to a network")
else:
	print("You have no connection")
  