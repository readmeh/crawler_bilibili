# -*- config: utf-8 -*-
# @File  : sendComment.py
# @Auther: Hxp
# @Date  : 2021/2/20 : 0:43
# @ 发送B站弹幕

import requests
import io
import time, datetime
import re

def sendRoll(your_msg):
    url = "https://api.live.bilibili.com/msg/send",
    dat = {
    "color": "16777215",
    "fontsize": "25",
    "mode": "1",
    "msg": your_msg,
    "rnd": "1613752490",
    "roomid": "3822389",
    "bubble": "0",
    "csrf_token": "1e5ddb99c3719d05d3f7990b87f8ffb4",
    "csrf": "1e5ddb99c3719d05d3f7990b87f8ffb4",
    }

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Content-Length": "163",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "buvid3=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; _uuid=8EA2DB3A-7AB3-8FA6-A948-D20D2A5237B441478infoc; CURRENT_FNVAL=80; bsource=search_baidu; blackside_state=1; sid=bd2t5r8m; fingerprint=534d613ffdc5588fd5b9c4971a48a088; buvid_fp=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; buvid_fp_plain=17BBB8B4-07AE-4FD1-BE12-D0156A1763DA143073infoc; SESSDATA=67e154bc%2C1629303472%2C26000%2A21; bili_jct=1e5ddb99c3719d05d3f7990b87f8ffb4; DedeUserID=269850875; DedeUserID__ckMd5=48fd6883b751d4ac; rpdid=|(um)Rl~kRY)0J'uYuJ~lu~R|; LIVE_BUVID=AUTO8316137519418592; PVID=5; _dfcaptcha=ddaca5f51ff84d4f13ec2eab32f5e8fd",
        "DNT": "1",
        "Host": "api.live.bilibili.com",
        "Origin": "https://live.bilibili.com",
        "Referer": "https://live.bilibili.com/3822389?visit_id=5pe0wlj3ctmo",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
}

    response = requests.post(url, data = dat, headers = headers)
    print(response.text[vlist][pic])

def getNewVideoData(mid):
    videos_url = "https://api.bilibili.com/x/space/arc/search?mid={}&pn=1&ps=1".format(mid)
    dict = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "api.bilibili.com",
        "TE": "Trailers",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
}

    response = requests.get(videos_url,headers=dict)
    try:
        response_json = response.json()
        #print(response_json[data])
    except  ValueError:
        print("json 解析失败：{}".format(resp.text))
    else:
        return response_json

def downloadCover(cover_image_url):
    #下载封面图
    res = requests.get('https:{}'.format(cover_image_url))
    # 初始化BytesIO对象并且写入数据
    s = io.BytesIO(res.content)
    #print(s.format)  # 获取图片的格式
    #print(s.size)  # 获取图片的大小
    r2 = io.BytesIO()  # 创建一个空的Bytes对象
    r2 = s.getvalue()  # 这个就是保存的图片字节流
    f = open('coverImage.jpg', 'wb')
    f.write(r2)
    f.close()

def saveComment(AId, BvId,message):
    url = "https://api.bilibili.com/x/v2/reply/add"
    Referer = "https://www.bilibili.com/video/{}".format(BvId)
    headers = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Content-Length": "127",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Cookie": "finger=-1486130818; buvid3=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; _uuid=8EA2DB3A-7AB3-8FA6-A948-D20D2A5237B441478infoc; CURRENT_FNVAL=80; blackside_state=1; sid=bd2t5r8m; fingerprint=534d613ffdc5588fd5b9c4971a48a088; buvid_fp=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; buvid_fp_plain=17BBB8B4-07AE-4FD1-BE12-D0156A1763DA143073infoc; SESSDATA=67e154bc%2C1629303472%2C26000%2A21; bili_jct=1e5ddb99c3719d05d3f7990b87f8ffb4; DedeUserID=269850875; DedeUserID__ckMd5=48fd6883b751d4ac; rpdid=|(um)Rl~kRY)0J'uYuJ~lu~R|; LIVE_BUVID=AUTO8316137519418592; PVID=1; CURRENT_QUALITY=80; bsource=search_baidu; _dfcaptcha=869426da4675655a4ca4b388f67aa460; bfe_id=1bad38f44e358ca77469025e0405c4a6",
        "DNT": "1",
        "Host": "api.bilibili.com",
        "Origin": "https://www.bilibili.com",
        "Referer": Referer,
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }

    dat = {
        "oid": AId,
        "type": "1",
        "message": message,
        "plat":"1",
        "ordering":"heat",
        "jsonp": "jsonp",
        "csrf": "1e5ddb99c3719d05d3f7990b87f8ffb4",
    }

    response = requests.post(url, data=dat, headers=headers)
    print(response)
    response_json = response.json()
    return response_json['data']['rpid_str']

