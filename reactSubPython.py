import requests
import json



#https://my.locationiq.com/dashboard/?firstLogin=1

url = "https://us1.locationiq.com/v1/search.php"
#
# data = {
#     'key': 'API key',
#     'q': 'New Delhi',
#     'format': 'json'
# }
#
# response = requests.get(url, params=data)
#
# print(response.text)



##writing to json
async def main():
    with open('places.json',encoding='utf-8') as f:
        Placedata = json.load(f)

    NewList = Placedata["Places"]
    print(NewList)

    f = open('places.txt','r')
    f1 = f.readlines()


    for x in enumerate(f1):
        print(x)
        tempData = {}
        tempData['key'] = 'Your Api Key'
        tempData['q'] = x[1].strip('\n').replace('\"','')
        tempData['format'] = 'json'
        NewList.append(tempData)

    String_Data = "{" + "'Places':" + str(NewList) + "}"
    #print(eval(String_Data))




    Dict =  eval(String_Data)

    with open('places.json','w',encoding='utf-8') as f2:
         json.dump(Dict,f2,indent=2)


    with open('places.json',encoding='utf-8') as f:
        Placedata = json.load(f)

    fpi =  open('placesInfo.txt','a+')


    for place in Placedata["Places"]:
        c = place

        response =yield requests.get(url, params=c)
        NewPlacesData = response.json()

        print(json.dumps(NewPlacesData,indent = 2))

        latlon = []
        templatlon = {}
        templatlon['lon'] = NewPlacesData[0]['lon']
        templatlon['lat'] = NewPlacesData[0]['lat']

        latlon.append(templatlon)
        fpi.write(str(latlon)+"\n")



    fpi.close()

if __name__ == '__msin__':
    main()#print(placeData)