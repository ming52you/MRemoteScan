#!/usr/bin/env python
# coding=utf-8

import re

#IP 格式校验

def print_test():
    print "test"

#IP 检查IP格式，例如：10.10.10.1
def ip_check(string):
    pattern = re.compile(r'^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$')
    result = pattern.match(string)
    if result:
        print result.group()
        return True
    else:
        return False


ip_check("0.0.0.0")



