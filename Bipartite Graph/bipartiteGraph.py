
def bipartiteGraph(sourceFileName, resultsFileName):


    #------------------------------------------------------------------------
    
    def dfs(node):
        for u in range(sz):
            if len(visited) == sz and u == sz - 1:
                return True      
            elif matrix[node][u] == 0:
                if u == sz - 1:
                    return dfs(fathers[node])
                else:
                    continue 
            elif matrix[node][u] == 1:
                if u not in visited:
                    visited.append(u)
                    color[u] = 1 - color[node]
                    fathers.update({u : node})
                    return dfs(u)
                elif u in visited:
                    if color[u] == color[node]:
                        return False
                    else:
                        if u == sz - 1:
                            return dfs(fathers[node])
                        else:
                            continue
            else:
                return dfs(fathers[node])
    
    
    
    #------------------------------------------------------------------------   
    
    
    def write_func_if_yes(lst1,lst2):
        redsToStr = ' '.join([str(elem) for elem in [x + 1 for x in lst1]])
        greensToStr = ' '.join([str(elem) for elem in [x + 1 for x in lst2]])
        r.write('Y\n')
        r.write(redsToStr+'\n')
        r.write(greensToStr+'\n')
    
        
    #------------------------------------------------------------------------                
                
    with open(sourceFileName, 'r') as f, open(resultsFileName, 'w') as r:
    
        firstLine = f.readline().strip()
        sz = int(firstLine)
        matrix = [[0 for j in range(sz)] for i in range(sz)]  


        
        content = [x.strip() for x in f.readlines()]
        i = 0
        for row in content:                 
            lst = row.split(' ')             
            j = 0                           
            for c in lst:                   
                matrix[i][j] = int(c)       
                j = j + 1                   
            i = i + 1                       
        print(matrix)
   

        
        visited = []
        
        color = [-1] * sz
        
        color[0] = 1
        
        visited.append(0)
        
        fathers = dict()
        
        
        if not dfs(0):
            r.write('N')
        else:
            red = []
            green = []
            for i in range(sz):
                if color[i] == 1:
                    red.append(i)
                else:
                    green.append(i)
            if red[0] <= green[0]:
                write_func_if_yes(red, green)
            else:
                write_func_if_yes(green, red)
      
        
 #------------------------------------------------------------------------
  
bipartiteGraph('B:\Python Scripts\(lab1) Bipartite Graph\Source.txt', \
                'B:\Python Scripts\(lab1) Bipartite Graph\Results.txt')
         
         
         
         
         
         
         
         
         
         
         
         