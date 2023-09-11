import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"

websites_to_block = ['www.youtube.com','youtube.com']

redirect_localhost = '127.0.0.1'

work_start = dt.now().replace(hour=8, minute=0, second=0)
work_end = dt.now().replace(hour=17, minute=0, second=0)
print(work_start)

while True:
    if work_start < dt.now() < work_end:
        print("This is working hours...")
        with open(hosts_path, "r+") as file:
            hosts = file.read()
            for web in websites_to_block:
                if web in hosts:
                    pass
                else:
                    file.write(redirect_localhost + " " + web + "\n")
    else:
        print("Fun Hours")
        with open(hosts_path, "r+") as file:
            hosts = file.readlines()
            file.seek(0)
            for line in hosts:
                if not any(web in line for web in websites_to_block):
                    file.write(line)
            file.truncate()
        print("Fun Hours...")
    time.sleep(5)