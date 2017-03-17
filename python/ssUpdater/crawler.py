# -*- coding:utf-8 -*-
import requests
import re
import json
from bs4 import BeautifulSoup
from prettytable import PrettyTable

r = requests.get("http://www.ishadowsocks.me/")
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, "html.parser")
pw = soup.find_all(text=re.compile(u'密码'))
server = soup.find_all(text=re.compile(u'服务器'))
port = soup.find_all(text=re.compile(u'端口'))

def f(s):
    return s.split(':')[1]


pw = list(map(f, [pw[0], pw[2], pw[4]]))
server = list(map(f, [server[0], server[1], server[2]]))
port = list(map(f, [port[0], port[1], port[2]]))
l = []
for i in range(3):
        d = {"method": "aes-256-cfb", "server": server[i], "password": pw[i], "server_port": int(port[i]), "local_port":1080, "timeout":600}
        l.append(d)

with open('iss.json', 'wt') as out:
	res = json.dump(l[0], out, sort_keys=True, indent=4, separators=(',', ': '))

info = PrettyTable(["服务器", "端口", "密码"])
for i in range(3):
    info.add_row([server[i], port[i], pw[i]])
print(info)

with open('iss_mac.json', 'wt') as out:
	for i in range(len(l)):
		res = json.dump(l[i], out, sort_keys=True, indent=4, separators=(',', ': '))
		if not i==len(l)-1:
			out.write('|')
