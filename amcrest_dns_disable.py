import requests
from requests.auth import HTTPDigestAuth

#IPC Cams (Web interface)
ipc_cams = ['10.0.0.126', '10.0.0.184', '10.0.0.225', '10.0.0.205', '10.0.0.186']

#DVR Cams (App only)
dvr_cams = ['10.0.0.168']

#Camera Username / Pass - set same for all cams.
username = 'admin'
password = 'YourPassword'

#Disable the Amcrest Config to stop DNS requests on IPC cams.
for cam in ipc_cams:
    try:
        print("Setting ipc cam: ", cam)
        
        url = "http://"+cam+"/cgi-bin/configManager.cgi?action=setConfig&Amcrest.ConfigAddress=0.0.0.0"
        response = requests.get(url, auth=HTTPDigestAuth(username, password))
        print(response.text)
    except Exception as e:
        print(e)
        pass

#Settings to disable for insane number of DNS requests on DVR cams
for cam in dvr_cams:
    settings = ['T2UServer.Enable=false',
                'VSP_PaaS.Enable=false',
                'VSP_PaaS.CustomEnable=false',
                'VSP_PaaS.RsServerIP=0.0.0.0',
                'VideoWidget[0].TimeTitle.EncodeBlend=false'] #Disable TimeStamps

    try:
        print("Setting dvr cam: ", cam)

        for setting in settings:
            url = "http://"+cam+"/cgi-bin/configManager.cgi?action=setConfig&" + setting
            response = requests.get(url,auth=HTTPDigestAuth(username, password))
            print(setting, ' ', response.text)

    except Exception as e:
        print(e)
        pass