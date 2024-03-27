#!/usr/bin/env python3
#barborapavlu

import random

class: Kostka:

    def __init__(self, pocet_sten):
        self.pocetSten = pocet_sten

    def hod(self, max):
        return random.randint(1,self.pocetSten)

    def GetPocetSten(self):
        return self.__pocetSten


k1 = Kostka (6)
print (k1.hod())

k2 = Kostka (12)
print(k2.hod()) 

print(k1.getPocetSten())
