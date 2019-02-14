from urllib import request, parse
from http import cookiejar

# 创建cookiejar实例
filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建请求管理器
# build_opener(*handler) 其中handler是Handler的实例，封装不同的请求参数
# opener是OpenerDirector对象,用于操作的函数有open()
opener = request.build_opener(cookie_handler)


def login():
    '''
    负责初次登录
    需要输入用户名密码来获取cookie凭证
    '''

    url = 'http://47.94.145.254:8082/xfz/login/'

    data = {
        'phone': '1234567890',
        'password': '12345678',
    }
    data = parse.urlencode(data)  # 将用户的账号密码格式转换
    # data: 'email=1234567890&password=12345678'
    req = request.Request(url, data=data.encode())

    rsp = opener.open(req)

    cookie.save(ignore_discard=True, ignore_expires=True)


if __name__ == '__main__':
    login()
    print(opener)
    print(cookie)   # 就是cookiejar.CookieJar()实例的值
