#!/usr/bin/env python
# coding=utf-8
# IP格式校验，该脚本ip格式是否正确,IP格式包括IP和IP段
# 调用方法：python ips_regex.py 10.10.10.0/24 [debug/release]
# 支持格式包括：
# 10.10.10.1
# 10.10.*.*
# 10.10.10.0/24
# 10.10.10.1-254

import re
import sys

#IP 检查IP格式，例如：10.10.10.1
def ip_check(string):
    pattern = re.compile(r'^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$')
    result = pattern.match(string)
    if result:
        return True
    else:
        return False

#IP 检查IP格式，例如：10.10.*.*
def ip_check2(string):
    pattern = re.compile(r'^([01]?\d\d?|2[0-4]\d|25[0-5]|\*)\.([01]?\d\d?|2[0-4]\d|25[0-5]|\*)\.([01]?\d\d?|2[0-4]\d|25[0-5]|\*)\.([01]?\d\d?|2[0-4]\d|25[0-5]|\*)$')
    result = pattern.match(string)
    if result:
        return True
    else:
        return False

            
#IP 检查IP格式，例如192.168.24.0-254
def ip_check3(string):
    pattern = re.compile(r'^([01]?\d\d?|2[0-4]\d|25[0-5]|\*)\.([01]?\d\d?|2[0-4]\d|25[0-5]|\*)\.([01]?\d\d?|2[0-4]\d|25[0-5]|\*)\.([01]?\d\d?|2[0-4]\d|25[0-5]|\*)-([01]?\d\d?|2[0-4]\d|25[0-5]|\*)$')
    result = pattern.match(string)
    if result:
        return True
    else:
        return False

#IP 检查IP格式，例如192.168.24.0/24
def ip_check4(string):
    pattern = re.compile(r'^([01]?\d\d?|2[0-4]\d|25[0-5]|\*)\.([01]?\d\d?|2[0-4]\d|25[0-5]|\*)\.([01]?\d\d?|2[0-4]\d|25[0-5]|\*)\.([01]?\d\d?|2[0-4]\d|25[0-5]|\*)/([01]?\d\d?|2[0-4]\d|25[0-5]|\*)$')
    result = pattern.match(string)
    if result:
        return True
    else:
        return False


def ips_check(string):
    return ip_check(string) or ip_check2(string) or ip_check3(string) or ip_check4(string)


####################################################################################

