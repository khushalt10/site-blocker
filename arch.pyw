import time
from datetime import datetime as dt 

host_temp = r"C:\Users\admin\Desktop\block\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
ip = "127.0.0.1"
block_list = ["www.facebook.com","facebook.com","www.utorrent.com","twitter.com","www.twitter.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):
        print("WORK.....")
        with open(host_path,"r+") as file:
            content = file.read()
            for ws in block_list:
                if ws in content:
                    pass
                else:
                    file.write(ip+" "+ws+"\n")
    else:
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(ws in line for ws in block_list):
                    file.write(line)
            file.truncate()
        print("Funnn...")
    time.sleep(5)