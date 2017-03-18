# -*- coding:utf-8 -*-
import requests
import re
import json
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# mode: 1-shadowsocks, 2-freevpnss
mode=2
if mode==1:
	r = requests.get("http://www.ishadowsocks.me/")
elif mode==2:
	r = requests.get("https://get.freevpnss.me/")
else:
	pass

r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, "html.parser")
if mode==1:
	pw = soup.find_all(text=re.compile(u'密码'))
	server = soup.find_all(text=re.compile(u'服务器'))
	port = soup.find_all(text=re.compile(u'端口'))
elif mode==2:
	pw = soup.find_all(text=re.compile(u'码'))
	server = soup.find_all(text=re.compile(u'服务器地址'))
	port = soup.find_all(text=re.compile(u'端口'))
else:
	pass

def f(s):
	ssplit=s.split(u':')
	ssplit2=s.split(u'：')
	if len(ssplit)>1:
		return ssplit[1]
	elif len(ssplit2)>1:
		return ssplit2[1]
	else:
		return ' '

if mode==1:
	pw = list(map(f, [pw[0], pw[2], pw[4]]))
	server = list(map(f, [server[0], server[1], server[2]]))
	port = list(map(f, [port[0], port[1], port[2]]))
elif mode==2:
	pw = list(map(f, [pw[5], pw[6], pw[7]]))
	server = list(map(f, [server[3], server[4], server[5]]))
	port = list(map(f, [port[0], port[1], port[2]]))
else:
	pass

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
