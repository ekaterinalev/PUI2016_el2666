import pylab as pl
import json
import urllib.request as ulr
import sys
import json
import csv

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key= + sys.orgv[1] + sys.orgv[2]"
response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

Stop_Name = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
Stop_Status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']

Latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
Longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

print("Latitude", Latitude, "Longitude", Longitude, "Stop Name", Stop_Name, "Stop Status", Stop_Status)

get_bus_info = "Latitude", Latitude, "Longitude", Longitude, "Stop Name", Stop_Name, "Stop Status", Stop_Status

with open("get_bus_info", "w") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['pk'], item['model']] + item['fields'].values())



