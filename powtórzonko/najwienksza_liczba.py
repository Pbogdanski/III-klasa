#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  najwienksza_liczba.py
#  
#  Copyright 2019  <>
#  
#  


def main(args):
    a = int(input("Podaj liczbę:"))
    print(a)
    b = int(input("Podaj liczbę jeszcze jedną:"))
    print (b)
    c = int(input("Proszę nie podawać takich samych liczb bo to bardzo niemiłe i nierozsądne"))
    print (c)
        
    if a > b and a > c:
        print("Ło ale duża ta pierwsza liczba normalnie największa z tych wszystkich")
    
    if b > a and b > c:
        print("Druga liczba jest bardzo i w ogóle Proszę pamiętać że byłem tylko na jednej lekcji")
    
    if c > a and c > b:
        print("a trzecia świnka zbudowała dom z czerstwego chleba")
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
