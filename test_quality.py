#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:38:15 2020

@author: taimaame
"""
from quality import trans



def test_1():
    assert trans(1014) == 'MXIV'


def test_2():
    assert trans(6) == 'VI'


def test_3():
    assert trans(1776) == 'MDCCLXXVI'


def test_string():
    assert trans('invalid') == ''


def test_decimal():
    assert trans(1.776) == ''


def test_mix():
    assert trans('1776invalid') == ''
