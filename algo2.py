import pygame as py, colors, main as m

mini= 1000000009
minimumpath=[]

# globals
city_states = {}
cities = {}
adj = []
edges = []


def init_globals(x, y, z):
    global city_states
    global cities
    global adj
    city_states = x
    cities = y
    adj = z


def findpath(current,visited,costmatrix,cost,path,n):
    global mini
    global minimumpath
    visited[current]=True
    city_states[current] = colors.LIGHT_PURPLE
    m.update_screen(cities, city_states,1)
    city_states[current] = colors.GREEN
    m.update_screen(cities, city_states, 1)
    flag=1
    for i in range(n):
        if visited[i]==False:
            flag=0
            path.append(i)
            findpath(i,visited,costmatrix,cost+costmatrix[current][i],path,n)
            path.pop()
    if flag==1:
        cost+=costmatrix[current][0]
        if cost<mini:
            mini=cost
            minimumpath=path[:]
    visited[current]=False
    city_states[current] = colors.RED
    m.update_screen(cities, city_states, 1)






def main():
    global mini
    global minimumpath
   
    n=4
    visited=[False for i in range(n)]
    costmatrix=[[ 0, 10, 15, 20 ],
                       [ 10, 0, 35, 25 ],
                       [ 15, 35, 0, 30 ],
                       [ 20, 25, 30, 0 ]]
    path=[0]
    findpath(0,visited,costmatrix,0,path,n)
    



# if __name__ == "__main__":
#     main()