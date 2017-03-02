import json


DATA_PATH="Data/"


def dump(charName,serverName,jsondata):
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
	