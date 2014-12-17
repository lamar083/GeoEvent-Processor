
# Import arcpy module
import arcpy


# Local variables:
json = "C:\\GeoEvent\\Input\\NOAA_Warnings\\NWS_Public_Alerts.json"
SDE_1 = " " # update with path to local ArcServer Feature Service
SHP_1 = "C:\\GeoEvent\\Input\\NOAA_Warnings\\NWS_Public_Alerts.shp"
SHP_2 = "C:\\GeoEvent\\Input\\NOAA_Warnings\\NWS_Public_Alerts.shp"
SDE_2 = " " # update with path to local ArcServer Feature Service

# Process: Delete
arcpy.Delete_management(SHP_1, "ShapeFile")

# Process: JSON To Features
arcpy.JSONToFeatures_conversion(json, SHP_2)

# Process: Delete Features
arcpy.DeleteFeatures_management(SDE_1)

# Process: Append
arcpy.Append_management("C:\\GeoEvent\\Input\\NOAA_Warnings\\NWS_Public_Alerts.shp", SDE_2, "TEST", "", "")

