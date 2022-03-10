import requests
import json 
from datetime import datetime
now = datetime.now()
now = str(now)
now = list(now)
now[10] = "T"; now[19] = "Z"
now = now[0:20]
month = now[5] + now[6]
year = now[0]+now[1]+now[2]+now[3]
INTmonth = int(month)
if INTmonth == 1:
    now[5] = "1"
    now[6] = "2"
    now[3] = int(now[3]) - 1
    now[3] = str(now[3])
else:
    if INTmonth >10:
        INTmonth -= 1
        now[5] = "1"
        now[6] = str(INTmonth - 10)
    else:
        now[5] = "0"
        now[6] = str(INTmonth - 1)
now = "".join(now)
print(now)




URL = "https://api.battlemetrics.com/servers"

URL2 = "https://api.battlemetrics.com/players"

searchTerm = "Rustopia EU Main"

playerSearchTerm = "[SB] ostritch"

PARAMS = {
    "filter[search]":searchTerm,
    "filter[game]":"rust",
    }

playerPARAMS = {
    "filter[search]":playerSearchTerm,
    "filter[after]":now
}

x = requests.get(url = URL, params = PARAMS)
y = requests.get(url = URL2, params = playerPARAMS)

data2 = y.json()

data = x.json()

parsed_data2 = json.dumps(data2,indent=4,sort_keys=True)
parsed_data = json.dumps(data,indent=4,sort_keys=True)

#print(parsed_data2)

parsed_data_dict = json.loads(parsed_data)
parsed_data_dict2 = json.loads(parsed_data2)

#print(len(parsed_data_dict["data"]))
if False:
    for i in range(len(parsed_data_dict["data"])):
        print(parsed_data_dict["data"][i]["attributes"]["ip"])
        print(parsed_data_dict["data"][i]["attributes"]["name"])
        print(parsed_data_dict["data"][i]["attributes"]["players"])
        print(parsed_data_dict["data"][i]["attributes"]["status"])
        print(parsed_data_dict["data"][i]["id"])



with open("C:\\Users\\wista002\\Desktop\\Mitt-repo\\python-development\\rust-automated\\alert-bot\\testing\\request.json","w") as outfile:
#with open("C:\\Users\\Gaming_Dator_VII\\Desktop\\Mitt-repo\\python-development\\rust-automated\\alert-bot\\testing\\request.json","w") as outfile:

    outfile.write(parsed_data2)


    

