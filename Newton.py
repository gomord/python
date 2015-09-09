pol2 = [1050,50,50,50,50,-920.7]
pol3 = [1070,70,70,70,70,-1003.1]
pol4 = [1120,120,120,120,120,-1209.2]


def pol_calc(pol,val):
    return sum([it*pow(val,i) for i,it in enumerate(pol)])
def polt(pol):
       return [(i+1)*it for i,it in enumerate(pol[1:])] 
def Newton(pol,val):
    p = pol_calc(pol,val)
    pt= pol_calc(polt(pol),val)
    return val - float(p)/pt

def mayki(pol,start,count):
    res = start
    #reduce(Newton
    for i in range(count):
        res = Newton(pol,res)
    print (res - 1)*100

    
##>>> mayki(pol2,1,10)
##6.93045311089
##>>> mayki(pol3,1,10)
##6.92454656742
##>>> mayki(pol4,1,10)
##6.91008423702
