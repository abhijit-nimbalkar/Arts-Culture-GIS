import requests
import folium
import json
import ckanapi
import pprint as PP
import My_Keys as mk
from IPython.display import HTML, display

pp=PP.PrettyPrinter(indent=2)
pprint=pp.pprint
API_for_census_root_url='https://api.census.gov/data/2016/acs/acs5'

#----------Census Data for Allegheny County---------------------------#

base_param_for_census= {
    'get':'NAME,B01001_001E',
    'for':'county%20subdivision',
    'in':'state:42%20county:003'
    }

modified_base_param='&'.join('%s=%s' % (k,v) for k,v in base_param_for_census.items())

r_census=requests.get(API_for_census_root_url,params=modified_base_param)

population_data=r_census.json()
Tot_est_pop=0
for i in range(len(population_data)):
    if(i!=0):
        Tot_est_pop=Tot_est_pop+int(population_data[i][1])
print("Census Data for Allegheny County\n")
for i in range(10):
    print(population_data[i])    
print("Total Estimated Population is: ", Tot_est_pop)

#-----------Housing data for Allegheny County--------------------#

base_param_for_housing= {
    'get':'NAME,B25001_001E',
    'for':'county%20subdivision',
    'in':'state:42%20county:003'
    }

modified_base_param='&'.join('%s=%s' % (k,v) for k,v in base_param_for_housing.items())
r_housing=requests.get(API_for_census_root_url,params=modified_base_param)
housing_data=r_housing.json()

print("\nHousing Data for Allegheny County\n")
for i in range(10):
    print(housing_data[i])
    
Tot_est_house=0
for i in range(len(housing_data)):
    if(i!=0):
        Tot_est_house=Tot_est_house+int(housing_data[i][1])
print("Total Estimated Population is: ", Tot_est_house)

#--------------Using WPRDC to pull the data----------------------#
site="https://data.wprdc.org"
playing_field_id='6af89346-b971-41d5-af09-49cfdb4dfe23'
has_lights='False'

number_of_fields=mk.query_resource(site,'SELECT count(*) FROM \"{}\"'.format(playing_field_id))
number_of_fields_not_having_light=mk.query_resource(site,"select name,park,latitude,longitude from \"{}\" where \"has_lights\" = '{}'".format(playing_field_id,has_lights))

print('There are total number of ',len(number_of_fields_not_having_light),' fields are not having lights out of ',number_of_fields[0]['count'])

print(number_of_fields_not_having_light[0])

myMap = folium.Map(location=[number_of_fields_not_having_light[0]['latitude'],number_of_fields_not_having_light[0]['longitude']], zoom_start=16)

