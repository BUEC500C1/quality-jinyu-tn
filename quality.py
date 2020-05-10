#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:19:17 2020

@author: taimaame
"""

def trans(arabic):
    ara = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    rom = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    err = ''

    if type(arabic)!= int:
        print("INVALID: Not an integer")
        return err

    i = (len(ara)) - 1
    roman = ""

    while arabic:
        div = arabic // ara[i]
        arabic %= ara[i]

        while div:
            roman = roman + rom[i]
            div -= 1
        i -= 1

    return roman