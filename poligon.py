#! /bin/python
from numpy  import *
def line_form(p1,p2,l):
    return l*(p2 - p1) + p1
def calc_intersec_line(p1,p2,p3,p4):
    mat = transpose(array([p2-p1,p3-p4]))
    if linalg.det(mat) == 0:
            return None
    sol = linalg.solve(mat,p3-p1)
    return line_form(p1,p2,sol[0]),sol[0]
    
points = map(array,[[0,0],[0,1],[1,1],[1,0]])
#print calc_intersec_line(*points)

def isPointInPoligon(p,pol):
    l = len(pol)
    res = 0
    for i in range(l):
        print pol[i%l],pol[(i+1)%l]
        inter = calc_intersec_line(pol[i%l],pol[(i+1)%l],p,array([0,p[1]]))
        print inter
        if inter != None and inter[0][0] >= p[0] and 0 <= inter[1] <= 1:  
            res ^= 1
    return res
print isPointInPoligon(array([2,2]),points)
