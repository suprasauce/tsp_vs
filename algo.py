# import sys    

mini= 1000000009
minimumpath=[]


def cost(nodes,costmatrix):
    cst=0
    for i in range(1,len(nodes)):
        cst+=costmatrix[nodes[i-1]][nodes[i]]
    cst+=costmatrix[nodes[len(nodes)-1]][nodes[0]]
    return cst


def permute(start,end,nodes,costmatrix):
    global mini
    global minimumpath
    if start==end:
        fps=cost(nodes,costmatrix)
        if fps<mini:
            mini=fps
            minimumpath=nodes[:]
            # print(minimumpath)
    else:
        for i in range(start,end):
            nodes[start],nodes[i]=nodes[i],nodes[start]
            permute(start+1,end,nodes,costmatrix)
            nodes[start],nodes[i]=nodes[i],nodes[start]
            



def main():
    global mini
    global minimumpath
    # print(sys.maxint)
    n=4
    nodes= [x for x in range(0,n)]
    costmatrix=[[ 0, 10, 15, 20 ],
                       [ 10, 0, 35, 25 ],
                       [ 15, 35, 0, 30 ],
                       [ 20, 25, 30, 0 ]]
    permute(0,n,nodes,costmatrix)
    print(mini)
    for i in range(n):
        minimumpath[i]=minimumpath[i]+1
    




if __name__=="__main__":
    main()