def createComment(AId, videoJson):
    #生成评论

    ## 视频类型是否为转载
    if videoJson['data']['list']['vlist'][0]['copyright'] == '':
        v_copyright = "转载"
        ## 如果是转载验证是否提供源链接
        if re.search("https://",videoJson['data']['list']['vlist'][0]['description']):
            v_original_line = "是否给出原链接：是\n简介: {}".format(videoJson['data']['list']['vlist'][0]['description'])
        else:
            v_original_line = "\n是否给出原链接：否"

    elif videoJson['data']['list']['vlist'][0]['copyright'] == '1':
        v_copyright = "自制"
    else:
        v_copyright = "未知(不确定这个分类是不是对的)"

    messages = """标题: {}
作者：@{}
视频时长: {}
发布时间: {}
视频总数: {}
aid: {}
bid: {}
视频类型: {}
{}
    """.format(
        videoJson['data']['list']['vlist'][0]['title'],
        videoJson['data']['list']['vlist'][0]['author'],
        videoJson['data']['list']['vlist'][0]['length'],
        time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(videoJson['data']['list']['vlist'][0]['created'])),
        videoJson['data']['page']['count'],
        AId,
        videoJson['data']['list']['vlist'][0]['bvid'][2:],
        v_copyright,
        v_original_line
    )

    return messages

#跟踪寂照庵最新视频发送统计信息
def jizhaoanBot():
    NewVideoJson = getNewVideoData(mid=1468726245)
    currentVideosNum =NewVideoJson['data']['page']['count']

    NewVideoJson = getNewVideoData(mid=1468726245)
    currentVideosNum = NewVideoJson['data']['page']['count']

    # 最新视频ID
    BvId = NewVideoJson['data']['list']['vlist'][0]['bvid']
    AId = NewVideoJson['data']['list']['vlist'][0]['aid']

    # 评论
    message = createComment(AId=AId, videoJson=NewVideoJson)
    print(message)
    saveComment(AId=AId, BvId=BvId, message=message)

#获取消息中心页面回复数据
def getRepply():
    url = "https://api.bilibili.com/x/msgfeed/reply"


    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection":"keep-alive",
        "Cookie":"buvid3=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; _uuid=8EA2DB3A-7AB3-8FA6-A948-D20D2A5237B441478infoc; CURRENT_FNVAL=80; blackside_state=1; sid=bd2t5r8m; fingerprint=534d613ffdc5588fd5b9c4971a48a088; buvid_fp=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; buvid_fp_plain=17BBB8B4-07AE-4FD1-BE12-D0156A1763DA143073infoc; SESSDATA=67e154bc%2C1629303472%2C26000%2A21; bili_jct=1e5ddb99c3719d05d3f7990b87f8ffb4; DedeUserID=269850875; DedeUserID__ckMd5=48fd6883b751d4ac; rpdid=|(um)Rl~kRY)0J'uYuJ~lu~R|; LIVE_BUVID=AUTO8316137519418592; PVID=3; CURRENT_QUALITY=0; bfe_id=1bad38f44e358ca77469025e0405c4a6",
        "DNT":"1",
        "Host":"api.bilibili.com",
        "Proxy-Authorization":"Basic MTpDaUpDUm1SbFlqQTVaVFUyTlRRM1lXUm1ZamcwWVdWa1l6WmxOVGxtWVRkbU5UbGpFQUFZc1FNZ0NTZ0dNUGFpQkRvQ1ZWTlNEMjVsZEhkdmNtc3RaWGhoYlM1MWMxb0FnZ0VDZW1nPSRFMGtKdGRUcEFNUGpKNHBwK1ZNQU1MUVhkSGlRT1lQNEtoWmhpSmg4MmhFQ01hdjVGbXVOaGpoRVErSXpER0U2Z3VYTmppZ2tQci9NM09ZTTQrRWdPWkg5STJWNHpoZHRTVjk1MFprWmtJNXhoUDJJRDhnT1N4bTBFMWdp",
        "TE":"Trailers",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }

    response = requests.get(url = url, headers = headers)
    print('replyid',response.json()['data']['items'][0]['id'],
          '\nvid',response.json()['data']['items'][0]['item']['subject_id'],
          '\nrid',response.json()['data']['items'][0]['item']['root_id'],
          '\nsid',response.json()['data']['items'][0]['item']['source_id'],
          '\nmsg',response.json()['data']['items'][0]['item']['source_content'])

def SupplementDataReply(aid,BvId,rid,message):
    url = 'https://api.bilibili.com/x/v2/reply/add'
    Referer = "https://www.bilibili.com/video/{}".format(BvId)

    headers = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Cookie": "finger=-1486130818; buvid3=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; _uuid=8EA2DB3A-7AB3-8FA6-A948-D20D2A5237B441478infoc; CURRENT_FNVAL=80; blackside_state=1; sid=bd2t5r8m; fingerprint=534d613ffdc5588fd5b9c4971a48a088; buvid_fp=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; buvid_fp_plain=17BBB8B4-07AE-4FD1-BE12-D0156A1763DA143073infoc; SESSDATA=67e154bc%2C1629303472%2C26000%2A21; bili_jct=1e5ddb99c3719d05d3f7990b87f8ffb4; DedeUserID=269850875; DedeUserID__ckMd5=48fd6883b751d4ac; rpdid=|(um)Rl~kRY)0J'uYuJ~lu~R|; LIVE_BUVID=AUTO8316137519418592; PVID=3; CURRENT_QUALITY=0; bfe_id=5db70a86bd1cbe8a88817507134f7bb5",
        "DNT": "1",
        "Host": "api.bilibili.com",
        "Referer": Referer,
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }

    createRequest = {
        "oid":aid,
        "type":"1",
        "root":rid,
        "parent":rid,
        "message":message,
        "plat":"1",
        "ordering":"heat",
        "jsonp":"jsonp",
        "csrf":"1e5ddb99c3719d05d3f7990b87f8ffb4"
    }

    response = requests.post(url=url, headers=headers, data=createRequest)

