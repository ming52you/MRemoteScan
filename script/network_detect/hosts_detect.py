#!/usr/bin/env python
# coding=utf-8
# 主机探测，发现指定IP或IP段中存活的主机
# 调用方法：python hosts_detect.py 10.10.10.1-10.10.10.254 [debug/release]

import nmap
import time
import sys
from regex.ips_regex import *

DEBUG_MAX_ARGC = 3
RUN_MAX_ARGC = 2

argc = len(sys.argv)

if argc < RUN_MAX_ARGC or argc > DEBUG_MAX_ARGC:
    print "Error:The number of arguments is error."
    sys.exit()

hosts = ""
model_flag = "release"
if argc == DEBUG_MAX_ARGC:
    model_flag = sys.argv[DEBUG_MAX_ARGC - 1]

if model_flag != "release" and model_flag != "debug":
    print "Error:The argument of model is error."
    sys.exit(1)

if model_flag == "debug":
    print "The current model is: ",sys.argv[RUN_MAX_ARGC]

hosts = sys.argv[1]
if ips_check(hosts) == False:
    if model_flag == "debug":
        print "Error:The host's format is error!"
    sys.exit(1)
else:
    if model_flag == "debug":
        print "The host is ",hosts

if model_flag == "debug":
    start_time = time.time()
#基于nmap的主机探测
try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print('Exception:Nmap not found',sys.exc_info()[0])
    sys.exit(1)
except:
    print('Exception:Unexpected error:',sys.exc_info()[0])
    sys.exit(1)

nm.scan(hosts ,arguments="-sP")

#print nm.all_hosts()
for host in nm.all_hosts():
    print host

end_time = time.time()
if model_flag == "debug":
    print "%f s" % (end_time-start_time)

