# -*- coding: utf-8 -*-
__author__ = 'imressed'
"""Полиморфизм - разное поведение одного и того же метода в разных классах."""

#example 1
""" Например, мы можем сложить два числа,
и можем сложить две строки. При этом получим разный результат,
так как числа и строки являются разными классами."""
print(1 + 1)
print ('1' + '1')

#example 2
class Poly1:
    def func(self):
        return print('Poly1 func')


class Poly2:
    def func(self):
        return print('Poly2 func')


p1 = Poly1()
p2 = Poly2()
p1.func()
p2.func()