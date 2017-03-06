import json,os


DATA_PATH="Data/"


def dump(charName,serverName,jsondata):
	print("Trying to dump in "+DATA_PATH+serverName)
	if not os.path.exists(DATA_PATH+serverName):
		print("Creating directory "+DATA_PATH+serverName)
		os.makedirs(DATA_PATH+serverName)
	else:
		print(DATA_PATH+serverName+" already exists")
	dumpfile=open(DATA_PATH+serverName +"/"+charName+".json",'w')
	dumpfile.write(json.dumps(jsondata))
	dumpfile.flush()
	dumpfile.close()

def tryLoad(charName,serverName):
	try:
		charfile=open(DATA_PATH+serverName +"/"+charName+".json",'r')
		charfile.close()
		return True
	except IOError:
	    print "No data for this character!"
	    return False

def load(charName,serverName):
	charfile=open(DATA_PATH+serverName +"/"+charName+".json",'r')
	data=json.loads(charfile.read())
	charfile.close()
	return data
	