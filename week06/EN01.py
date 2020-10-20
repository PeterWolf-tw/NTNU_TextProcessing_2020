#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def sentence2LIST_v1(inputSTR):
    for item in (". ", ", "):
        inputSTR = inputSTR.replace(item, "{}{}".format(item,"<My_Cutting_Mark>"))
    resultLIST = inputSTR.split("<My_Cutting_Mark>")
    return resultLIST


def sentence2LIST_v2(inputSTR):
    cuttingMarkTUPLE = (". ", ", ")
    for index in range(0, len(cuttingMarkTUPLE)):
        inputSTR = inputSTR.replace(cuttingMarkTUPLE[index], "{}{}".format(cuttingMarkTUPLE[index],"<My_Cutting_Mark>"))
    resultLIST = inputSTR.split("<My_Cutting_Mark>")
    return resultLIST




if __name__== "__main__":
    inputSTR = "Application security is hard...when it’s a separate process. With GitLab, application security testing is built into the CI/CD process. Every merge request is scanned for vulnerabilities in your code and that of its dependencies."
    resultLIST = sentence2LIST_v1(inputSTR)
    print(resultLIST)