import json
import requests

# disable https warning from python
# source: https://stackoverflow.com/questions/27981545/suppress-insecurerequestwarning-unverified-https-request-is-being-made-in-pytho

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# open json file containing the appKey
json_file = open("config.json")
config = json.load(json_file)
json_file.close()

url = 'https://pp-2101111403aw.portal.ptc.io/Thingworx/Things/JA_Generic_Analytics_Thing/Services/RunPrediction'
headers = {'Content-Type': 'application/json', 'accept': 'application/json',
           "appKey": config["appKey"]} 


def call_thingworx_service(data):
    payload = {"goal": "goal",
               "modelUri": "7b251012-9e69-436a-863f-215497c4a031",
               "scoringData": {
                   "dataShape": {
                       "fieldDefinitions": {
                           "feature1": {
                               "name": "feature1",
                               "aspects": {
                                   "isPrimaryKey": "false"
                               },
                               "description": "",
                               "baseType": "NUMBER",
                           }
                       }
                   },
                   "rows": data["rows"]
               }
               }
    thingworx_response = requests.post(url, headers=headers, json=payload, verify=False)
    return thingworx_response


# Define a dictionary containing scoring data
feature1Value = 2
data = {'rows': [{'feature1': feature1Value}]}

response = call_thingworx_service(data)
if response.status_code == 200:
    result = json.loads(response.text)
    goal = result["rows"][0]["goal"]  # save to file?
    print("The predicted value for the goal is: " + goal)
else:
    print("Request failed with error code: " + str(response))
    print("Thingworx error code: " + str(response.text))

