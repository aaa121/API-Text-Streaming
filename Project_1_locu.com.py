# This project signed up for api key via dev.locu.com
#tripplehay777;akinakin1988

api_key='f3972d994a3e733bf6380f4d0ae0c23dbbd7b112'
query_url='https://api.locu.com/v1_0/venue/search/?category=restaurant&api_key=f3972d994a3e733bf6380f4d0ae0c23dbbd7b112'
#from Web_Scraping_LXML_and_Requests_Modules import web_statistics_function as ws
#ws.web_stat(query_url)
'''
# The stat indicates that it is a JSON web:
Status:200
Header:text/html;charset=UTF-8
Encode:UTF-8

Status:200
Header:application/json
Encode:None
'''
#OPEN the website
import requests
r=requests.get(query_url)
#print(r.text) #This prints the json format of the data. It has two objects;
# 1. is object with two names and values pairs; 2. is an array with multiple
# objects, each for individual restaurant.
#print(r.json()) # This prints the second object with list of variables of interest
data=r.json()
for item in data['objects']:
    #print(item)
    print(item["name"])
    print(item["phone"])

def locu_search(category,location,search):
    '''
    This search through the directory in locu.com for bars, restaurants or spa centres around a particular location
    for a given category i.e. query.

    https://api.locu.com/v1_0/venue/search/?locality=Newport%20beach&category=spa&api_key=f3972d994a3e733bf6380f4d0ae0c23dbbd7b112
    https://api.locu.com/v1_0/venue/search/?locality=Newport%20beach&category=restaurant&api_key=f3972d994a3e733bf6380f4d0ae0c23dbbd7b112
    '''
    import requests
    api_key='api_key=f3972d994a3e733bf6380f4d0ae0c23dbbd7b112'
    url='https://api.locu.com/v1_0/venue/search/?'
    locality=location.replace(' ','%20')
    final_url=url+'locality='+locality+'&category='+category+'&'+api_key
    r=requests.get(final_url)
    data = r.json()
    for item in data['objects']:
        print(item[search])
        