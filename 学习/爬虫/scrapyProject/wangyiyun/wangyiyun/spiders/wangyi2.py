#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
通过查看js文件，找到加密方式
'''

'''
分别查看boy和girl搜索时的请求，发现ts, salt, sign是不一样的
在fanyi.min.js中找到几个参数的计算函数

ts = r = "" + (new Date).getTime(),
salt = i = r + parseInt(10 * Math.random(), 10);
sign = n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
e = key
'''
from urllib import request, parse


def youdao(key):
    url = 'https://music.163.com/#/artist?id=3684'
    # data和headers 都是直接复制网站中的请求数据

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_ntes_nnid=a519099829e0ed489627062a9c2fb877,1543058121492; _ntes_nuid=a519099829e0ed489'
                  '627062a9c2fb877; __f_=1543058122279; P_INFO=13763062252|1543058155|1|study|00&99|gud&154'
                  '2967136&study#gud&440300#10#0#0|&0|null|13763062252; UM_distinctid=1674a97d933322-0fb127'
                  '771a608a-6313363-1fa400-1674a97d9356bf; vjuids=4dbdacf1b.1674a97e57a.0.902759998f304; _'
                  '_gads=ID=1c495967928d8733:T=1544082989:S=ALNI_MZ_2ocV3yb_A4bLrE2-WqKRRpJhsw; _iuqxldmzr'
                  '_=32; __utmz=94650624.1545556265.1.1.utmcsr=ngwind.github.io|utmccn=(referral)|utmcmd=r'
                  'eferral|utmcct=/2018/08/14/Python%E4%B9%8BTime%E6%A8%A1%E5%9D%97/; WM_TID=eIrceT06J1xBF'
                  'QVRRFY4f7eZciYBibpI; hb_MA-BFF5-63705950A31C_source=mooc.study.163.com; hb_MA-BFF5-6370'
                  '5950A31C_u=%7B%22utm_source%22%3A%20%22cp-1018878377%22%2C%22utm_medium%22%3A%20%22shar'
                  'e%22%2C%22utm_campaign%22%3A%20%22commission%22%2C%22utm_content%22%3A%20%22%22%2C%22ut'
                  'm_term%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%7D; __remember_me=true; mail_p'
                  'sc_fingerprint=6f8b4bbdd12953fa4b7559bf1078973e; hb_MA-92E7-6C2BD5FB5ABF_source=study.16'
                  '3.com; hb_MA-92E7-6C2BD5FB5ABF_u=%7B%22utm_source%22%3A%20%22study.163.com%22%2C%22utm_m'
                  'edium%22%3A%20%22web_banner%22%2C%22utm_campaign%22%3A%20%22business%22%2C%22utm_content'
                  '%22%3A%20%2220190107%22%2C%22utm_term%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%'
                  '7D; _ga=GA1.2.1687637954.1547122628; Province=0; City=0; NNSSPID=8b06cdfa407247cd99f48bac'
                  '43e99eec; vjlast=1543144728.1547623849.21; vinfo_n_f_l_n3=eb1b742a5eb29ab4.1.7.1543144727'
                  '982.1546409512298.1547624268883; __utmc=94650624; MUSIC_U=cac450265aa764fd51cd8bcc601d2ff'
                  '2bac1a71990be98d1df5570b6d9b7e713a199e0226c0b6aaa55f1e57933b199e131b299d667364ed3; __csrf'
                  '=6ba5760dec8007ff1c4b8f68b5435def; WM_NI=Dveis79UOLlo524ctFyQGukUj%2BFB0JfPbjgKAHc68QArzc'
                  'pnwFgZSfiIaO%2FwxNnoOe1LzmTLISd4bNnbQSKcaelkou%2BWExFooTvUZ0dKApb9rLqUSKrzZiJo5a0VUfVXR08'
                  '%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee99e65aa894a4b6b1468c928fb2d85a879f8eaef774859484b3e2'
                  '53829098a4c12af0fea7c3b92a88aaab8af23dfb8b81adef65f7eefc84f74ebb8f8996ea5faaf58aa3b342a69'
                  '0ae8be6418398add7bb5b83aeb684f366b59aa9bbd26eab97afb0ae7dbc92a290ce6ff394b68ed7488b8dacd5'
                  'e146aebe9fb4ca69a3bba48cee7fe9898b99c565ad8cbab6d93ca8958f91e133b294bfb6d241b2a6968ac965f'
                  '7bf00b7d86e96889ed1bb37e2a3; JSESSIONID-WYYY=5Cz1QKl87isBs7rZm1Z58Gk4I7TTQNqg4%2BN%2Boc8y'
                  'XNdHWh3P5O8%2FNriItpZZO8U2gwVImhm8vnTxsWw0C5MalOvDqlDqn74wU1HO6dFg4%2FRdkiUz2NVEDHujIkIJp'
                  'dtM%5C8gtJIzx2g%5CZVRfj4e%2FUcDt2fo%2FC%5CYN9CaVkIEq%2FCmAA%2BNG7%3A1547719474099; __utma'
                  '=94650624.222583246.1545556265.1547693301.1547718854.11; __utmb=94650624.2.10.1547718854',
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }

    req = request.Request(url=url, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)


if __name__ == '__main__':
    youdao('girl')
