# -*- coding: utf-8 -*-
# !/usr/bin/python3
import datetime

import pymysql

#
#已经匹配的，不在进行相关度比较

#select COMPANY_NAME,LEGAL_PERSON_NAME from company_180415 where id in (330142, 655315, 13595834, 104453189);

def dict2list(k,v,dic:dict):
    list_group =[]
    for k2, v2 in dic.items():
        #print('k,k2',k,k2)
        if k!=k2 :
            s = Similarity(v.items(), v2.items())
            if s.similar() > 0:
                list_group.append(k)
                list_group.append(k2)
    #print('list_group',list_group)
    return list_group


if '__main__' == __name__:
    now1 = datetime.datetime.now()

    # 打开数据库连接
    #db = pymysql.connect("localhost", "root", "root", "company_distinct")
    from cosine.T3 import Similarity

    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root',db='company_namegroup',charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    now2 = datetime.datetime.now()
    print("mysql连接:",now2 - now1)

    # SQL 查询语句
    sql = "SELECT ID,COMPANY_NAME,LEGAL_PERSON_ID,LEGAL_PERSON_NAME FROM company_180415 \
           WHERE LEGAL_PERSON_ID = %d "

    sql2 = "SELECT ID,COMPANY_ID,COMPANY_NAME,H_ID, H_NAME FROM company_person_180415 \
           WHERE company_id = %d and h_id <> %d "

    sql3 = "SELECT ID,COMPANY_ID,COMPANY_NAME,C_ID,C_NAME FROM company_company_180415 \
           WHERE company_id = %d "



    try:
        #用户id
        parameterHid = 182732
        #阈值
        similarThreshold = 0
        # 执行SQL语句
        cursor.execute(sql % (parameterHid))
        # 获取所有记录列表
        results = cursor.fetchall()
        list = []
        dictAll = {}
        dictAllTemp1 = {}
        dictAllTemp2 = {}
        for row in results:
            cid = row[0]
            # 打印结果
            # print("cid=%s,cname=%s,hid=%s,hname=%s " % \
            #       (cid, cname, hid, hname))
            list.append(cid)
        #print('list:',list)

        now2 = datetime.datetime.now()
        print(now2 - now1)

        # 定义字典
        dict1 = {}
        for cid in list:
            # 执行SQL语句
            #print(sql2 % (cid,parameterHid))
            cursor.execute(sql2 % (cid, parameterHid))
            # 获取所有记录列表
            results = cursor.fetchall()
            dict_1 = {}
            for row2 in results:
                hid2 = row2[3]
                hname2 = row2[4]
                # print("hid2=%s, hname2=%s " % \
                #       (hid2, hname2) )
                dict_1.setdefault(str(hid2),1)
                dict1.setdefault(str(hid2), 0)
                dictAll.setdefault(cid, dict1)
                dictAllTemp1.setdefault(cid, dict_1)


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
        #print('dictAll ', dictAll)
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

        #分组
        listAll = []
        dictTemp = dictAll.copy();
        for k, v in dictAll.items():
            list_group = []
            list_group = dict2list(k, v, dictTemp)
            #print('list_group:',list_group)
            if len(list_group) > 0:
                for listkey in set(list_group) :
                    # print('list_key',listkey)
                    # print('dictTemp', dictTemp)
                    if len(dictTemp) > 0:
                        if dictTemp.get(listkey):
                           #print('listkey:',listkey)
                           dictTemp.pop(listkey)
                # print('dictTemp:',dictTemp)
                if listAll.count(set(list_group))<=0:
                   listAll.append(set(list_group))
        print('listAll:',listAll)


    except Exception  as err:
        print("Error: unable to fetch data"+err)

    # 关闭数据库连接
    db.close()

    now2 = datetime.datetime.now()
    print(now2-now1)