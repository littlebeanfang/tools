import urllib
import requests
import re
import os
import sys

#### var definition
# # source url for pdf list page, e.g.
srcurl = 'http://www.stat.cmu.edu/~larry/=stat705/'
# downloading base url, e.g.
baseurl = 'http://www.stat.cmu.edu/~larry/=stat705/'
# package to store the downloaded files, e.g.
pkgname = '36_705_Intermediate_Statistics'

# srcurl = 'http://cs229.stanford.edu/materials.html'
# baseurl = 'http://cs229.stanford.edu/'
# pkgname = 'CS_229_Machine_Learning_Course_Materials'

# regex for pdf files
reg = '<a\s+href\s*=\s*\"([^.>]+\.pdf)\">'

#### process
print "0. make dir====================="+pkgname
pkgbase = 'pdfsDown/'
pkg = pkgbase+pkgname
if not os.path.exists(pkgbase):
	os.mkdir(pkgbase)
if not os.path.exists(pkg):
	os.mkdir(pkg)
print "1. fetch list source page======="
r = requests.get(srcurl)
# print r.content

print "2. filter list=================="
regex = re.compile(reg)
filelist = regex.findall(r.content)
print filelist

print "3. downloading=================="
for filename in filelist:
	print baseurl + filename
	urllib.urlretrieve(baseurl + filename, pkg+'/'+filename.split('/')[-1])
