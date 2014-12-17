import urllib

#import time
#timestr = time.strftime("%Y%m%d_%H%M%S")
f = "NOAA_SVR_ShortTermWarnings.json"# + timestr + ".json"
r = urllib.urlopen(r"http://tmservices1.esri.com/arcgis/rest/services/LiveFeeds/NOAA_short_term_warnings/MapServer/0/query?f=json&where=1%3D1&outFields=OBJECTID,WFO,ETN,UGC,WFILE,UTC_EXPIRE,UTC_ISSUE&outSR=4326&maxAllowableOffset=")
values = r.read()

if values.find("Unable to complete Query operation") <> -1:
	print "Unable to complete Query operation."
else:
	print "OK"
	jsonFile = open(r"C:\GeoEvent\Input\NOAA_Warnings\\" + f, "w")
	jsonFile.write(values)
	jsonFile.close()
