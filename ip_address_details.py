import ipapi
import json

dataip=input("Enter the IP address:")
data=ipapi.location(ip=dataip)
# dataipai=json.loads(data)
dataipai=json.dumps(data,indent=1)
print(dataipai)