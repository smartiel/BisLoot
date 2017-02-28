#https://eu.api.battle.net/wow/character/Hyjal/Shlick?fields=items&locale=en_GB&apikey=bwbkcvgtndshe3vt342k45v49vbrkruu

import httplib,urllib,json
from jinja2 import Environment, PackageLoader, Template

ITEM_SLOTS=["shoulder","offHand","neck","trinket1","trinket2","finger2","waist","finger1","head","mainHand","back","feet","chest","wrist","hands","legs"]



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
		self.apiConnection.request("GET", self.CHAR_API_SERVICE+self.WORLD+"/"+self.CHARNAME+"?fields=items&locale=en_GB&apikey="+self.API_KEY, '', {})
		req=self.apiConnection.getresponse()
		data=req.read()
		self.DATA=json.loads(data)



def genItemBox(CL):
	ITEMS_BOX=""
	for itemType in ITEM_SLOTS:
		ITEMS_BOX+="<a href=\"http://www.wowdb.com/items/{{ items."+itemType+".id}}?bonusIDs={{items."+itemType+".bonusLists}}"+"\">"+itemType+"</a><br>"
	return ITEMS_BOX

CL=CharLoader("Shlick","Hyjal")
CL.gatherItems()


HEADER="<script src=\"//ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js\"></script><script type=\"text/javascript\" src=\"http://static-azeroth.cursecdn.com/current/js/syndication/tt.js\"></script>"

NAME_BOX="{{ charname }} from {{ servername }} <br>"



Template(HEADER+NAME_BOX+genItemBox(CL)).stream({"charname" : CL.CHARNAME,"servername" : CL.WORLD, "items":CL.DATA.get("items")}).dump('test.html')



#print(template.render(charname=CL.CHARNAME,servername=CL.WORLD,shoulderName=CL.DATA.get("items").get("shoulder").get("name"),shoulderId=CL.DATA.get("items").get("shoulder").get("id")))



#print(CL.DATA.get("items").get("shoulder"))