import json
import ast

f =open('placesInfo.txt','r+')
k = open('places.txt')

stringAllPlacesJson = ''
newPlacesArry = []
for k1 in k.readlines():
    newPlacesArry.append(k1)

temp = {}

for f1 in enumerate(f.readlines()):
    details = {}
    details["name"] = newPlacesArry[f1[0]].strip('\n').replace('\"','')
    details["lon"] = int(ast.literal_eval(f1[1])[0]["lon"])
    details["lat"] = int(ast.literal_eval(f1[1])[0]["lat"])

    # details["lat"] = json.loads(f1[1])['lat']

    temp["Places" + str(f1[0])] = details

with open("AllPlaces.json",'w+') as f_key:
    json.dump(temp,f_key,indent=2)
