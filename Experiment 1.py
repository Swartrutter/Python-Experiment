# -*- coding: utf-8 -*-
# @Time : 2021/9/17 13:09
# @Author : Swartrutter
# @Email : dai2411848759@163.com
# @File : Experiment 1.py
# @Project : pythonProject


# 实验要求：输入某一个功能编号，能实现以下几点功能（功能可根据自己的理解进行实现）:
# 1､新增实验室预约(学号、姓名、所预约的时间、目标实验室等信息)；注意信息字段根据个人理解进行设计。
# 2､显示目前全部的预约信息；
# 3､查询预约情况；
# 4､修改预约信息。
# 5､退出系统。


import time
import datetime


def contents():  # 第一个方法，显示预约菜单
    print("==========欢迎使用Swartrutter开放实验室简单预约系统==========")
    print("功能1————新增实验室预约(学号、姓名、所预约的时间、目标实验室等信息)")
    print("功能2————显示目前全部的预约信息")
    print("功能3————查询预约情况")
    print("功能4————修改预约信息")
    print("功能5————退出系统")


RoomList = []  # 定义一个实验室列表存放数据


def add():  # 第二个方法，新增实验室预约
    stuN = input("请输入您的学号：")
    Name = input("请输入您的姓名：")
    Time = input("请输入您要预约的时间：格式为mm-dd，如：09-17")
    # t = time.strftime(Time , "%m-%d")
    # m,d = t[0:2]
    # print("您预约的时间为：" + datetime.datetime(m,d))
    Room = input("请输入您要预约的实验室：格式为XXX，如：105")
    dict = {'学号': stuN, '姓名': Name, '预约的时间': Time, '预约的实验室': Room}  # 更新字典
    RoomList.append(dict)  # 将更新好的字典加入到实验室列表中


def show():  # 第三个方法，显示全部的预约信息
    print("以下是已有的所有预约信息：")
    for i in RoomList:
        print(i)


def query():  # 第四个方法，通过学号查询预约的信息
    num = input("请输入您的学号，以此查询您的预约信息：")
    for i in RoomList:
        if num == i['学号']:
            print(i)
            break
        else:
            print("系统查询不到您有预约信息，请输入1前去预约！")


def modify():  # 第五个方法，通过学号查询并修改自己的预约信息
    num = input("请输入您的学号，以此修改您的预约信息：")
    for i in RoomList:
        if num == i['学号']:
            print("您好！" + i['姓名'] + "请输入更新的预约时间与预约实验室：")
            tt = input("更新的预约时间：")
            i['预约的时间'] = tt
            rr = input("更新的预约实验室")
            i['预约的实验室'] = rr


while 'true':  # 使用while循环，true代表无限循环
    contents()
    i = input("输入数字1-5，实现某种功能：")
    if i == '1':
        add()
    elif i == '2':
        show()
    elif i == '3':
        query()
    elif i == '4':
        modify()
    elif i == '5':
        flag = input("您是否确实要退出本预约系统？确认请输入Y，否则输入N:")  # 设置flag标志确认退出系统
        if flag == 'Y':
            break
    else:
        print("输入的数字有误，请重新输入！")
