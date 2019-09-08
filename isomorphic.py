s1,s2 = input().split()
if(len(s1)==len(s2)):
    d1=[]
    d2=[]
    def dups(s):
        d=[]
        r=[]
        for i in s:
            if i not in d:
                d.append(i)
            else:
                if i not in r:
                    r.append(i)
        return r
    r1=dups(s1)
    r2=dups(s2)
    if len(r1)==len(r2):
        def rep(r1,s1):
            p=[]
            for i in r1:
                ip=[]
                count=-1
                for j in s1:
                    count=count+1
                    if i==j:
                        ip.append(count)
                p.append(ip)
                return p
        p1=rep(r1,s1)
        p2=rep(r2,s2)

        if(p1==p2):
            print('yes')
        else:
            print('no')
    else:
        print('yes')
else:
    print('no')
