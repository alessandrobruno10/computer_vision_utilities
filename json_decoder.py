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
#print(wjdata)
#here is a couple of parent node fields such as name, id, publish_from
#print(wjdata.get('camera'))
#print(wjdata.get('camera_location'))
#print(wjdata.get('id'))
print(wjdata.get('campaing_interactive_content'))

#print((child1[0]))
#print((child[1]))

child1=(wjdata.get('content'))
print(child1)
