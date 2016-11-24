这个小程序是根据百度地图API进行酒店、银行、娱乐等信息查询出名字、地址、电话与总评分，现在仍在补充调试，纯属娱乐，切勿较真。
----------------------------------------------------
发送请求部分可以使用requests库，这样可以更加简洁,可以达到相同效果
improt requests
query=raw_input("输入查询项:")
city=raw_input("输入城市:")
num=int(raw_input("第几页:"))
url='http://api.map.baidu.com/place/v2/search?query=%s&' \
    'page_size=10&page_num=%d&scope=2&region=%s&output=json&ak=NYFRcc4A4UBQpq5qLdxhTcfx5DKn5C0H'%(query,num,city)
info=requests.get(url).json()
print info
print info['total']
print '名称：',info['results'][0].get("name")
print '地址：',info['results'][0].get("address")
print '电话：',info['results'][0].get("telephone")
print info['results'][0].get('detail_info').get('overall_rating'
