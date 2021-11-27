def main():
    with open('B:\Python Scripts\(lab3) Way In Net\Source.txt', 'r') as f, \
         open('B:\Python Scripts\(lab3) Way In Net\Results.txt', 'w') as g:
        lists, s, t = unpackingFile(f)
        print(lists, s, t, sep='\n')
        sz = len(lists)
        Inf = float('inf')
        matr = helper(lists)
        print('Matrice =', matr)
        D, Previous = FordBellman(matr, s - 1, t - 1) 
        print('D =', D)
        print('Previous =', Previous)
        weight, path = buildPath(D, Previous, matr, s - 1, t - 1)
        print('weight =', weight)
        print('path =', path)
        writeToFile(weight, path, g)
            

def FordBellman(matr, s, t):
    sz = len(matr)
    D = [1 for i in range(sz)]
    Previous = [1 for i in range(sz)]
    for v in range(sz):
        D[v] = matr[s][v]
        Previous[v] = s
    for k in range(sz - 2):
        for v in range(sz):
            if v == s: continue
            for w in range(sz):
               d = D[w] + matr[w][v]
               if d < D[v]:
                   D[v] = d
                   Previous[v] = w
    return D, Previous
   
def buildPath(D, Previous, matr, s, t):
    if D[t] < float('inf'):
       weight = 0
       path = []
       v = t
       path.append(t + 1)
       while Previous[v] != 0:
           weight += matr[Previous[v]][v]
           path.append(Previous[v] + 1)
           v = Previous[v]
       path.append(s + 1)
       weight += matr[Previous[v]][v]
       return - weight, path
    else:
       return float('inf'), 'Not exists!'
        
    

   
def helper(lists):  #Переводит список списков предыдущих вершин (с весами)
                         # в матрицу весов. Знаки весов меняются на противоположные
    sz = len(lists)
    matr = [[0 for j in range(sz)] for i in range(sz)]
    for i in range(sz):
         if lists[i] == []:
             for j in range(sz):
                 matr[j][i] = float('inf')
         else:
             nums = []
             for index, item in enumerate(lists[i]):
                 if index % 2 == 0:
                     matr[item - 1][i] = - lists[i][index + 1]
                     nums.append(item)
                 else:
                     continue
             for j in range(sz):
                 if j + 1 in nums:
                     continue
                 else: 
                     matr[j][i] = float('inf')
    return matr
    
    
    
def unpackingFile(file):
    firstLine = file.readline().strip()
    sz = int(firstLine)
    lines = file.readlines()
    x = int(lines[-2])
    y = int(lines[-1])
    lines = [[] if (x == '0') \
             else  [int(z) for z in x.strip()[:-2].split()] \
             for x in lines[:sz]]
    return lines, x, y


def writeToFile(weight, path, file):
    if weight == float('inf'):
        file.write('N')
    else:
        file.write(str(weight) + '\n')
        path.reverse()
        for v in path:
            file.write(str(v) + ' ')
        
     
main()