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

url = 'https://pp-2101111403aw.portal.ptc.io/Thingworx/Things/JA_Generic_Analytics_Thing/Services/TrainAnalyticsModel'
headers = {'Content-Type': 'application/json', 'accept': 'application/json',
           "appKey": config["appKey"]}


def call_thingworx_service(data):
    payload = {"goal": "goal",
               "trainingData": {
                   "dataShape": {
                       "fieldDefinitions": {
                           "goal": {
                               "name": "goal",
                               "aspects": {
                                   "isPrimaryKey": "false"
                               },
                               "description": "",
                               "baseType": "INTEGER",
                           },
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

               },
               "metadataInput": {
                   "dataShape": {
                       "fieldDefinitions": {
                           "fieldName": {
                               "name": "fieldName",
                               "description": "",
                               "baseType": "STRING",
                               "ordinal": 0,
                               "aspects": {

                               }
                           },
                           "dataType": {
                               "name": "dataType",
                               "description": "",
                               "baseType": "STRING",
                               "ordinal": 0,
                               "aspects": {

                               }
                           },
                           "opType": {
                               "name": "opType",
                               "description": "",
                               "baseType": "STRING",
                               "ordinal": 0,
                               "aspects": {

                               }
                           },
                           "min": {
                               "name": "min",
                               "description": "",
                               "baseType": "NUMBER",
                               "ordinal": 0,
                               "aspects": {

                               }
                           },
                           "max": {
                               "name": "max",
                               "description": "",
                               "baseType": "NUMBER",
                               "ordinal": 0,
                               "aspects": {

                               }
                           },
                           "values": {
                               "name": "values",
                               "description": "",
                               "baseType": "INFOTABLE",
                               "ordinal": 0,
                               "aspects": {
                                   "dataShape": "GenericStringList"
                               }
                           },
                           "timeSamplingInterval": {
                               "name": "timeSamplingInterval",
                               "description": "",
                               "baseType": "INTEGER",
                               "ordinal": 0,
                               "aspects": {

                               }
                           },
                           "isStatic": {
                               "name": "isStatic",
                               "description": "",
                               "baseType": "BOOLEAN",
                               "ordinal": 0,
                               "aspects": {
                                   "defaultValue": "false"
                               }
                           }
                       }
                   },
                   "rows": [
                       {
                           "fieldName": "goal",
                           "dataType": "INTEGER",
                           "opType": "CONTINUOUS",
                           "isStatic": "false"
                       },
                       {
                           "fieldName": "feature1",
                           "dataType": "DOUBLE",
                           "opType": "CONTINUOUS",
                           "isStatic": "false"
                       }
                   ]
               }
               }
    thingworx_response = requests.post(url, headers=headers, json=payload, verify=False)
    return thingworx_response


# Define a dictionary containing training data
goal = 1
feature1 = 1
data = {'rows': [{'goal': goal, 'feature1': feature1}, {'goal': '2', 'feature1': '2'}]}
#print(data)
value = 100
data['rows'].append({'goal': value, 'feature1': '3'})

response = call_thingworx_service(data)
if response.status_code == 200:
    result = json.loads(response.text)
    modelUri = result["rows"][0]["result"]     #save to file?
    print("The URI for the Analytics model is: " + modelUri)
    print("Please call the check model status service next, to see if the training is finished!")
else:
    print("Request failed with error code: " + str(response))
    print("Thingworx error code: " + str(response.text))
