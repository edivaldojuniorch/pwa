import requests
import json
from dotenv import load_dotenv
import os

# Credentials
load_dotenv('.env')

# Use the sensitive data from the security file 
pi_vision_hostname = os.getenv('PI_VISION_HOSTNAME')
user = os.getenv('USER')
password = os.getenv('PASSWORD')

# cases to be runned using a simple approunch
case  = 1

if case == 0:
    ## Request process
    # get information from asset servers connected to PI Web API
    route =  '/piwebapi/system'

    # build the route to match the desided endpoint
    PWA_url = pi_vision_hostname + route

    # build a request to PI Web API, using the required authentication method. 
    # OBS.: SSL is desiable at the PI Vision server, so the verification for certificate is disable
    response = requests.get(PWA_url,auth=(user, password), verify=False)

    ## set a json format for the response
    rq_text = json.loads(response.text)

    ## Output Process
    print('--- Processando dados ----')
    print(rq_text = json.loads(response.text))

elif case == 1 :
    ## Request process
    # get information from asset servers connected to PI Web API
    route = '/piwebapi/assetservers'

    # build the route to match the desided endpoint
    PWA_url = pi_vision_hostname + route

    # build a request to PI Web API, using the required authentication method. 
    # OBS.: SSL is desiable at the PI Vision server, so the verification for certificate is disable
    response = requests.get(PWA_url,auth=(user, password), verify=False)

    ## set a json format for the response
    rq_text = json.loads(response.text)

    ## Output Process
    print('--- Processando dados ----')

    for i in rq_text['Items']:
        print(i['Name'])
        

report = {
    'content': response.headers['content-type'],
    'encoding': response.encoding,
    'text' : response.text,
    'json': response.json()
}

