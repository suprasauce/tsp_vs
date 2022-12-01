import pygame as py, colors, main as m

mini= 1000000009
minimumpath=[]
def findpath(current,visited,costmatrix,cost,path,n):
    global mini
    global minimumpath
    visited[current]=True
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
    print(mini)
    print(minimumpath)



if __name__ == "__main__":
    main()