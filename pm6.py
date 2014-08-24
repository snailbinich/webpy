#!/usr/bin/python

import urllib2
import re
import json
#content_stream = urllib2.urlopen('http://www.6pm.com/grazie-flossie-red')
#content = content_stream.read()
# with open(r'red.txt') as somefile:
#         content =  somefile.read()
            # ...more code
#result +=  content
#var dimensions = ["d3","d4"];


# getproductId
def get6PmData(url):


    content_stream = urllib2.urlopen(url)
    content = content_stream.read()
    result = dict()   

    result['productId'] =  re.search(r'(var[\s]productId[\s]*\=)([^;]+)',content).group(2)


    result['productName'] =  re.search(r'(var[\s]productName[\s]*\=)([^;]+)',content).group(2)


    result['brandName']  =  re.search(r'(var[\s]brandName [\s]*\=)([^;]+)',content).group(2)


    colorNames  =  re.search(r'(var[\s]colorNames [\s]*\=)([^;]+)',content).group(2)
    colorNames =  colorNames.replace("\n", "").strip().replace("\'","\"")

    colorNames = json.loads(colorNames)
    result['colorNames'] = colorNames
 


    dimensions = re.search(r'(dimensions[\s]*\=)([^;]+)',content).group(2)
    dimensions = json.loads(dimensions)
    result['dimensions'] = dimensions
    # for dimen in dimensions:
    #     result +=  dimen
        
    dimensionIdToNameJson = re.search(r'(dimensionIdToNameJson[\s]*\=)([^;]+)',content).group(2)
    result['dimensionIdToNameJson'] = json.loads(dimensionIdToNameJson)

    valueIdToName = re.search(r'(valueIdToNameJSON[\s]*\=)([^;]+)',content).group(2)
    valueIdtoNameJson = json.loads(valueIdToName)
    result['valueIdtoNameJson'] = valueIdtoNameJson


    stock =  re.search(r'(stockJSON[^;]+)',content).group().split("=")
    result['stock'] = json.loads(stock[1])
    # test = json.loads(stock[1])

    imgs = re.search(r'(http://[^\s]*MULTIVIEW.jpg)',content).group()
    result['imgs'] = imgs
    # #result +=  test
    # for item in test:
    #     for dimen in dimensions:
    #        #result +=  "color:", colorNames[item["color"].encode('utf-8')], "size" ,valueIdtoNameJson[item[dimen]]["value"]," stock ",item["onHand"]
    #         pass
    print json.dumps(result)
    return result
        


# if __name__=="__main__":
#     with open(r'urls.txt') as somefile:
#     	for line in somefile:
#     		reslove(line)
    		

#var colorNames = {
#'3':"Black",
#'158':"Blue",
#'401':"Grey",
#'574':"Purple",
#'585':"Red"
#}
#;



