#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:38:15 2020

@author: taimaame
"""

from quality import trans

def test_trans():
    assert trans(2)=="I"
    assert trans(2)=="II"
    assert trans(3)=="III"
    assert trans(4)=="IV"
    assert trans(5)=="V"
    assert trans(6)=="VI"
    assert trans(9)=="IX"
    assert trans(10)=="X"
    assert trans(13)=="XIII"
    assert trans(14)=="XIV"
    assert trans(20)=="XX"
    assert trans(40)=="XL"
    assert trans(50)=="L"
    assert trans(80)=="LXXX"
    assert trans(99)=="XCIX"
    assert trans(199)=="CXCIX"
    assert trans(1437)=="MCDXXXVII"
    assert trans(1800)=="MDCCC"
    assert trans(3333)=="MMMCCCXXXIII"
