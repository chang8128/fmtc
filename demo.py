
# -*- coding:utf-8 -*-

__author__ = 'Administrator'


from EmQuantAPI import *

def startCallback(message):
    print("[EmQuantAPI Python]", message)
    return 1
def demoQuoteCallback(quantdata):
    """
    DemoCallback 是EM_CSQ订阅时提供的回调函数模板。该函数只有一个为c.EmQuantData类型的参数quantdata
    :param quantdata:c.EmQuantData
    :return:
    """
    print ("demoQuoteCallback,", str(quantdata))
    
def cstCallBack(quantdata):
    '''
    cstCallBack 是日内跳价服务提供的回调函数模板
    '''
    for i in range(0, len(quantdata.Codes)):
        length = len(quantdata.Dates)
        for it in quantdata.Data.keys():
            print(it.decode(c_encodeType))
            for k in range(0, length):
                for j in range(0, len(quantdata.Indicators)):
                    print(quantdata.Data[it][j * length + k], " ",end = "")
                print()
   

#调用登录函数（激活后使用，不需要用户名密码）
loginResult = c.start("ForceLogin=1")

if(loginResult.ErrorCode != 0):
    print("login in fail")

# csc使用范例    
data = c.csc("300059.SZ", "OPEN,CLOSE,HIGH", "2016-10-10", "2016-10-10", "RowIndex=2,Ispandas=0")
print("csc输出结果======分隔线======")
if(not isinstance(data, c.EmQuantData)):
    print(data)
else:
    if data.ErrorCode != 0:
        print("request csc Error, ", data.ErrorMsg)
    else:
        for i in range(0, len(data.Indicators)):
            for j in range(0, len(data.Dates)):
                print("indicator=%s, value=%s" % (data.Indicators[i], str(data.Data[i][j])))

# csd使用范例
data = c.csd("300059.SZ,600425.SH", "open,close", "2016-07-01", "2016-07-06", "RowIndex=1,period=1,adjustflag=1,curtype=1,pricetype=1,year=2016,Ispandas=0")

print("csd输出结果======分隔线======")
if not isinstance(data, c.EmQuantData):
    print(data)
else:
    if data.ErrorCode != 0:
        print("request csd Error, ", data.ErrorMsg)
    else:
        for code in data.Codes:
            for i in range(0, len(data.Indicators)):
                for j in range(0, len(data.Dates)):
                    print(data.Data[code][i][j])

# css使用范例
data = c.css("300059.SZ, 000002.SZ, 000002.SH", "open,close", "TradeDate=20170308,Ispandas=0")
print("css输出结果======分隔线======")
if not isinstance(data, c.EmQuantData):
    print(data)
else:
    if data.ErrorCode != 0:
        print("request css Error, ", data.ErrorMsg)
    else:
        for code in data.Codes:
            for i in range(0, len(data.Indicators)):
                print(data.Data[code][i])

# sector使用范例
# data = c.sector("011019002001", "2016-04-26")
data = c.sector("001004", "2016-10-26")
if data.ErrorCode != 0:
    print("request sector Error, ", data.ErrorMsg)
else:
    print("sector输出结果======分隔线======")
    for code in data.Data:
        print(code)

# tradedate使用范例
data = c.tradedates("2016-09-01", "2016-09-12")
if data.ErrorCode != 0:
    print("request tradedates Error, ", data.ErrorMsg)
else:
    print("tradedate输出结果======分隔线======")
    for item in data.Data:
        print(item)

# getdate使用范例
data = c.getdate("20160426", -3, "Market=CNSESH")
if data.ErrorCode != 0:
    print("request getdate Error, ", data.ErrorMsg)
else:
    print("getdate输出结果======分隔线======")
    print(data.Data)

#实时行情订阅使用范例
data = c.csq('000850.SH', 'TIME,Now,Volume','Pushtype=1')
if data.ErrorCode != 0:
    print("request csq Error, ", data.ErrorMsg)
else:
    print("csq输出结果======分隔线======")
    text = input("press any key to cancel csq \r\n")
    #取消订阅
    data = c.csqcancel(data.SerialID)

#日内跳价服务使用范例
data = c.cst('300059.SZ,600000.SH', 'TIME,OPEN,HIGH,LOW,NOW', '100000', '101000')
if data.ErrorCode != 0:
    print("request cst Error, ", data.ErrorMsg)
else:
    print("cst输出结果======分割线======")
    input("press any key to quit cst \r\n")

#行情快照使用范例
data = c.csqsnapshot("000005.SZ,600602.SH,600652.SH,600653.SH,600654.SH,600601.SH,600651.SH,000004.SZ,000002.SZ,000001.SZ,000009.SZ", "PRECLOSE,OPEN,HIGH,LOW,NOW,AMOUNT")
if data.ErrorCode != 0:
    print("request csqsnapshot Error, ", data.ErrorMsg)
else:
    print("csqsnapshot输出结果======分割线======")
    for key,value in data.Data.items():
        print(key, ">>> ", end="")
        for v in value:
            print(v, " ", end="")
        print()

#获取专题报表使用范例
data = c.ctr("INDEXCOMPOSITION", "", "IndexCode=000001.SH,EndDate=2017-01-13")
if data.ErrorCode != 0:
    print("request ctr Error, ", data.ErrorMsg)
else:
    print("ctr输出结果======分割线======")
    for key,value in data.Data.items():
        for v in value:
            print(v, " ", end="")
        print()

#选股使用范例
data = c.cps("B_001004", "s0,OPEN,2017/2/27,1;s1,NAME", "[s0]>0", "orderby=rd([s0]),top=max([s0],100)")
if data.ErrorCode != 0:
    print("request cps Error, ", data.ErrorMsg)
else:
    print ("cps输出结果======分割线======")
    for it in data.Data:
       print (it)
key = None
#组合信息查询
data = c.pquery()
if(data.ErrorCode != 0):
    print("request pquery Error, ", data.ErrorMsg)
else:
    print("[key]:",end="")
    for index in range(0, len(data.Indicators)):
        print("\t", data.Indicators[index],end="")
    print("")
    for k,v in data.Data.items():
        if(key == None):
            key = k
        print(k,": ", end="")
        for vv in v:
            print("\t", vv, end="")
        print("")

orderdict = {'code':['300059.SZ','600000.SH'],
             'amount':[1000,200],
             'price':[13.11,12.12],
             'date':['2017-08-14','2017-08-24'],
             'time':['14:22:18','14:22:52'],
             'optype':[1,1],
             'cost':[0,3],
             'rate':[0,2]}
#组合下单
data = c.porder(key, orderdict, "this is a test")

if(data.ErrorCode != 0):
    print("porder Error, ", data.ErrorMsg)
else:
    print("order succeed")
#退出
data = logoutResult = c.stop()
print('ok')
