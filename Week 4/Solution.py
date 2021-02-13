def rainaverage(l):
    count = {}
    addme = {}
    arr = {}
    for i in l:
        count[i[0]] = 0
        addme[i[0]] = 0
    for j in l:
        count[j[0]]+=1
    for k in l:
        addme[k[0]] += k[1]

    for m in count.keys():
        arr[m] = addme[m]/count[m]
    res = sorted(arr.items())
    return res


############# Solution 2


def flatten(lst):
    res =[]
    for i in lst:
        if listtype(i):
            flatten(i)
        else:
            res.append(i)
    return res

def listtype(trm):
    if (type(trm) == type([])):
        return True
    if (type(trm)==type(())):
        return False
print((["hello",True,3,{'h':'k'}]))
