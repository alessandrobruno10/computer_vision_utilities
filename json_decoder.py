'''
created on Tuesday the 26th of May 2020
@author: Alessandro Bruno
'''

#the lines of code down below allow for extracting fields from
#json objects catching them from a URL

#let's try out with a Json object coming out of a simple DB Query

import json
import requests

wjdata = requests.get('http://phplaravel-211194-641825.cloudwaysapps.com/api/interactive-campaign/31').json()
print(wjdata)
