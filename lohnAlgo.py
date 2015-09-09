#! /usr/bin/python
def getLohn(num):
    return str(sum([sum(divmod(int(v)*(i%2 +1),10)) for i,v in enumerate(num)])*9%10)
    
def checkLohn(num):
    return getLohn(num[:-1]) == num[-1]


















##
##def getLohn(num):
##    return str(sum([str((i%2 + 1)*int(v)) for i,v in enumerate(num)])*9%10)
##
##













##
##
##def getLohn(num):
##    return str((10 - sum([((i+1)%2)*int(v) + (((i%2)*int(v)*2))%10 + (((i%2)*int(v)*2))/10 for i,v in enumerate(num)]))%10)
##  return str(sum(map(int,''.join([str((i%2 + 1)*int(v)) for i,v in enumerate(num)])))*9%10)
###(i%2 + 1)*int(v)%10 + (i%2 + 1)*int(v)/10
#def getLohn(num):
#    return str(sum([sum(divmod(int(v)*(i%2 +1),10)) for i,v in enumerate(num)])*9%10)










def getLohn2(num):
    return str((10 - sum([((i+1)%2)*int(num[i]) + (((i%2)*int(num[i])*2))%10 + (((i%2)*int(num[i])*2))/10 for i in range(len(num))]))%10)

def checkLohn2(num):
    return getLohn(num[:len(num) - 1]) == num[len(num)-1]
