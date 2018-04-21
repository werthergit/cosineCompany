def merge(a:list,listAllTemp:list):
    #print(a)
    list_group = []
    listIdx=[]
    for b in listAllTemp:
        if list(set(a).intersection(set(b))):
           listIdx.append(listAllTemp.index(b))
           #print('a,b',a,b)
           list_group = set(a).union(set(b))
           a = list_group
           print('list_group', list_group)
    print(listIdx)
    for idx in listIdx:
        listAllTemp.pop(idx)
    return list_group

if '__main__' == __name__:
    print('dddddddd')
    listAll = [{111146458, 274667, 135947607}, {104453189, 13595834, 655315, 111146458, 330142}, {29338323, 68402029}, {128016063, 90375591}, {54810560, 104453189, 13595834, 274667, 655315, 135947607, 111146458, 330142}, {54810560, 111146458, 274667, 135947607}, {54810560, 111146458, 135947607}]

    listResult = []
    listAllTemp = listAll.copy()
    idx=0



    for listAll_1 in listAll:
        #print('listAllTemp:', listAllTemp)
        listAllTemp.pop(idx)
        list_groupmerge = merge(listAll_1, listAllTemp)
        if len(list_groupmerge) > 0 :
           listResult.append(list_groupmerge)
        else:
           #未匹配上
           listResult.append(listAll_1)

    print('listResult:', listResult)
