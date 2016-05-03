# For Name and Phone Number

def locu_search(category,location):
    '''
    #This search through the directory in locu.com for bars, restaurants or spa centres around a particular location
    #for a given category i.e. query.

    #https://api.locu.com/v1_0/venue/search/?locality=Newport%20beach&category=spa&api_key=f3972d994a3e733bf6380f4d0ae0c23dbbd7b112
    #https://api.locu.com/v1_0/venue/search/?locality=Newport%20beach&category=restaurant&api_key=f3972d994a3e733bf6380f4d0ae0c23dbbd7b112
    '''
    import requests
    api_key='api_key=f3972d994a3e733bf6380f4d0ae0c23dbbd7b112'
    url='https://api.locu.com/v1_0/venue/search/?'
    locality=location.replace(' ','%20')
    final_url=url+'locality='+locality+'&category='+category+'&'+api_key
    r=requests.get(final_url)
    data = r.json()
    for item in data['objects']:
        print(item['name'],item['phone'],sep='\t')

locu_search('spa','new york')