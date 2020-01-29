#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:19:17 2020

@author: taimaame
"""

def trans(one_num):

    num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res=''
    for i in range(len(num_list)):
        while one_num>=num_list[i]:
            one_num-=num_list[i]
            res+=str_list[i]
    return res


if __name__ == '__main__':
    
    one_num_list=[77,66,55,8,1200,34,65,3,21,99]
    for one_num in one_num_list:
        print(one_num,trans(one_num))
