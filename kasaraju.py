def DFS(G, GV):
    used = []
    metka=[0]*len(G)
    GV1=COPY_1(GV,len(G))
    t=1
    while(GV1!=[]):
        #print(GV1)
        steck=[]
        steck.append(GV1[0])
        used.append(GV1[0])
        while(steck!=[]):
            #print(steck)
            v=steck[-1]
            k=0
            for i in G[v]:
                if (i not in used):
                    used.append(i)
                    steck.append(i)
                    k=1
                    break
            if (k==0):
                metka[steck.pop()]=t
                t+=1
        for m in used:
            if (m in GV1):
                GV1.remove(m)
    return metka

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
#n = 8
#GV = [0,1,2,3,4,5,6,7]
#замена вершины без выходов на пустой массив
#G = [[1,6],[],[1],[2,5],[3],[4],[1,2,7],[0]]

#n=5
#GV=[0,1,2,3,4]
#G=[[1,4],[2],[3],[1],[3]]

#n = 4
#GV=[0,1,2,3]
#G=[[1],[2],[0],[2]]
mark=[]
#начало ввода с клавиатуры
G=[]
GV=[]
metka=[]
mark=[]
n=int(input())
for i in range (0, n):
    ent_list = input().split()
    num_list = list(map(int, ent_list))
    G.append(num_list)

for i in range(0, n):
    if (-1 in G[i]):
        G[i]=[]
#конец ввода с клавиатуры
for i in range(0, n):
    mark.append(0)
GV=[]
n = len(G)
used=[]
#DFS(G,3,used)
for i in range(0, len(G)):
    GV.append(i)
t=0
metka=[]
metka=DFS(G,GV)


#print(metka)
#print(G)
def INVERT(G):
    n=len(G)
    G1 = []
    for i in range(0, n):
        G1.append([])
    for i in range(0,n):
        #print(i)
        if(G[i]!=[]):
            for m in G[i]:
                if (m!=-1):
                    G1[m].append(i)
    return G1
#print(G)
G2= INVERT(G)
#print(G2)
#for i in range(len(G2)):
#    if (G2[i]==[]):
#        G2[i].append(-1)
#print(G2)

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
    #return mark

#print(DFSK(G2,0,1))
#DFSK(G2,2,1,mark)
#print(mark)
#DFSK(G2,3,2,mark)
#print(mark)
#DFSK(G2,0,3,mark)
#print(mark)
#DFSK(G2,1,4,mark)
#print(mark)

for i in range(0, n):
    #print(mark)
    DFSK(G2,metka.index(max(metka)),i+1,mark)
    metka[metka.index(max(metka))]=-1
#print(mark)
print(len(set(mark)))