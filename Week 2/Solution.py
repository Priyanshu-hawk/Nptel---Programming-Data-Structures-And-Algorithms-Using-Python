def primepartition(m):
    if m<0:
        return False
    pl = prime(m)
    for i in pl:
        chk = m-i
        if chk in pl:
            return True
    else:
        return False


def prime(m):
    eptlst = []
    for i in range(2,m + 1):
        for p in range(2,i):
            if (i % p) == 0:
                break
        else:
            eptlst.append(i)

    return eptlst
  
#######################
  
  
def matched(s):
  cm = 0
  i = 0
  
  while cm >=0 and i<len(s):
    if "(" == s[i]:
      cm += 1
    if ")" == s[i]:
      cm -= 1
    i += 1
    
  if cm == 0:
    return True
  else:
    return False
  
#######################
  
def rotatelist(lst,k):
    l=lst[:]
    if k < 0:
        return l
    for i in range(k):
        onerote(l,len(l))
    return (l)
def onerote(l,n):
    tmp = l[0]
    for i in range(n-1):
        l[i] = l[i+1]
    l[n-1] = tmp

  
