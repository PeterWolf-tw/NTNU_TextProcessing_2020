#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def 旁邊休息(體溫):
    體溫 = 體溫 - 0.5
    return 體溫


def 量體溫(體溫):
    if 體溫 > 37:
        print("啊！{}度，好危險！".format(體溫))
        體溫 = 旁邊休息(體溫)
        量體溫(體溫)
        return "降溫了…算安全吧！"
    else:
        return "安全！"

if __name__ == "__main__":
    我的體溫 = 40
    結果 = 量體溫(我的體溫)
    print(結果)
