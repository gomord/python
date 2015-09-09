import itertools
import types
def eq(oper,bi,onar):
    #print oper,bi
    res = bi[0](onar[0](oper[0]),onar[1](oper[1]))
    for i in range(1,len(bi)):
        res = bi[i](res,onar[i+1](oper[i + 1]))
    return res
def mul(a,b):
    return a*b
def dev(a,b):
    return a/b
def sub(a,b):
    return a - b
def sum(a,b):
    return a + b

def polish(stack):
    in_stack = []
    #print stack
    while stack != []:
        c = stack.pop()
        
        if type(c) == types.FunctionType:
            if len(in_stack) < 2:
                return None
            b = in_stack.pop()
            a = in_stack.pop()
            if c == dev and b == 0:
                return None
            in_stack.append(c(a,b))
        else:
            in_stack.append(c)
    if in_stack == []:
        return None
    else:
        return in_stack.pop()

            
def arr_sub(A,B):
    return tuple((x for x in A if x not in B))
bina = (sum,sub,mul,dev)

#for i in range(30):
i = 2
dic = {}
num = (1.,5.,6.,7.)
for oper in itertools.permutations(num,2):
    for bi in itertools.combinations_with_replacement(bina,3):
        for stack in itertools.permutations(bi+arr_sub(num,oper)):
            #print stack + oper
            res = polish(list(stack + oper))
            if res == None:
                continue
            if res == i:
                print stack + oper
            if (res % 1 == 0) and not dic.has_key(str(res)):
                dic[str(res)] = stack + oper[2:4]
                

            




        
        
