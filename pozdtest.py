G=[]
GV=[]
n=int(input())
for i in range (0, n):
    ent_list = input().split()
    num_list = list(map(int, ent_list))
    G.append(num_list)

for i in range (0, n):
    GV.append(i)

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
CS=[]
def DFS(G, GV):
    i=0
    while (GV != []):
        T=[]
        i+=1
        stack = []
        stack.append(GV[0])
        GV.remove(GV[0])
        while (stack != []):
            k=stack[len(stack)-1]
            for m in G[k]:
                if m in GV:
                    stack.append(m)
                    GV.remove(m)
            stack.remove(k)
    return i
G1=COPY(G,n)
GV1=COPY_1(GV,n)
k=DFS(G1,GV1)
gg=0
for i in range(0,n):
    for m in G[i]:
        if(m!= -1):
            G1=COPY(G,n)
            GV1=COPY_1(GV,n)
            G1[i].remove(m)
            G1[m].remove(i)
            if DFS(G1,GV1)!=k:
                gg+=1
print (int(gg/2))


