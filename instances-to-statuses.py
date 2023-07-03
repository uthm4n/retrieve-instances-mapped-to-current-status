import json 
import requests
import warnings 

warnings.filterwarnings("ignore")
url = "https://<YOUR-MORPHEUS-URL>/api/instances?max=25&offset=0&showDeleted=false&details=false"   # By default, this retrieves the first 25 instances. You can configure this by changing 'max=' to a valid integer within the limits defined in the API docs

headers = {
    "accept": "application/json",
    "authorization": "Bearer <YOUR-API-TOKEN>"
}
response = requests.get(url, headers=headers, verify=False)
data = response.json()

string = json.dumps(data)                                                                            
total_running_instances = string.count("running")                                                         # add some logic to retrieve 'running' and 'stopped' instances. Note to self: think of a better way to do this
total_stopped_instances = string.count("stopped")
print(f"Total number of instances in a RUNNING state: {total_running_instances}")
print(f"Total number of instances in a STOPPED state: {total_stopped_instances}\n\n")

for h in data['instances']:
    print(f"INSTANCE: {h['hostName']}\n STATUS: {h['status'].upper()}\n")
