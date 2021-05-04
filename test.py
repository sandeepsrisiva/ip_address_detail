import ipapi
data=[]
ipdata=[]
dataip=ipapi.location()
if 'error' in dataip.keys():
        if(dataip['error']==True):
            data=['Reason',data['reason']]
            ipdata=data
else:
    data=["IP Address", str(dataip['ip'])]
    ipdata.append(data)
    data=["Version",str(dataip['version'])]
    ipdata.append(data)

print(ipdata)