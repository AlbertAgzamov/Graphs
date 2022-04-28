# Скрипт определяет минимальный поток в сети методом Форда Фалкерсона

from collections import defaultdict

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0
        f = [[0 for i in range(self.ROW)] for i in range(self.ROW)]
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                f[u][v] -= path_flow
                f[v][u] += path_flow
                v = parent[v]
        f1 = [[0 for i in range(self.ROW)] for i in range(self.ROW)]
        for i in range(self.ROW):
            for j in range(self.ROW):
                if f[i][j] < 0:
                    f[i][j] = 0
        for i in range(self.ROW):
            f1[i] = f[i].copy()
        for i in range(self.ROW):
            for j in range(self.ROW):
                f[i][j] = f1[j][i]
        print(self.graph)
        return max_flow, f

file = open("B:\Python Scripts\(lab4) Maximal Network Flow\Source.txt", 'r')
file_lst = []
for row in file:
    file_lst.append(row[:len(row) -1].split(" "))
    row_last = row
file.close()
file_lst.remove([''])
file_lst.append([row_last])
for lst in file_lst:
    for i in range(len(lst)):
        lst[i] = int(lst[i])

N = file_lst[0][0]
source = file_lst[-2][0] - 1

sink = file_lst[-1][0] - 1

graph = file_lst[1:-2]

g = Graph(graph)
answer = g.FordFulkerson(source, sink)
file = open("B:\Python Scripts\(lab4) Maximal Network Flow/Results.txt", 'w')
for line in answer[1]:
    str_line = [str(elem) for elem in line]
    for col in str_line:
        file.write(col + ' ')
    file.write('\n')
file.write(str(answer[0]))
file.close()
