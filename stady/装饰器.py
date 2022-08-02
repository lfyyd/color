# # 定义一个装饰器
# def decorate(func):
#     a = 100
#     print('wrapper外层打印测试')
#     def wrapper():
#         func()
#         print('刷漆')
#         print('铺地板')
#         print('装门')
#     print('wrapper加载完成')
#     return wrapper
#
# # 使用装饰器
# @decorate
# def house():
#     print('我是毛坯房')
#
# house()


# 登录校验
# from time import sleep
#
#
# def decorate(func):
#     def wrapper(*x):
#         print('正在校验中')
#         sleep(2)
#         print('校验完成')
#         # 调用原函数
#         func(*x)  # f1 f2 f3
#
#     return wrapper
#
#
# @decorate
# def f1(n):
#     print('f1', n)
#
#
# f1(5)
#
#
# @decorate
# def f2(name):
#     print('f2', name)
#
#
# #
# #
# f2('lili')
#
#
# #
# #
# @decorate
# def f3(lst):
#     for ls in lst:
#         print(ls)
#
#
# lst = [1, 2, 3, 4]
# f3(lst)

import time


def auth_user(func):
    def auth_count(**kwargs):
        username = kwargs["username"]
        password = kwargs["password"]
        if username == "lucy" and password == "12345":
            return {"code": 200, "data": func(username), "msg": "login succ"}
        else:
            return {"code": 403, "msg": "login fail"}

    return auth_count


@auth_user
def get_info(username="", password=""):
    return {"username": username, "login_time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}


if __name__ == '__main__':
    # 正常用例
    print(get_info(username="lucy", password="12345"))
#
    # 错误用例
    print(get_info(username="lucy", password="dfs"))

