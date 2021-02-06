def remdup(l):
    if len(l) == 0:
        return []
    lst_val = l[-1]
    l.reverse()
    ans = []
    for i in l:
        if i in ans:
            pass
        else:
            ans.append(i)
    ans.remove(ans[0])
    ans.reverse()
    ans.append(lst_val)
    return ans

##########################

def splitsum(l):
    poslist = []
    neglist = []
    for i in l:
        if '-' in str(i):
            neglist.append(i)
        else:
            if i != 0:
                poslist.append(i)
    ans = []
    pos = sqr(poslist)
    neg = cub(neglist)
    ans.append(pos)
    ans.append(neg)
    return ans

def sqr(lst):
    ans = 0
    for i in lst:
        ans += (i**2)
    return ans
def cub(lst):
    ans = 0
    for i in lst:
        ans += (i**3)
    return ans

##########################

def matrixflip(myl ,chk):
  l = myl[:]
  if len(l) == 0:
    return myl
  if chk.lower() == 'h':
    return (horflip(l))
  if chk.lower() == 'v':
    return (verflip(l))
  else:
    return l

def horflip(l):
  for i in range(len(l[0])):
    l[i].reverse()
  return l
def verflip(l):
  l.reverse()
  return l

