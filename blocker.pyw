host_path = "C:\Windows\System32\drivers\etc\hosts"
host_temp="E:\Project\Python\Program\Website\hosts"
redirect = "127.0.0.1"
website_list = ["www.yahoo.co.in","www.instagram.com","www.myntra.com"]
import time
from datetime import datetime as dt

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day,7)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,8):
        print("blocker is running")
        with open(host_path,'r+') as file:
            file.seek(0)
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("blocker is not running")
    time.sleep(7)
