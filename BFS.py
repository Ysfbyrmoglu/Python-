
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : [],
}

gidilen = []
sıra = []   

def bfs(gidilen, graph, dügüm): 
  gidilen.append(dügüm)
  sıra.append(dügüm)

  while sıra:          
    m = sıra.pop(0) 
    print (m, end = " ") 

    for komşu in graph[m]:
      if komşu not in gidilen:
        gidilen.append(komşu)
        sıra.append(komşu)
# Driver Code
print("geniş öncelikle aramanın izlediği yol ")
bfs(gidilen, graph, '5')    