def DFS(G, GV):
    used = []
    metka=[0]*len(G)
    GV1=GV
    t=1
    while(GV1!=[]):
        #print(GV1)
        steck=[]
        steck.append(GV1[0])
        used.append(GV1[0])
        while(steck!=[]):
            print(steck)
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

n=5
G=[[1,2,4],[0,2,3],[0,1,3,4],[1,2,4],[0,2,3]]
GV=[0,1,2,3,4]
DFS(G,GV)
