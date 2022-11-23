def DFS(G, GV, metka, n):
    #GVm=COPY_1(GV,n)
    GVm=[]
    for i in range(0,n):
        GVm.append(i)
    i=1
    while(GVm!=[]):
        steck=[]
        steck.append(GVm[0])
        GVm.pop(0)
        while (steck!=[]):
            #print(steck)
            v=steck[len(steck)-1]
            for m in G[v]:
                k=0
                if (m in GVm):
                    steck.append(m)
                    GVm.remove(m)
                    k=1
                    break
            if(k==0):
                TT=steck.pop()
                metka[TT] = i
                i += 1

def COPY(F, n):
    G1=[]
    for i in range(0,n):
        G1.append([])
    for i in range(0, n):
        for m in F[i]:
            G1[i].append(m)
    return G1
def COPY_1(F, n):
    GV=[]
    for i in range(0,n):
        GV.append(F[i])
    return GV
#metka=[]
#n = 7
#GV = [0,1,2,3,4,5,6]
#G = [[1,6],[3],[-1],[5],[-1],[1],[5]]
#mark=[]

G=[]
GV=[]
metka=[]
mark=[]
n=int(input())
for i in range (0, n):
    ent_list = input().split()
    num_list = list(map(int, ent_list))
    G.append(num_list)

for i in range (0, n):
    GV.append(i)
    mark.append(0)

dele=[]
for i in range(0,len(G)):
    if (-1 in G[i]):
        dele.append(i)
ud=0
for i in range(0, len(G)):
    if (-1 in G[i]):
        G[i]=[]
        n-=1
        ud+=1
G1=[]
for i in range(0, len(G)):
    if(G[i]!=[]):
        G1.append(G[i])
G=G1
GV=[]

for p in dele:
    for i in range(0,len(G)):
        for j in range(0, len(G[i])):
            if (G[i][j]>=p):
                G[i][j]-=1

for i in range(0, 5):
    metka.append(0)
    mark.append(0)
    GV.append(i)

DFS(G,GV,metka, n)
def INVERT(G, n):
    G1 = []
    for i in range(0, n):
        G1.append([])
    for i in range(0,n):
        for m in G[i]:
            G1[m].append(i)
    return G1
G2= INVERT(G,n)

def DFSK(G2, v, color, mark):
    used = []
    steck = []
    steck.append(v)
    used.append(v)
    while (steck != []):
        v = steck[len(steck) - 1]
        k=0
        for m in G2[v]:
            k = 0
            if (m not in used):
                steck.append(m)
                used.append(m)
                k = 1
                break
        if (k == 0):
            t=steck.pop()
            if (mark[t]==0):
                mark[t] = color



for i in range(0, n):
    if (0 in mark):
        if(G[metka.index(max(metka))] != []):
            DFSK(G2,metka.index(max(metka)),i+1,mark)
            metka[metka.index(max(metka))]=-1
print(max(mark)+ud)