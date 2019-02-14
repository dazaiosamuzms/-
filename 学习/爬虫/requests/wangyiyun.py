#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

import requests


url = 'https://music.163.com/weapi/song/enhance/player/url'


# :

params = {
    'params': 'jCzCrGKoppa8UXG4QewWm68kbWhaTA9O2GGdEfUMnQ9SXMF16Ao+QxR2kirJxKeHZPbWKgXc/conoUupq80JETWnH+Y1aIUbkGG6KqEgHg2w2110AmXoizK2sHE8hvzvjRiOIjSJd4Gv/ZTUKeyPwEx+9D2mZ5Cl9GdepqUb0kq5AUvKoKJxdgvNDl6I201a',
    'encSecKey': '0dbf7dc5ff106206a10d8045f6481de41cbaadd9e746648fa821d8b5e1e56ec82d4c7fba8a7b61dfda72e8495bd1027da827770f91883bbd6004b6a631ceaa3a772a41526c25e6636449dc928cb0f7d9867acb1380613f030aa55c86f971001cf3ab3629ad851a7074bd60186f1636009f20944704cbfdebcb688828b9941e1e',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Content-Length': str(len(params)),
    # 'Cache-Control': 'no-store',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    # 'Content-Encoding': 'gzip',
    # 'Content-Type': 'text/plain;charset=UTF-8',
    # 'Date': 'Fri, 25 Jan 2019 08:54:54 GMT',
    # 'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT',
    # 'Transfer-Encoding': 'chunked',
    # 'Server': 'nginx',
    # 'Vary': 'Accept-Encoding',
    # 'X-From-Src': '120.229.159.61',
    # 'X-Via': 'MusicServer',

}

cookies = {
    '_ntes_nnid': 'a519099829e0ed489627062a9c2fb877,1543058121492',
    '_ntes_nuid': 'a519099829e0ed489627062a9c2fb877',
    '__f_': '1543058122279',
    'P_INFO': '13763062252|1543058155|1|study|00&99|gud&1542967136&study#gud&440300#10#0#0|&0|null|13763062252',
    'UM_distinctid': '1674a97d933322-0fb127771a608a-6313363-1fa400-1674a97d9356bf',
    'vjuids': '4dbdacf1b.1674a97e57a.0.902759998f304',
    '__gads': 'ID=1c495967928d8733:T=1544082989:S=ALNI_MZ_2ocV3yb_A4bLrE2-WqKRRpJhsw',
    '_iuqxldmzr_': '32',
    '__utmz': '94650624.1545556265.1.1.utmcsr=ngwind.github.io|utmccn=(referral)|utmcmd=referral|utmcct=/2018/08/14/Python%E4%B9%8BTime%E6%A8%A1%E5%9D%97/',
    'WM_TID': 'eIrceT06J1xBFQVRRFY4f7eZciYBibpI',
    'hb_MA-BFF5-63705950A31C_u': '%7B%22utm_source%22%3A%20%22cp-1018878377%22%2C%22utm_medium%22%3A%20%22share%22%2C%22utm_campaign%22%3A%20%22commission%22%2C%22utm_content%22%3A%20%22%22%2C%22utm_term%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%7D',
    '__remember_me': 'true',
    'mail_psc_fingerprint': '6f8b4bbdd12953fa4b7559bf1078973e',
    'hb_MA-92E7-6C2BD5FB5ABF_source': 'study.163.com',
    'hb_MA-92E7-6C2BD5FB5ABF_u': '%7B%22utm_source%22%3A%20%22study.163.com%22%2C%22utm_medium%22%3A%20%22web_banner%22%2C%22utm_campaign%22%3A%20%22business%22%2C%22utm_content%22%3A%20%2220190107%22%2C%22utm_term%22%3A%20%22%22%2C%22promotional_id%22%3A%20%22%22%7D',
    '_ga': 'GA1.2.1687637954.1547122628',
    'Province': '0',
    'City': '0',
    'vjlast': '1543144728.1547623849.21',
    'vinfo_n_f_l_n3': 'eb1b742a5eb29ab4.1.7.1543144727982.1546409512298.1547624268883',
    '__utma': '94650624.222583246.1545556265.1547693301.1547718854.11',
    'WM_NI': 'wLv0cMOvj6LgaHDLoIPmCeOfqlnS5YQ6ebA4eJrNCHldRALJ9GOKk%2BqUsb83WQd32sW3PxPAZPIjsXiwcMidh656hVOme4rdr1x2nU2UsbJ9ej7O6DQzIddzKKvYwLJkN2M%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6ee88ae45aaacfd8ed1609c928fa3d45e829a9fabee618b8a838dee7288bfa1a5c92af0fea7c3b92ab594bad1e2478daaa6d7cf6da3988cadee4394b38d86ce6eb3b4a2b4b85393eaab83c440a796beafc244b0bc9ea2cf42fb9981acea21b38bbd83bb39958facd4b17995eda099d34b9a90878bf254aba9adaeec70aceafbd7eb5e8db3abd5f170b2efb8d3ed5ff28bbd83c933a7b6f9b0b55093a68785e7728995babaf6488ab582d3d037e2a3',
    'playerid': '16759628',
    'MUSIC_U': 'cac450265aa764fd51cd8bcc601d2ff24a5207bd88bf79d9b0a09341fc45e8083dfbf1c6d69a79c12873d62184f216ac31b299d667364ed3',
    '__csrf': 'cc2c0bd6e78145ae849bc988f817b84c',
    'JSESSIONID-WYYY': '5Xv65SdO74aX3QY%5CD04zG%2BMBU%2BQ5YP%2B%2FQRH%2FCpx5xcmacSrQFdj7ms%5CTGm9iCD2ZXNyUDxdO7Qp7RBlu68wk4B9ml%2Fq6uIRm4PM0b1I%2FlTzd%2BsQThyksUoRgz9%5CAAm%5CKOk0C41IrsVnGoH%2FPWt8m3VnHiOuA7uwmHSD7wsa%5CkR3f4tJt%3A1548409050142',
}


rsp = requests.post(url, headers=headers, data=params)
print(rsp.text)
print(rsp.url)
