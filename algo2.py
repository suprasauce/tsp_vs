import pygame as py, colors, main as m

mini= 1000000009
minimumpath=[]

# globals
city_states = {}
cities = {}
costmatrix = []
edges = []

def init_globals(x, y, z):
    global city_states
    global cities
    global costmatrix
    city_states = x
    cities = y
    costmatrix = z
    for i in range(len(costmatrix)):
        edges.append([0 for x in range(len(costmatrix))])


def findpath(current,visited,cost,path,n):
    global mini
    global minimumpath
    visited[current]=True
    city_states[current] = colors.GREEN
    #m.update_screen(cities, city_states, 1, edges)
    flag=1
    for i in range(n):
        if visited[i]==False:
            edges[current][i] = 1
            m.update_screen(cities, city_states, 1, edges)
            flag=0
            path.append(i)
            findpath(i,visited,cost+costmatrix[current][i],path,n)
            edges[current][i] = 0
            m.update_screen(cities, city_states, 1, edges)
            path.pop()
    if flag==1:
        edges[0][current] = 1
        m.update_screen(cities, city_states, 1, edges)
        cost+=costmatrix[current][0]
        if cost<mini:
            mini=cost
            minimumpath=path[:]
        edges[0][current] = 0
        m.update_screen(cities, city_states, 1, edges)
    visited[current]=False
    city_states[current] = colors.RED





# def main():
#     global mini
#     global minimumpath
   
#     n=4
#     visited=[False for i in range(n)]
#     costmatrix=[[ 0, 10, 15, 20 ],
#                        [ 10, 0, 35, 25 ],
#                        [ 15, 35, 0, 30 ],
#                        [ 20, 25, 30, 0 ]]
#     path=[0]
#     findpath(0,visited,costmatrix,0,path,n)
#     print(mini)
#     print(minimumpath)



# if __name__ == "__main__":
#     main()