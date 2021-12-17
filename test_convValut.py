# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 21:36:32 2021

@author: Мрнаиа
"""

import pytest
from convValADAPTED import convertSum, enterCurr, enterCurr2, menu

cur = ""
UAHtoAll = {'UAH': 1, 'USD': 0.0379, 'GBP': 0.0276} #USD GBP
USDtoAll = {'USD': 1, 'UAH': 26.39, 'GBP': 0.73} #UAH GBP
GBPtoAll = {'GBP': 1, 'UAH': 36.27, 'USD': 1.37}#UAH USD
currList = {'UAH':UAHtoAll, 'USD':USDtoAll, 'GBP':GBPtoAll}

def test1GBPpositive():
    cur1 = enterCurr(currList, "GBP")
    cur2 = enterCurr2(currList, cur1, "UAH")
    assert cur1 == 'GBP' and cur2 == 'UAH'
    
def test2GBPnegative():
    with pytest.raises(Exception):
           enterCurr2(currList, "GBP", "GBP") == cur
def test3UAHpositive():
    cur1 = enterCurr(currList, "UAH")
    cur2 = enterCurr2(currList, cur1, "USD")
    assert cur1 == "UAH" and cur2 == "USD"
    
def test4UAHnegative():
    with pytest.raises(Exception):
           enterCurr2(currList, "UAH", "UAH") == cur
           
def test5USDpositive():
    cur1 = enterCurr(currList, "USD")
    cur2 = enterCurr2(currList, cur1, "GBP")
    assert cur1 == "USD" and cur2 == "GBP"
    
def test6USDnegative():
    with pytest.raises(Exception):
           enterCurr2(currList, "USD", "USD") == cur
           
def test7negativeVal1():
    with pytest.raises(Exception):
           enterCurr(currList, "EUR") == cur
    
def test7negativeVal2():
    with pytest.raises(Exception):
           enterCurr(currList, "DDSLA") == cur
           
def test7negativeVal3():
    with pytest.raises(Exception):
           enterCurr(currList, "ЫЫЫ") == cur
              
def test8PositiveComm1():
    command = menu(1)
    assert command == 1
    
def test8PositiveComm2():
    command = menu(2)
    assert command == 2

def test8PositiveComm3():
    command = menu(3)
    assert command == 3

def test8PositiveComm0():
    command = menu(0)
    assert command == 12
    

def test9NegativeComm1():
    with pytest.raises(Exception):
          menu(-334) == cur
          
def test9NegativeComm2():
    with pytest.raises(Exception):
          menu("aaaaaaaa") == cur
          
def test9NegativeComm3():
    with pytest.raises(Exception):
          menu(8) == cur

def test10PositiveSum1():
    sum = convertSum(UAHtoAll, "USD", 12)
    assert sum > 0

def test10PositiveSum2():
    sum = convertSum(UAHtoAll, "USD", 465.50)
    assert sum > 0

def test11NegativeSum1():
    with pytest.raises(Exception):
          convertSum(GBPtoAll, "UAH", "ады23") == cur

def test11NegativeSum2():
    with pytest.raises(Exception):
          convertSum(GBPtoAll, "UAH", "12d334a5") == cur

def test11NegativeSum3():
    with pytest.raises(Exception):
          convertSum(GBPtoAll, "UAH", -124) == cur
          
def test11NegativeSum4():
    with pytest.raises(Exception):
          convertSum(GBPtoAll, "UAH", 9999999999999) == cur

def test12Conv1():
    sum = convertSum(USDtoAll, "UAH", 100)
    assert sum == 2639

def test12Conv2():
    sum = convertSum(USDtoAll, "UAH", 3450.40)
    sum = round(sum, 2)
    assert sum == 91056.06

