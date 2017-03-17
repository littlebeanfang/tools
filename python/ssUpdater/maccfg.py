# -*- coding:utf-8 -*-
import json
from bs4 import BeautifulSoup
import base64
from pprint import pprint
import os
import sys

cvtplfile=sys.argv[1]
serverfile=sys.argv[2]
updatefile=sys.argv[3]

# read config template
html_doc=open(cvtplfile, 'r')
soup = BeautifulSoup(html_doc, "html.parser")

# extract data part from config file
data = base64.b64decode(soup.data.string)
datajs = json.loads(data.decode())

# fetch server list
f = open(serverfile, 'r')
serverstrs = f.read().replace('\n','').split('|')
serverlist = []
for i in range(len(serverstrs)):
	serverlist.append(json.loads(serverstrs[i]))
print 'server info #: '+str(len(serverlist))

# change serverlist and write back
datajs['profiles'] = serverlist
soup.data.string = base64.b64encode(str(json.dumps(datajs)))
html_doc=open(updatefile, 'w')
html_doc.write(str(soup))