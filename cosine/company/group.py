from cosine.T3 import Similarity




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
    print('dddddddd')
    dict1={1000: {'101': 1, '102': 1, '103': 0, '104': 0, '105': 0, '106': 0, '109': 0, '107': 0, '108': 0, '2000': 1, '2001': 0, '2002': 0, '2003': 0, '2004': 0},
           1001: {'101': 0, '102': 1, '103': 1, '104': 1, '105': 0, '106': 0, '109': 0, '107': 0, '108': 0, '2000': 0, '2001': 1, '2002': 0, '2003': 0, '2004': 0},
           1002: {'101': 0, '102': 0, '103': 0, '104': 0, '105': 1, '106': 1, '109': 1, '107': 0, '108': 0, '2000': 0, '2001': 0, '2002': 1, '2003': 1, '2004': 0},
           1003: {'101': 0, '102': 0, '103': 0, '104': 0, '105': 0, '106': 0, '109': 1, '107': 1, '108': 1, '2000': 0, '2001': 0, '2002': 0, '2003': 0, '2004': 1},
           1004: {'101': 0, '102': 0, '103': 0, '104': 0, '105': 1, '106': 1, '109': 1, '107': 0, '108': 0, '2000': 0, '2001': 0, '2002': 1, '2003': 1, '2004': 0},
           1005: {'101': 0, '102': 0, '103': 0, '104': 0, '105': 0, '106': 0, '109': 1, '107': 1, '108': 1, '2000': 0, '2001': 0, '2002': 0, '2003': 0, '2004': 1},
           }


    listAll=[]
    dictTemp = dict1.copy();
    for k ,v in dict1.items():
        #print('k:',k)
        list_group = []
        list_group = dict2list(k,v, dictTemp)
        if len(list_group)>0 :
            for listkey in set(list_group):
                print('list_key',listkey)
                print('dictTemp', dictTemp)
                if len(dictTemp)>0:
                   dictTemp.pop(listkey)
            #print('dictTemp:',dictTemp)
            #list_group = dict2list(k)
            listAll.append(list_group)
    print(listAll)
    # setAll = set(list)
    # print(setAll)



    # vec = VectorCompare("hello");
    # aa = vec.relation(list1, list2)

    #print(aa)

