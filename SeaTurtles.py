import pandas as pd
import pprint
from config import gmap_apikey

from gmplot import *
import gmplot 

#kemp's ridley turtle
ridley = pd.read_csv("Ridley_1csv.csv")

latitude = ridley['decimalLatitude']
longitude = ridley['decimalLongitude']

gmap = gmplot.GoogleMapPlotter( -10.695, 135.908, 6 )
gmap.scatter(latitude, longitude, 'black',size = 500, marker = False )
gmap.plot(latitude, longitude, '#0BD029', edge_width = 1.0)
gmap.apikey = gmap_apikey
gmap.draw ( "Users>heidiklise>Desktop>python>ridley.html")


#hawksbill turtle
hawksbill = pd.read_csv("hawksbillcsv.csv")

hawksbill_lat = hawksbill['decimalLatitude']
hawksbill_long = hawksbill['decimalLongitude']

gmap = gmplot.GoogleMapPlotter( -10.695, 135.908, 6 )
gmap.scatter(hawksbill_lat, hawksbill_long, 'black',size = 500, marker = False )
gmap.plot(hawksbill_lat, hawksbill_long, 'E645F3', edge_width = 1.0)
gmap.apikey = gmap_apikey
gmap.draw ( "Users>heidiklise>Desktop>python>hawksbill.html")
