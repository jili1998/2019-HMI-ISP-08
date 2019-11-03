import requests
import json
import base64
import os

def shibie(pcm_file):
    baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    client_id = "Od5uRBIN3K26UG4pWuVY55hu"
    client_secret = "fYsv5tWpaoQqxihukTBOUanqB5tSGRLt" 

    url ="%sgrant_type=%s&client_id=%s&client_secret=%s"%(baidu_server,grant_type,client_id,client_secret)
#print(url)

    res = requests.post(url)
#print(res.text)
    token = json.loads(res.text)["access_token"]
#print(token)

    RATE = "16000"
    FORMAT = "pcm"
    CUID="hsj_yuyin"
    DEV_PID="1536"

    with open(pcm_file,'rb') as f:
        speech_data = f.read()

    size = len(speech_data)
    speech = base64.b64encode(speech_data).decode('utf8')
    headers = { 'Content-Type' : 'application/json'} 
    url = "https://vop.baidu.com/server_api"
    data={

            "format":FORMAT,
            "rate":RATE,
            "dev_pid":DEV_PID,
            "speech":speech,
            "cuid":CUID,
            "len":size,
            "channel":1,
            "token":token,
        }

    req = requests.post(url,json.dumps(data),headers)
    result = json.loads(req.text)
    print (result["err_msg"])
    if result["err_msg"] == "success.": 
        return result["result"][0]
    else:
        return ""
