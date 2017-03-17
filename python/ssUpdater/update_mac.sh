#!/bin/bash
tmplfile="./ss.template"
cvtplfile="./ss.xml"
serverfile='./iss_mac.json'
updatefile='./ss_update.xml'
plistfile='./ss.plist'
echo "Fetch free accounts from ishadowsocks..."
python crawler.py
plutil -convert xml1 $tmplfile -o $cvtplfile
python maccfg.py $cvtplfile $serverfile $updatefile
plutil -convert binary1 $updatefile -o $plistfile
defaults import clowwindy.ShadowsocksX $plistfile
open /Applications/ShadowsocksX.app
rm $cvtplfile $updatefile $plistfile