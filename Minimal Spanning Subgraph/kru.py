from collections import deque


def Kruskal(sourceFileName, resultsFileName):
        
    with open(sourceFileName, 'r') as f, open(resultsFileName, 'w') as g:
        firstLine = f.readline().strip()
        sz = int(firstLine)
        lists = [[] for i in range(sz)]
        content = [x.strip() for x in f.readlines()]
        i = 0
        for row in content:                 
            lst = row.split(' ')
            l = len(lst)
            j = 0                           
            for c in lst:
               if j != l - 1: 
                   lists[i].append(int(c))
                   j = j + 1
               else:
                   break
            i = i + 1
        
        
        ls = [[] for i in range(sz)]
        wg = [[] for i in range(sz)]
        i = 0
        for x in lists:
            j = 0
            for elem in x:
                if j % 2 == 0:
                    ls[i].append(int(elem))
                    j = j + 1
                else:
                    wg[i].append(int(elem))
                    j = j + 1
            i = i + 1
            
            
        lst = []
        for k in range(sz):
            for m in range(len(ls[k])):
                y = ls[k][m]
                if y > k:
                    wy = wg[k][m]
                    lst.append([wy, k + 1, y])
                else:
                    continue
            
        lst.sort()                      
        
        E = deque()                 #очередь ребер в порядке возрастания весов
        for x in lst:
            E.append(x)
        
        
        name = [i for i in range(sz)] 
        
        ET = []   # список всех ребер в остове T - это будет почти результат
        S = 0
        while len(ET) != sz - 1:
            if E:
                e = E.popleft()
            else:
                break
            s = e[0]
            u = e[1]
            w = e[2]
            p = name[u - 1]
            q = name[w - 1]
            if p != q:
                ET.append([u,w])
                S = S + s
                for i, x in enumerate(name):
                    if x == p:
                        name[i] = q
                        
        T = [[] for i in range(sz)]
        for e in ET:
            a = e[0]
            b = e[1]
            T[a - 1].append(b)
            T[b - 1].append(a)
        for x in T:
            x.sort()
        T.append([S])
        
        for x in T:
            for elem in x:
                g.write(str(elem) + ' ')
            g.write('\n')


print(Kruskal('B:\Python Scripts\(lab2) Minimal Spanning Subgraph\Source.txt', \
              'B:\Python Scripts\(lab2) Minimal Spanning Subgraph\Results.txt'))    