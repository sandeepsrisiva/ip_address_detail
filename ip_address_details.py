import ipapi
import json

dataip=input("Enter the IP address:")
data=ipapi.location(ip=dataip)
# dataipai=json.loads(data)
# dataipai=json.dumps(data,indent=1)
# print(dataipai)
print("IP Address       : "+str(data['ip']))
print("Version          : "+str(data['version']))
print("City             : "+str(data['city']))
print("Region           : "+str(data['region']))
print("Country          : "+str(data['country_code'])+"|"+str(data['country_name']))