# retrieve-instances-mapped-to-current-status
Retrieve a list of your instances mapped to their current status (Running, Stopped, etc...)

**How it works:** 

1. Sends an API call to [Get All Instances](https://apidocs.morpheusdata.com/reference/listinstances)
2. Filters through the JSON response and finds .instances.hostName and maps that to .instances.status
3. You now have a list of your instances mapped to their current status ("Running", "Stopped", etc...)

**Example Usage + Output:**

![Pretty-Output.png](https://github.com/uthm4n/retrieve-instances-mapped-to-current-status/blob/main/Pretty-Output.png)


**Note:** similar to [polling the health API](https://github.com/uthm4n/polling-health-api), you can wrap the code in a try-except block + take input for the appliance URL + API key (hardcoding these is never a good practice for security). You can also copy the polling logic from the repo linked ^
