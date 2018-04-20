from cosine.T3 import Similarity
from cosine.VectorCompare import VectorCompare

def dict2list(dic:dict):
    ''' 将字典转化为列表 '''
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val)
    for key, val in
           zip(keys, vals)]
    print(lst)
    return lst

if '__main__' == __name__:
    print('dddddddd')
    dict1={1000: {'101': 1, '102': 1, '103': 0, '104': 0, '105': 0, '106': 0, '109': 0, '107': 0, '108': 0, '2000': 1, '2001': 0, '2002': 0, '2003': 0, '2004': 0},
           1001: {'101': 0, '102': 1, '103': 1, '104': 1, '105': 0, '106': 0, '109': 0, '107': 0, '108': 0, '2000': 0, '2001': 1, '2002': 0, '2003': 0, '2004': 0},
           1002: {'101': 0, '102': 0, '103': 0, '104': 0, '105': 1, '106': 1, '109': 1, '107': 0, '108': 0, '2000': 0, '2001': 0, '2002': 1, '2003': 1, '2004': 0},
           1003: {'101': 0, '102': 0, '103': 0, '104': 0, '105': 0, '106': 0, '109': 1, '107': 1, '108': 1, '2000': 0, '2001': 0, '2002': 0, '2003': 0, '2004': 1},
           1004: {'101': 0, '102': 0, '103': 0, '104': 0, '105': 1, '106': 1, '109': 1, '107': 0, '108': 0, '2000': 0, '2001': 0, '2002': 1, '2003': 1, '2004': 0},
           1005: {'101': 0, '102': 0, '103': 0, '104': 0, '105': 0, '106': 0, '109': 1, '107': 1, '108': 1, '2000': 0, '2001': 0, '2002': 0, '2003': 0, '2004': 1},
           }


    listAll=[]
    for k,v in dict1.items():
        list_group =[]
        for k2, v2 in dict1.items():
            if k != k2:
                # print(k)
                s = Similarity(v.items(), v2.items())
                # print(s.similar())
                if s.similar() > 0:
                    if list_group.count(k) <=0 :
                       list_group.append(k)
                    if list_group.count(k2)<= 0:
                       list_group.append(k2)
        #print('before:',list_group)
        # 排序
        list_group.sort()
        #print('after:', list_group)
        if len(list_group)>0 :
           if (listAll.count(list_group))<=0:
               #print('list,list_group:',list,list_group)
               listAll.append(list_group)
    print(listAll)
    # setAll = set(list)
    # print(setAll)



    # vec = VectorCompare("hello");
    # aa = vec.relation(list1, list2)

    #print(aa)

