
####
from __future__ import print_function
import sys
import pylab as pl
import os
import json
####
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
####

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_hy1528.py <MTA_KEY> <BUS_LINE>")
    sys.exit()


####get data from the input

url1 ="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&version=2&LineRef=%s&VehicleMonitoringDetailLevel=calls&MaximumNumberOfCallsOnwards=1"%(sys.argv[1],sys.argv[2])
response = urllib.urlopen(url1)
data = response.read().decode("utf-8")
data = json.loads(data)
bus=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


####list the number of buses at activity and their location
print("Bus Line :%s"%sys.argv[2])
print("Number of Active buses : %s"%len(bus))
for num,it in enumerate(bus):
    location=it['MonitoredVehicleJourney']['VehicleLocation']
    Latitude=location['Latitude']
    Longitude=location['Longitude']
    print("bus%s is at Latitude: %s and Longitude: %s"%(num,Latitude,Longitude))



