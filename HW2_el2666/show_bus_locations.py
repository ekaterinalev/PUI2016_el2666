import pylab as pl
import json
import urllib.request as ulr
import sys

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key= + sys.orgv[1] + sys.orgv[2]"
response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

Bus_Line = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']
Active_Buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleRef']
Bus_0_lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
Bus_0_long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'

print "Bus Line:", Bus_Line
print "Number of Active Buses:", Active_Buses
print "Bus 0 is at", Bus_0_lat, "and at", Bus_0_long