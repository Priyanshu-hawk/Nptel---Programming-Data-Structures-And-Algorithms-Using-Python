def ldSet(arr, n):
     
    divset = [0 for i in range(n)]
     
    divset[0] = 1

    for i in range(n):
        divset[i] = 1
        for j in range(i):
            if (divset[j] != 0 and arr[i] % arr[j] == 0):
                divset[i] = max(divset[i], divset[j] + 1)
 
    return max(divset)
#ar = [14,2,11,16,12,36,60,71,17,29,144,288,129,432,993]
#ar = [9,2,3,7,8,14,39,145,76,320]

ar = []
inp = int(input())
ar.append(inp)
i = 0
while i < inp:
    ar.append(int(input()))
    i+=1
print(ldSet(ar, len(ar)))
