import ipapi


while True:
    dataip=input("Enter the IP address:")
    if dataip=='q' or dataip=='quit':
        break
    data=ipapi.location(ip=dataip)
    # print(type(data))
    if 'error' in data.keys():
        if(data['error']==True):
            print("============================================")
            print(data['reason'])
            print("============================================")
    else:
        print ("====================================================================")
        print("IP Address       : "+str(data['ip']))
        print("Version          : "+str(data['version']))
        print("City             : "+str(data['city']))
        print("Region           : "+str(data['region']))
        print("Country          : "+str(data['country_code'])+"|"+str(data['country_name']))
        print("Postal           : "+str(data['postal']))
        print("European Union   : "+str(data['in_eu']))
        print("Latitude         : "+str(data['latitude']))
        print("Longitude        : "+str(data['longitude']))
        print("Time Zone        : "+str(data['timezone'])+'('+str(data['utc_offset']+')'))
        print("Calling Code     : "+str(data['country_calling_code']))
        print("Langagues        : "+str(data['languages']))
        print("ASN              : "+str(data['asn']))
        print("ISP              : "+str(data['org']))
        print ("=========================================================================")

    print("If you want to exit this please enter q/quit")


