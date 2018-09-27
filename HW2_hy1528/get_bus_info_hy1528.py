
######
from __future__ import print_function
import sys
import pylab as pl
import os
import json
######

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
#####
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python show_bus_locations_hy1528.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()
#####

fout = open(sys.argv[3], "w")

####get data from the input

url1 ="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&version=2&LineRef=%s&VehicleMonitoringDetailLevel=calls&MaximumNumberOfCallsOnwards=1"%(sys.argv[1],sys.argv[2])
response = urllib.urlopen(url1)
data = response.read().decode("utf-8")
data = json.loads(data)
bus=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#####list the number of buses at activity and their location

fout.write("Bus Line :%s\n"%sys.argv[2])
fout.write("Number of Active buses : %s\n"%len(bus))
fout.write('Latitude,Longitude,Stop_name,Stop_status\n')
for it in bus:
    location=it['MonitoredVehicleJourney']['VehicleLocation']
    try:
         stop_name=it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
         stop_status=it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['ArrivalProximityText']
    except:
         stop_name="NA"
         stop_status="NA"
    fout.write("%s,%s,%s,%s\n"%(location['Latitude'],location['Longitude'],stop_name,stop_status))
fout.close()
