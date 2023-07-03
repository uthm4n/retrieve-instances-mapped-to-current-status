import json 
import requests

url = "https://<YOUR-MORPHEUS-URL>/api/instances?max=25&offset=0&showDeleted=false&details=false"   # By default, this retrieves the first 25 instances. You can configure this by changing 'max=' to a valid integer within the limits defined in the API docs

headers = {
    "accept": "application/json",
    "authorization": "Bearer <YOUR-API-TOKEN>"
}
response = requests.get(url, headers=headers, verify=False)
data = response.json()
for h in data['instances']:
    print(f"Instance: {h['hostName']}, Status: {h['status'].upper()}")
