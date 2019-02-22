import xml.etree.ElementTree as ET
import requests
import csv

#parse xml file from tfl site for santander bikes

req = requests.get(".....", stream=True)
req.raw.decode_content = True  # ensure transfer encoding is honoured
data = ET.parse(req.raw)
root = data.getroot()

bike_data = open('tflbikes.csv', 'w' ,newline='')
bikes_head = ['id','name','lat','long','installed','locked','installDate','removalDate','temporary','nbBikes','nbEmptyDocks','nbDocks']

csvwriter = csv.writer(bike_data)
csvwriter.writerow(bikes_head)


for station in root.findall('station'):

    # bike = []

    id = station.find('id').text
    name = station.find('name').text
    lat = station.find('lat').text
    long = station.find('long').text
    installed = station.find('installed').text
    locked = station.find('locked').text
    installDate = station.find('installDate').text
    removalDate = station.find('removalDate').text
    temporary = station.find('temporary').text
    nbBikes = station.find('nbBikes').text
    nbEmptyDocks = station.find('nbEmptyDocks').text
    nbDocks = station.find('nbDocks').text

    bike = [id,name,lat,long,installed,locked,installDate,removalDate,temporary,nbBikes,nbEmptyDocks,nbDocks]

    csvwriter.writerow(bike)

    print(id,name,lat,long,installed,locked,installDate,removalDate,temporary,nbBikes,nbEmptyDocks,nbDocks)



