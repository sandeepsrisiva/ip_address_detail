from flask import Flask, render_template, request
import ipapi

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/", methods=['GET', 'POST'])
def streambyte():
    # your file processing code is here...
    data=[]
    ipdata=[]
  
    f = request.form['ipaddress']
    if f == '':
        dataip=ipapi.location(ip='')
    else:
        dataip=ipapi.location(ip=f)

    if 'error' in dataip.keys():
        if(dataip['error']==True):
            data=[str(dataip['reason'])]
            ipdata.append(data)
    else:
        data=["IP Address", str(dataip['ip'])]
        ipdata.append(data)
        data=["Version",str(dataip['version'])]
        ipdata.append(data)
        data=["City",str(dataip['city'])]
        ipdata.append(data)
        data=["Region",str(dataip['region'])]
        ipdata.append(data)
        
        data=["Country",str(dataip['country_code'])+" | "+str(dataip['country_name'])]
        ipdata.append(data)
        data=["Postal",str(dataip['postal'])]
        ipdata.append(data)
        data=["European Union",str(dataip['in_eu'])]
        ipdata.append(data)
        data=["Latitude",str(dataip['latitude'])]
        ipdata.append(data)
        data=["Longitude",str(dataip['longitude'])]
        ipdata.append(data)
        data=["Time Zone ",str(dataip['timezone'])+'('+str(dataip['utc_offset']+')')]
        ipdata.append(data)
        data=["Calling Code",str(dataip['country_calling_code'])]
        ipdata.append(data)
        data=["Langagues",str(dataip['languages'])]
        ipdata.append(data)
        data=["ASN",str(dataip['asn'])]
        ipdata.append(data)
        data=["ISP",str(dataip['org'])]
        ipdata.append(data)
    # your_script_result = 'This variable holds the final data output'
    # your file processing code is here...
   

    return render_template('index.html', ipdata = ipdata)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)