if __name__ == '__main__':
    #sendRoll(your_msg="hhh")
    #mid = input("请输入uid：")

    #获取回复数据
    getRepply()

    #下载封面
    #downloadCover(cover_image_url=NewVideoJson['data']['list']['vlist'][0]['pic'])

    #jizhaoanBot()

    SupplementDataReply(aid=629365002,
                        BvId="BV1Sb4y1R7ju",
                        rid=4163841497,
                        message="封面图：//i0.hdslb.com/bfs/archive/42ff067df7e2364ef581efeb908fade9f42a3f2c.jpg")

    """,
卧龙寺的计数工程就到这里吧
视频总数：30888
初次更新时间：2018-04-22 00:06:01
AV：22400052
最后更新时间：2021-01-21 00:34:06
BV：1dX4y1K7ta
粉丝总数：96.5万
创价学会祝您生活愉快
曲终未必人散,有缘自会相逢~~
2021.1.21

获取视频tag，问号后面是视频aid
https://api.bilibili.com/x/web-interface/view/detail/tag?aid=713771662

回复评论的表单数据
oid	"204266108"#视频aid
type	"1"
root	"4162739505"
parent	"4162739505"
message	"test"
plat	"1"
ordering	"heat"
jsonp	"jsonp"
csrf	"1e5ddb99c3719d05d3f7990b87f8ffb4"
回复评论的请求头
Accept
	application/json, text/javascript, */*; q=0.01
Accept-Encoding
	gzip, deflate, br
Accept-Language
	zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection
	keep-alive
Content-Length
	138
Content-Type
	application/x-www-form-urlencoded; charset=UTF-8
Cookie
	buvid3=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; _uuid=8EA2DB3A-7AB3-8FA6-A948-D20D2A5237B441478infoc; CURRENT_FNVAL=80; blackside_state=1; sid=bd2t5r8m; fingerprint=534d613ffdc5588fd5b9c4971a48a088; buvid_fp=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; buvid_fp_plain=17BBB8B4-07AE-4FD1-BE12-D0156A1763DA143073infoc; SESSDATA=67e154bc%2C1629303472%2C26000%2A21; bili_jct=1e5ddb99c3719d05d3f7990b87f8ffb4; DedeUserID=269850875; DedeUserID__ckMd5=48fd6883b751d4ac; rpdid=|(um)Rl~kRY)0J'uYuJ~lu~R|; LIVE_BUVID=AUTO8316137519418592; PVID=1; CURRENT_QUALITY=0; bfe_id=61a513175dc1ae8854a560f6b82b37af
DNT
	1
Host
	api.bilibili.com
Origin
	https://www.bilibili.com
Referer
	https://www.bilibili.com/video/BV1kh411r7Hc
TE
	Trailers
User-Agent
	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0

直接评论的表单数据
"oid": AId,
"type": "1",
"message": message,
"plat":"1",
"ordering":"heat",
"jsonp": "jsonp",
"csrf": "1e5ddb99c3719d05d3f7990b87f8ffb4",

Accept-Encoding
	gzip, deflate, br
Accept-Language
	zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Cache-Control
	max-age=0
Connection
	keep-alive
Cookie
	buvid3=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; _uuid=8EA2DB3A-7AB3-8FA6-A948-D20D2A5237B441478infoc; CURRENT_FNVAL=80; blackside_state=1; sid=bd2t5r8m; fingerprint=534d613ffdc5588fd5b9c4971a48a088; buvid_fp=A73A4074-CD1F-8C6C-BE4B-6CB897E01AB538498infoc; buvid_fp_plain=17BBB8B4-07AE-4FD1-BE12-D0156A1763DA143073infoc; SESSDATA=67e154bc%2C1629303472%2C26000%2A21; bili_jct=1e5ddb99c3719d05d3f7990b87f8ffb4; DedeUserID=269850875; DedeUserID__ckMd5=48fd6883b751d4ac; rpdid=|(um)Rl~kRY)0J'uYuJ~lu~R|; LIVE_BUVID=AUTO8316137519418592; PVID=3; CURRENT_QUALITY=0; bfe_id=1bad38f44e358ca77469025e0405c4a6
DNT
	1
Host
	api.bilibili.com
Origin
	https://message.bilibili.com
Referer
	https://message.bilibili.com/?spm_id_from=333.999.b_696e7465726e6174696f6e616c486561646572.35
TE
	Trailers
User-Agent
	Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0
"""