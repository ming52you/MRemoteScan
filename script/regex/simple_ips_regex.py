#!/usr/bin/env python
# coding=utf-8
# IP格式校验，该脚本ip格式是否正确,IP格式包括IP和IP段
# 调用方法：python simple_ips_regex.py 10.10.10.0/24 [debug/release]
# 支持格式包括：
# 10.10.10.1
# 10.10.*.*
# 10.10.10.0/24
# 10.10.10.1-10.10.10.254
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
if model_flag == "debug":
    print "The hosts is ", hosts,",and the format is ", ip_check(hosts)


#print ip_check("192.168.2.111-192.168.2.22")

