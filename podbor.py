class Node:
    def __init__(self ,key):
        self.data = key
        self.left = None
        self.right = None

    def BFS(root):
        n = len(G)  # узнаем количество вершин
        used = [False] * n  # инициализируем список, в котором хранится состояние каждой вершины
        Q = []  # инициализируем очередь
        Qstart = 0  # индекс первого элемента очереди
        Q.append(s)  # добавляем в очередь стартовую вершину
        used[s] = True  # и помечаем её, как просмотренную

        while (Qstart < len(Q)):
            v = Q[Qstart]  # выбираем первую в очереди вершину
            Qstart += 1  # удаляем её
            # проходимся по всем смежным вершинам от текущей, добавляем в очередь  помечаем, как просмотренные
            for i in G[v]:
                if (used[i] == False):
                    Q.append(i)
                    used[i] = True