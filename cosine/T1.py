from cosine.VectorCompare import VectorCompare

if '__main__' == __name__:
    print('dddddddd')
    list1={'a':1,'b':0,'c':1,'d':1};
    list2={'a':0,'b':1,'c':1,'d':0};
    print(list1.items())

    vec = VectorCompare("hello");
    aa = vec.relation(list1, list2)

    print(aa)