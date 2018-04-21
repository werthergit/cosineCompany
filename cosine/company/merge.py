def merge(a:list,listAllTemp:set, listIdx:list):
    #print(a)
    list_group = []
    for b in listAllTemp:
        if list(set(a).intersection(set(b))):
           listIdx.append(b)
           #print('a,b',a,b)
           list_group = set(a).union(set(b))
           a = list_group
           print('list_group', list_group)
    print(listIdx)
    # for idx in listIdx:
    #     listAllTemp.pop(idx)
    return list_group

if '__main__' == __name__:
    print('dddddddd')
    listAll =  [{111146458, 274667, 135947607}, {13595834, 655315, 104453189, 330142}, {29338323, 68402029}, {128016063, 90375591}, {54810560, 111146458}]

    listResult = []
    listAllTemp = listAll.copy()
    for listAll_1 in listAll:
        #print('listAllTemp:', listAllTemp)
        listIdx = []
        list_groupmerge = merge(listAll_1, listAllTemp,listIdx)
        print('listIdx:',listIdx)
        if len(list_groupmerge) > 0 :
           listResult.append(list_groupmerge)

           for value1 in listIdx.reverse():
               if listAllTemp.index(value1):
                  listAllTemp.remove(value1)
        else:
           #未匹配上
           listResult.append(listAll_1)

    print('listResult:', listResult)
