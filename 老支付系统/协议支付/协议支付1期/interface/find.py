#coding:utf-8
import json

import request

transNo = 'TR180712135909601631112'

print('####################查询协议开始##################')
##查询协议入参
data2 = {"transNo":transNo}
#查询协议请求地址
url2 = 'http://172.29.66.21:80/api/protocol/find'

t2 = request.request(url2, data2)

sss2 = json.loads(t2)
ss21 = sss2['data']
ss2 = json.loads(ss21)
print('transNo:'+transNo,'amount:'+ss2['amount'],'onpassageAmount:'+ss2['onpassageAmount'],'outAmount:'+ss2['outAmount'])

print('####################查询协议结束##################')

print(len(sss2.keys()))
print(sss2.keys())
print(len(ss2.keys()))
print(ss2.keys())