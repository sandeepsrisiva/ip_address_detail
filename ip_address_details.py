import ipapi
import json


data=ipapi.location()
# dataipai=json.loads(data)
dataipai=json.dumps(data,indent=1)
print(dataipai)