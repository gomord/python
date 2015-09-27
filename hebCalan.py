# -*- coding: utf-8 -*-
def decode(uni,delta):
	return hex(int(uni.encode('hex'),16) + delta)[2:].decode('hex')
uni_sufex = [10,13,15,19,21]
heb_let = [decode('א',i) for i in range(26) if i not in uni_sufex]
heb_gemat = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400]
#def heb_gemat(ind):
#    return 10**(ind/10)*(ind%10 + 1 ) + 10**(ind/10)*(ind/10)
def num2hebuni(num):
    res = ''
    i = 0
    while num > 0:
        red = num%10
        num /= 10
        res = deheb_gemat[i*red] + res
        
        
    
