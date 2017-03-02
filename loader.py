
import datahandler,time
import httplib,urllib,json



class CharLoader:
	WORLD=""
	CHARNAME=""
	API_URL="eu.api.battle.net"
	CHAR_API_SERVICE="/wow/character/"
	API_KEY="bwbkcvgtndshe3vt342k45v49vbrkruu"
	LANG="en_GB"

	DATA={}

	def __init__(self,charname,worldserver):
		self.WORLD=worldserver
		self.CHARNAME=charname
		self.apiConnection=httplib.HTTPSConnection(self.API_URL)

	def gatherItems(self):
		if(datahandler.tryLoad(self.CHARNAME,self.WORLD)):
			self.DATA=datahandler.load(self.CHARNAME,self.WORLD)
		else:
			self.apiConnection.request("GET", self.CHAR_API_SERVICE+self.WORLD+"/"+self.CHARNAME+"?fields=items&locale=en_GB&apikey="+self.API_KEY, '', {})
			req=self.apiConnection.getresponse()
			data=req.read()
			self.DATA=json.loads(data)
			self.DATA["last_load"]=time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
			datahandler.dump(self.CHARNAME,self.WORLD,self.DATA)





#print(template.render(charname=CL.CHARNAME,servername=CL.WORLD,shoulderName=CL.DATA.get("items").get("shoulder").get("name"),shoulderId=CL.DATA.get("items").get("shoulder").get("id")))



#print(CL.DATA.get("items").get("shoulder"))