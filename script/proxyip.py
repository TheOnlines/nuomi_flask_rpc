#!/usr/bin/env python
# encoding: utf-8
"""
Spider ip proxy. Website: http://www.xicidaili.com/nn
Authors: idKevin
Date: 20170717
"""

from bs4 import BeautifulSoup
import urllib2
import time
import socket
import random
import re

def getContent(Url):
    """ Get the web site content.  """


    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'}
    req = urllib2.Request(Url, headers=header)       # request

    while True:
        try:
            response = urllib2.urlopen(req).read()   # Web site content
            break
        except urllib2.HTTPError as e:     # Ouput log to debug easily
            print 1, e
            time.sleep(random.choice(range(5, 20)))
        except urllib2.URLError as e:
            print 2, e
            time.sleep(random.choice(range(10, 30)))
        except socket.timeout as e:
            print 3, e
            time.sleep(random.choice(range(15, 20)))
        except Exception as e:
            print 4, e
            time.sleep(random.choice(range(10, 20)))

    return response                        # The website content

def extractIPAddress(content):
    """ Extract web IP address and port. """
    proxys = []                                   # proxy list
    soup = BeautifulSoup(content, 'html.parser')  # soup object
    trs = soup.find_all('tr')                     # extract tr tag
    for tds in trs[1:]:
        td = tds.find_all('td')                   # extract td tag
        proxys.append(str(td[1].contents[0]) + ":" + str(td[2].contents[0]))

    return proxys

def getProxys():
    """ main function. """
    Url = 'http://www.xicidaili.com/nn/1'   # assign relevant url
    content = getContent(Url)               # achieve html content
    proxys = extractIPAddress(content)      # achieve proxys
    # for e in proxys:                        # output proxy on screen
    #     print e

    return proxys
def testProxys(proxys):
    """ Test the proxys. """
    validProxys = []
    Url = "http://ip.chinaz.com/getip.aspx"
    for proxy in proxys:
        try:
            # set proxy
            proxy_handler = urllib2.ProxyHandler({'http':proxy, 'https':proxy})
            opener = urllib2.build_opener(proxy_handler)
            urllib2.install_opener(opener)
            # request website
            response = urllib2.urlopen(Url, timeout=5).read()

            # set filtration condition according website
            if re.findall('{ip:.*?,address:..*?}', response) != []: # remove invalid proxy
                validProxys.append(proxy)
                print "%s\t%s" % (proxy, response)
        except Exception as e:
            # print "%s\t%s" % (proxy, "invalid")
            continue

    return validProxys
property = getProxys()
print testProxys(property)