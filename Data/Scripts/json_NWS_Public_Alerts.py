import urllib

#import time
#timestr = time.strftime("%Y%m%d_%H%M%S")
f = "NWS_Public_Alerts.json"# + timestr + ".json"
r = urllib.urlopen(r"http://tmservices1.esri.com/arcgis/rest/services/LiveFeeds/Weather_Warnings_Watches_Advisories_Statements/MapServer/0/query?f=json&where=1%3D1&outFields=OBJECTID,CATEGORY,EVENT,URGENCY,SEVERITY,CERTAINTY,UTC_START,UTC_END,INC_DESC,INC_LINK,STATE_ZONE&outSR=4326&maxAllowableOffset=")
values = r.read()

if values.find("Unable to complete Query operation") <> -1:
	print "Unable to complete Query operation."
else:
	print "OK"
	jsonFile = open(r"C:\GeoEvent\Input\NOAA_Warnings\\" + f, "w")
	jsonFile.write(values)
	jsonFile.close()
