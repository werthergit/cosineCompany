# -*- coding: utf-8 -*-
# !/usr/bin/python3
import datetime

import pymysql

now1 = datetime.datetime.now()

# 打开数据库连接
#db = pymysql.connect("localhost", "root", "root", "company_distinct")
from cosine.T3 import Similarity

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root',db='company_distinct',charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

now2 = datetime.datetime.now()
print("mysql连接:",now2 - now1)

# SQL 查询语句
sql = "SELECT * FROM company \
       WHERE LEGAL_PERSON_ID = %d "

sql2 = "SELECT * FROM company_person \
       WHERE company_id = %d "

sql3 = "SELECT * FROM company_company \
       WHERE company_id = %d "



try:
    # 执行SQL语句
    cursor.execute(sql % (100))
    # 获取所有记录列表
    results = cursor.fetchall()
    list = []
    dictAll = {}
    dictAllTemp1 = {}
    dictAllTemp2 = {}
    for row in results:
        cid = row[0]
        cname = row[1]
        hid = row[2]
        hname = row[3]
        # 打印结果
        # print("cid=%s,cname=%s,hid=%s,hname=%s " % \
        #       (cid, cname, hid, hname))
        list.append(cid)
    print('list:',list)

    now2 = datetime.datetime.now()
    print(now2 - now1)

    # 定义字典
    dict1 = {}
    for cid in list:
        # 执行SQL语句
        # print(sql2 % cid)
        cursor.execute(sql2 % cid)
        # 获取所有记录列表
        results = cursor.fetchall()
        dict_1 = {}
        for row2 in results:
            hid2 = row2[3]
            hname2 = row2[4]
            # print("hid2=%s, hname2=%s " % \
            #       (hid2, hname2))
            dict_1.setdefault(str(hid2),1)
            dict1.setdefault(str(hid2), 0)
            dictAll.setdefault(cid, dict1)
            dictAllTemp1.setdefault(cid, dict_1)
    # print('dictAll ', dictAll)
    # print('dictAllTemp ', dictAllTemp1)
    # for (k, v) in dictAll.items():
    #     dictAll[k] = dictAll[k].copy()
    # print('dictAll ', dictAll)
    # for (k, v) in dictAllTemp1.items():
    #     for (k1, v1) in v.items():
    #        print("k,k1",k,k1,v[k1])
    #        dictAll[k][k1] = 1
    # print('dictAll ', dictAll)




    for cid in list:
        # 执行SQL语句
        # print(sql3 % cid)
        cursor.execute(sql3 % cid)
        # 获取所有记录列表
        results = cursor.fetchall()
        dict_2 = {}
        for row3 in results:
            cid3 = row3[3]
            cname3 = row3[4]
            # print("cid=%s, cname=%s " % \
            #       (cid3, cname3))
            dict_2.setdefault(str(cid3), 1)
            dict1.setdefault(str(cid3), 0)
            dictAll.setdefault(cid, dict1)
            dictAllTemp2.setdefault(cid, dict_2)
    # print('dictAll ', dictAll)
    # print('dictAllTemp2 ', dictAllTemp2)
    for (k, v) in dictAll.items():
        dictAll[k] = dictAll[k].copy()
    print('dictAll ', dictAll)
    for (k, v) in dictAllTemp1.items():
        for (k1, v1) in v.items():
               # print("k,k1",k,k1,v[k1])
               dictAll[k][k1] = 1
    print('dictAll 同公司相关姓名设置为1 ', dictAll)
    for (k, v) in dictAllTemp2.items():
        for (k1, v1) in v.items():
           # print("k,k1",k,k1,v[k1])
           dictAll[k][k1] = 1
    print('dictAll 同公司相关企业设置为1 ', dictAll)

    list_all = []
    list_abc = []
    #比较相似度
    for (k, v) in dictAll.items():
        t1 = v.items();
        list_sim = []
        for (k1, v1) in dictAll.items():
            if k != k1 :
                print("k,k1",k,k1)
                #print("v,v1", v, v1)
                s = Similarity(v.items(), v1.items())
                print(s.similar())
                if s.similar() > 0:
                    if list_abc.count(k)<=0 :
                       list_sim.append(k)
                       list_abc.append(k)
                    if list_abc.count(k1)<=0 :
                       list_sim.append(k1)
                       list_abc.append(k1)
                    #print("k,k1", k, k1,s.similar())
                    #todo 分组
                    if len(list_sim)>0:
                       list_all.append(list_sim)
    print(list_all)
    for listTemp in list_all:
        print(listTemp, len(listTemp))
except Exception  as err:
    print("Error: unable to fetch data"+err)

# 关闭数据库连接
db.close()

now2 = datetime.datetime.now()
print(now2-now1)