#!/usr/bin/env python
# coding=utf-8
import nmap
import time
import sys
import socket

DEBUG_MAX_ARGC = 3
RUN_MAX_ARGC = 2


########################################################################
## 函数声明
def valid_ip(address):
    try:
        socket.inet_aton(address)
        return True
    except:
        return False

print valid_ip('192.168.24.111')
print valid_ip('10.10.10.0/24')
print valid_ip('asdfasdf')




########################################################################
argc = len(sys.argv)

if argc < RUN_MAX_ARGC or argc > DEBUG_MAX_ARGC:
    print "Error:The number of arguments is error."
    sys.exit()

hosts = ""
model_flag = "release"
if argc == RUN_MAX_ARGC:
    model_flag = sys.argv[RUN_MAX_ARGC]

if model_flag != "release" and model_flag != "debug":
    print "Error:The argument of model is error."

print "The current model is: ",sys.argv[RUN_MAX_ARGC]

hosts = sys.argv[1]
print hosts



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

nm.scan(hosts="10.10.10.0/24" ,arguments="-sS")

print nm.all_hosts()

end_time = time.time()
print "%f s" % (end_time-start_time)

