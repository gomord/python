#! /bin/python
import numpy as np
import cv2

def line_form(p1,p2,l):
    return l*(p2 - p1) + p1
def calc_intersec_line(p1,p2,p3,p4):
    mat = np.transpose(np.array([p2-p1,p3-p4]))
    if np.linalg.det(mat) == 0:
            return None
    sol = np.linalg.solve(mat,p3-p1)
    return line_form(p1,p2,sol[0]),sol[0]
    

#print calc_intersec_line(*points)

def isPointInPoligon(p,pol):
    intersecLines = []
    l = len(pol)
    res = 0
    for i in range(l):
        p1 = pol[i%l]
        p2 = pol[(i+1)%l]
        if p2[1] == p1[1] == p[1]:
            diff = (pol[(i-1)%l][1] - p2[1])*(pol[(i+2)%l][1] - p2[1])
            if diff > 0:
                res ^= 1
            elif diff < 0:
                continue
            else:
                raise
            
            
        inter = calc_intersec_line(p1,p2,p,np.array([0,p[1]]))
        print inter
        if inter != None and inter[0][0] >= p[0] and 0 <= inter[1] <= 1:
            intersecLines.append(inter[0])
            res ^= 1
    return res,intersecLines
def make_poligon(i,is_str = False):
    ret = []
    max_x = (i&~1)
    for i in range(1,max_x):
        if is_str:
            print "[%d,%d],"%((i*20),20+(i%2)*20),
        else:
            ret.append([i*20,20+(i%2)*20])
    if is_str:
        print "[%d,%d],"%((max_x - 20)/2,100),
    else:
        ret.append([(max_x*20 - 20)/2,100])
        return ret
        
po = np.array([40,30])
points = np.array(make_poligon(20))

res, inter =  isPointInPoligon(po,points)
inter = map(lambda ar:ar.astype(int),inter)
inter= sorted(inter,key=lambda x:x[0])
print "inter" , inter

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a polygon
#pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = points
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
colers = ((0,255,200),(100,100,100))
co = 0
last = po
for p in inter:
    
    print "co",co
    cv2.line(img,tuple(last.astype(int)),tuple(p),colers[co])
    last = p
    co ^=  1
    
print "co",co
if len(inter) == 0:
    cv2.line(img,tuple(po),(po[0],1000),colers[co])
else:
    print "co --",co

    print tuple(inter[-1]),tuple(np.array((1000,inter[-1][1])))
    cv2.line(img,tuple(inter[-1]),tuple(np.array((1000,inter[-1][1]))),colers[co])
             
cv2.namedWindow('img', cv2.CV_WINDOW_AUTOSIZE)

#Display the image
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range(1,10):
    cv2.waitKey(2)
