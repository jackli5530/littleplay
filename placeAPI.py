#coding=utf-8
import urllib2
import json
class placeApi:
    def place_api(self,query,city,num):
        try:
            #对百度地图api发送请求获取json
            url = 'http://api.map.baidu.com/place/v2/search?query=%s&' \
                  'page_size=10&page_num=0&scope=1&region=%s&output=json&ak=NYFRcc4A4UBQpq5qLdxhTcfx5DKn5C0H' % (query, city)
            req = urllib2.Request(url)
            request = urllib2.urlopen(req)
            jsons = request.read()
            #解析返回的json数据
            info = json.loads(jsons)
            #对json数据进行提取
            name = info['results'][num-1]["name"]
            address=info['results'][num-1]["address"]
            telephone=info['results'][num-1]["telephone"]
            #返回所需信息
            return name,address,telephone
        except Exception as e:
            print '发生异常:',e