import time
def co(q, c, w, com):
    for i in range(len(com)):
        if c==com[i]:
            if i==0:
                return de(q,w)
            elif i==1:
                return um(q,w)
            elif i==2:
                return mi(q,w)
            elif i==3:
                return pl(q,w)
            elif i==4:
                return st(q,w)
def pl(q,w):
    return q+w
def mi(q,w):
    return q-w
def um(q,w):
    return q*w;
def de(q,w):
    return q/w
def st(q,w):
    return q**w
def schet(a):
    for i in range(len(a)):
        if a[i] in com:
            f=0
            q=''
            w=''
            while a[f] in nums and f<i:
                q=q+a[f]
                f+=1
            f=i+1
            while f<=len(a)-1 and a[f] in nums and f>i:
                    w=w+a[f]
                    f+=1
            return co(int(q), a[i], int(w), com)
nums=[]
for i in range(0, 10):
    nums.append(str(i))
com=['/', '*', '-', '+', '^']
a=input()
print(schet(a))
time.sleep(3)