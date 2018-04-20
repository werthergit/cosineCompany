#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import jieba.analyse
from math import sqrt

from functools import reduce


class Similarity():
    def __init__(self, target1, target2 ):
        self.target1 = target1
        self.target2 = target2

    def vector(self):
        self.vdict1 = {}
        self.vdict2 = {}
        for k, v in self.target1:
            self.vdict1[k] = v
        for k, v in self.target2:
            self.vdict2[k] = v

    def mix(self):
        for key in self.vdict1:
            self.vdict2[key] = self.vdict2.get(key, 0)
        for key in self.vdict2:
            self.vdict1[key] = self.vdict1.get(key, 0)

        def mapminmax(vdict):
            """计算相对词频"""
            _min = min(vdict.values())
            _max = max(vdict.values())
            _mid = _max - _min
            # print _min, _max, _mid
            for key in vdict:
                vdict[key] = (vdict[key] - _min) / _mid
            return vdict

        self.vdict1 = mapminmax(self.vdict1)
        self.vdict2 = mapminmax(self.vdict2)

    def similar(self):
        self.vector()
        self.mix()
        sum = 0
        for key in self.vdict1:
            sum += self.vdict1[key] * self.vdict2[key]
        A = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict1.values())))
        B = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict2.values())))
        return sum / (A * B)


if __name__ == '__main__':
    # top_keywords1 = {'a': 1, 'b': 0, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
    # top_keywords2 = {'a': 0, 'b': 1, 'c': 0, 'd': 1, 'e': 0, 'f': 0}
    top_keywords1 = {'101': 1, '102': 1, '103': 0, 'a': 0, '105': 1, '106': 0, '109': 0, '107': 0, '108': 0, '2000': 1, '2001': 0, '2002': 0, '2003': 0, '2004': 0}
    top_keywords2 = {'101': 0, '102': 0, '103': 0, 'a': 0, '105': 1, '106': 1, '109': 1, '107': 0, '108': 0, '2000': 0, '2001': 0, '2002': 1, '2003': 1, '2004': 0}
    s = Similarity(top_keywords1.items(), top_keywords2.items())
    print(s.similar())