from PWA_interaction import PWApy
from dotenv import load_dotenv
import os

# Credentials
load_dotenv('.env')

# Use the sensitive data from the security file 
pi_vision_hostname = os.getenv('PI_VISION_HOSTNAME')
user = os.getenv('USER')
password = os.getenv('PASSWORD')

# instanciate obj for PWA interection 
pwa = PWApy(pi_vision_host_name=pi_vision_hostname, user_name= user, password= password)

# get pi point attributes
webid = 'F1DP72-6XVl5302c_uD52V8M7AOz4AAAUElBRlNFUlZFUjIwMThcw41ORElDRSBERSBJTkNSVVNUQcOHw4NPIChDT05ERU5TQURPUikuQ09OVEFET1IgREUgQUxBUk1FUw'
point_att = pwa.get_pi_point_attributes(WEDID=webid)

print(point_att)
