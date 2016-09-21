#coding=utf-8
import re
import datetime

today = datetime.datetime.today()
today = '%s.%s.%s' % (today.year, today.month, today.day)
pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
f = open('ips.txt')
start = """
# update: <today> 

[General]
skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, localhost, *.local
bypass-tun = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12
loglevel = notify

[Rule]
FINAL,DIRECT

[Host]
"""
start = start.replace('<today>', today)
print start
for line in f.readlines():
    line = line.replace('\n', '')
    item = line.split('\t')
    if pat.match(item[0]):
        print '%s = %s' % (item[-1], item[0])
f.close()
