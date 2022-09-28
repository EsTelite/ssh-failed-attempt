from pygtail import Pygtail
import os
import requests
import itertools
from time import sleep

api_url = 'http://192.168.241.13:8000/failed/?host={}'.format(os.uname()[1])


for _ in itertools.repeat([]):
    sleep(5)
    for line in Pygtail("/var/log/auth.log"):
        if "pam_unix(sshd:auth)" in line:
            response = requests.get(api_url)
            print(response)
            sleep(1)
