from dotenv import load_dotenv
load_dotenv()
import os

import requests

# If there is no ip variable, the machine's IP will be used by the API
IP = os.getenv('IP') or ''

r = requests.post('https://infomaniak.com/nic/update', 
                    data = {
                        'hostname': os.getenv('HOSTNAME'),
                        'myip': IP
                    }, 
                    auth=(os.getenv('USER'), os.getenv('PASS')))
print(r.status_code)
