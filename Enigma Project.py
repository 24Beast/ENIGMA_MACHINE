#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      BHANU
#
# Created:     12-12-2018
# Copyright:   (c) BHANU 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import string

class Switch_Board:
    def __init__(self):
        self.input=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.output=[]

    def set_board(self):
        for i in range(0,26):
            c=0
            print "CURRENT INPUT VALUE:",self.input[i],'\n'
            v=raw_input("ENTER OUTPUT VALUE")
            for j in self.output:
                if (j==v):
                    print "INPUT ALREADY USED"
                    c=c+1
            if(c>0):
                i=i-1
            else:
                self.output.append(v)

    def convert(self,x):
        x=string.upper(x)
        for i in range(0,26):
            if(self.input[i]==x):
                return self.output[i]

class Wheel:
    def __init__(self):
        self.outer=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.inner=[]
        self.c=0

    def setinner(self):
        for i in range(0,26):
            print "CURRENT OUTER WHEEL VALUE:",self.outer[i],'\n'
            v=raw_input("ENTER INNER WHEEL VALUE FOR CURRENT OUTER WHEEL VALUE: \n")
            for j in self.inner:
                if (j==v):
                    print "INPUT ALREADY USED"
                    c=c+1
            if(c>0):
                i=i-1
            else:
                self.inner.append(v)

    def signal(self,x):
        y=string.upper(x)
        for i in range(0,26):
            if(self.outer[i]==y):
                break
        return self.inner[(i+c)%26]

    def rotate(self,x):
        self.c=self.c+1
        self.signal(x);

    def checkc(self):
        return self.c/26

    def setval(self,m):
        m=string.upper(m)
        self.c=m+self.c

    def Reflect(self,m):
        m=string.upper(m)
        if(ord(m)>(ord(A)+ord(Z))/2):
            return chr(ord(m)-13)
        else:
            return chr(ord(m)+13)

    def back(self,m):
        m=string.upper(m)
        for i in range(0,26):
            if(self.inner[i]==m):
                break
        return self.outer[(i-c)%26]


class EnigmaMachine:
    def __init__(self):
        self.Switch=Switch_Board()
        self.Wheel1=Wheel()
        self.Wheel2=Wheel()
        self.Wheel3=Wheel()
        self.Reflector=Wheel()
        self.input=''

    def set_Machine(self):
        print "ENTER VALUES TO SET MACHINE \n"
        self.Switch.set_board()
        self.Wheel1.setinner()
        m1=raw_input("ENTER INITIAL SETTING OF WHEEL 1 \n")
        self.Wheel1.setval(m1)
        self.Wheel2.setinner()
        m2=raw_input("ENTER INITIAL SETTING OF WHEEL 2 \n")
        self.Wheel2.setval(m2)
        self.Wheel3.setinner()
        m3=raw_input("ENTER INITIAL SETTING OF WHEEL 3 \n")
        self.Wheel1.setval(m3)

    def execution(self):
        e=raw_input("ENTER DATA TO BE ENCRYPTED (ENTER -1 TO TERMINATE)")
        while(e!='-1'):
            e1=self.Switch.convert(e)
            w1=self.Wheel1.rotate(e1)
            c1=self.Wheel1.checkc()
            self.Wheel2.setval(c1)
            w2=self.Wheel2.signal(w1)
            c2=self.Wheel2.checkc()
            self.Wheel2.setval(c2)
            w3=self.Wheel2.signal(w2)
            r1=self.Reflector.Reflect(w3)
            r2=self.Wheel3.back(r1)
            r3=self.Wheel2.back(r2)
            ans=self.Wheel1.back(r3)
            print ans
            e=raw_input()

Enigma=EnigmaMachine()
Enigma.set_Machine()
Enigma.execution()

""" Notes:
    Following are the wheel settings at http://enigmaco.de/enigma/enigma.html
    Wheel1=[B,]"""