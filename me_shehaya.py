demand = [100.0,200.0,300.0]
def tools(demand):
	max_dem = max(demand)
	tools = [(x/2 , max_dem - x/2) for x in demand]
	return tools

def in_range(tools,total):
        amount = []
        #print total , max(tools,key=lambda a : a[0])

        if(total < max(tools,key=lambda a : a[0]) [0]):
                amount = filter(lambda tool: total < tool[0] ,tools)
                min_dem = min(amount,key=lambda a : a[0])
                ##print amount , min_dem
                return float(min_dem[0] - total) ,len(amount)
        else:
                amount = filter(lambda tool:total < tool[1],tools)
                min_dem = min(amount,key=lambda a : a[1])
                ##print amount , min_dem
                return float((min_dem[1] - total)), (len(tools) - len(amount))
def calc(demand,mony):
                total = float(0)
                mony = float(mony) 
                tools_arr = tools(demand)
                while(mony > 0):
                        ###print "b = to,mo",total,mony
                        amount, n = in_range(tools_arr,total)
                        ###print "amm,n",amount,n
                        total   += min(amount,mony/n)
                        mony   -= min(amount*n,mony)
                        
                        ###print "a = to,mo",total,mony
                
                return total
def printRes(demand,mony):
        to = tools(demand)
        ca = calc(demand,mony)
        for i in to:
                if i[0] > ca:
                        print i[0]*2 , ca
                elif ca >= i[0] and i[1] > ca:
                        print i[0]*2 , i[0]
                else:
                        print i[0]*2, ca - i[1] + i[0]

print "== 100 =="
printRes(demand,100)
print "== 200 =="
printRes(demand,200)
print "== 300 =="
printRes(demand,300)

