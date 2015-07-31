#!/usr/bin/env python
# coding=utf-8

# 读取NMAP运行结果

from xml.dom import minidom

file = "./test/nmap_detail.xml"

doc = minidom.parse(file)
root  = doc.documentElement

host_nodes = root.getElementsByTagName("host")
print root.nodeName

for tmp_host_node in host_nodes:
        print tmp_host_node.nodeName

host_node = ""
if len(host_nodes) > 0:
        host_node = host_nodes[0]
print host_node.nodeName


os = host_node.getElementsByTagName("os")
if os == None:
        print "Error"
else:
        if len(os) > 0:
                print os[0].nodeName
                osmatch = os[0].getElementsByTagName("osmatch")
                if osmatch == None:
                        print "Error"
                else:
                        
                        if len(osmatch) > 0:
                                print osmatch[0].getAttribute("name")
                        else:
                                print "Error Size"
        else:
                print "Error Size"


