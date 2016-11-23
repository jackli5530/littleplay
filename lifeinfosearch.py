#coding=utf-8
#导入api类
from placeAPI import placeApi
#输入查询条件
query=raw_input("输入查询项:")
city=raw_input("输入城市:")
page=raw_input("第几页:")
index=int(raw_input("输入查询第几项,不能大于10："))
#实例化类
info=placeApi()
#将方法中的返回值赋值变量，方法中返回多个值
name,address,telephone,overall=info.place_api(query,city,index,page)
print name,address,telephone,overall

