import loader
from jinja2 import Template

ITEM_SLOTS=["shoulder","neck","trinket1","trinket2","finger2","waist","finger1","head","back","feet","chest","wrist","hands","legs"]


ITEM_FIRST_COLUMN=["head","neck","shoulder","back","chest","wrist"]
ITEM_SECOND_COLUMN=["hands","waist","legs","feet","finger1","finger2","trinket1","trinket2"]


def genItem(itemType):
	return "<a class=\"box\" style=\"background-image: url(//wow.zamimg.com/images/wow/icons/large/{{items."+itemType+".icon}}.jpg);\"  href=\"http://www.wowdb.com/items/{{ items."+itemType+".id}}?bonusIDs={{items."+itemType+".bonusLists}}"+"\"></a><br>\n"


def genItemBox():
	ITEMS_BOX=""
	for itemType in ITEM_SLOTS:
		ITEMS_BOX+=genItem(itemType)
	return ITEMS_BOX


def ErrorTemplate():
	return "Error: No such character"

def CharacterTemplate(charname,servername):
	CL=loader.CharLoader(charname,servername)
	CL.gatherItems()
	if(CL.DATA):
		STYLE="<head><link rel=\"stylesheet\" type=\"text/css\" href=\"character.css\"></head>"
		HEADER="<script src=\"//ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js\"></script><script type=\"text/javascript\" src=\"http://static-azeroth.cursecdn.com/current/js/syndication/tt.js\"></script>"
		NAME_BOX="\n{{ charname }} from {{ servername }} <br>\n"
		FOOTER="Last loaded on {{ last_load }}<br>"
		print("Last data from "+CL.DATA.get("last_load"))
		return(Template(STYLE+HEADER+NAME_BOX+genItemBox()+FOOTER).render({"charname" : CL.CHARNAME,"servername" : CL.WORLD, "items":CL.DATA.get("items"),"last_load":CL.DATA.get("last_load")}))
	else:
		return(Template(ErrorTemplate()).render())