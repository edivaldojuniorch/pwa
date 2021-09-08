import requests
import json

class PWApy():
    def __init__(self, pi_vision_host_name, user_name, password):
      self._pi_vision_host_name  = pi_vision_host_name
      self._user = user_name
      self._password = password
    
    def get_pi_point_attributes(self, WEDID):

        route = self._pi_vision_host_name + '/piwebapi/points/' + WEDID + '/attributes'
        response = json.loads(requests.get(route,auth=('radixpiserver\sysadmin', 'NewDeal@2019'), verify=False).text)
        
        output = {}
        for item in response['Items']:
            output[item['Name']] = item['Value']

        return json.dumps(output, indent = 3)