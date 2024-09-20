# Make a file name as 'main.py'
import phonenumbers
import opencage
from myphone import number
from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, 'en')
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, 'en'))

from opencage.geocoder import OpenCageGeocode
key = '904077b16c8543a981ba821d103b92d7' //In this key we have to make a account on opencage and then there is a geo coding api code add this key here
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)



# Two software we have to install name as
# 1- pip install phonenumbers
# 2- pip install opencage
# This two software we have to install in terminal in the code editor

#make a anothor file name as myphone.py in there the code is 
number = 'the number'
