"""
----------------IPv4/IPv6 address Details Application------------------
Team Name: DevNet_Aditya_Dharmsinh Desai
Team Members: 
1.Sri Siva Sandeep as Scrum Leader and Developer
2. Deepak as Developer and Tester
3. Ravindra as Developer and Tester
4. Surya Ashok as Tester and Developer

"""
# This module install using pip3 install ipapi
import ipapi #import the module for ip location details 


while True:
    dataip=input("Enter the IP address:") # Asking for input 
    # -----check the input for quit------------------
    if dataip=='q' or dataip=='quit': # check the input is q or quit
        break 
    #---------- End--------------

    #get the ip location using this instruction 
    # Here we can instruction ad ipapi.location(ip="x.x.x.x") then we got details about the particular ip
    #x.x.x.x means ip address from the input
    data=ipapi.location(ip=dataip) 

    # check the ip address is correct or not
    # if ip address is wrong or any reserverd ip address  give to input that error message is displayed in terminal
    # if ip address is correct then display the ip address details in terminal
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


