# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:44:37 2021

@author: Мрнаиа
"""
UAHtoAll = {'UAH': 1, 'USD': 0.0379, 'GBP': 0.0276} #USD GBP
USDtoAll = {'USD': 1, 'UAH': 26.39, 'GBP': 0.73} #UAH GBP
GBPtoAll = {'GBP': 1, 'UAH': 36.27, 'USD': 1.37}#UAH USD
currList = {'UAH':UAHtoAll, 'USD':USDtoAll, 'GBP':GBPtoAll}

def convertSum(currencyFrom, currencyTo, moneySum):#dictionary, string, float
    if moneySum < 0 or moneySum > 9999999999998:
        raise Exception
    else:
        return currencyFrom[currencyTo]*moneySum

def enterCurr(curList, wantedCur):
        if wantedCur in curList:
            return wantedCur
        else:
            raise Exception
        
def enterCurr2(curList, cur1, wantedCur):
        if wantedCur in curList and wantedCur != cur1:
            return wantedCur
        else:
            raise Exception        

'''UAHtoAll = {'UAH': 1, 'USD': 0.0379, 'GBP': 0.0276} #USD GBP
USDtoAll = {'USD': 1, 'UAH': 26.39, 'GBP': 0.73} #UAH GBP
GBPtoAll = {'GBP': 1, 'UAH': 36.27, 'USD': 1.37}#UAH USD
currList = {'UAH':UAHtoAll, 'USD':USDtoAll, 'GBP':GBPtoAll}
#resultSum = convertSum(UAHtoAll, 'GBP', 56)
#print("%.2f" %resultSum)

sumFrom = 0
sumFinal = 0'''


def menu(switch, parameters = 0):
    if switch == 1:        
        #sumFrom = parameters[0]
        #sumFinal = convertSum(currList[parameters[1]], parameters[2], sumFrom)
        return 1
    elif switch == 2:
        #curFrom = enterCurr(currList, parameters[0])
        #curTo = enterCurr2(currList, parameters[0], parameters[1])
        return 2
    elif switch == 3:
        #parameters[0], parameters[1] = parameters[1], parameters[0]
        #return [parameters[0], parameters[1]]
        return 3
    elif switch == 0:
        return 0
    else:
        raise Exception

