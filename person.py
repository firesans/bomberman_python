#!/usr/lib/python

from __future__ import print_function
import signal,copy,sys,time
from random import *
from board import *

import random
import threading
from threading import Timer
import time
import os

class person(object):

    def __init__(self):
        self._x = 2
        self._y = 4
        #self._b1 = 2
        #self._b2 = 4
        self._e1 = 30
        self._e2 = 4
        self._f = 1
        #initial co-ordinates given for bomberman :(2,4)

    def moveright(self,b):

        b.erase_man(self._x,self._y)
        b.bomberman(self._x,self._y+1)
        self._y = self._y+1

    def moveleft(self,b):

        b.erase_man(self._x,self._y)
        b.bomberman(self._x,self._y-1)
        self._y = self._y-1

    def moveup(self,b):

        b.erase_man(self._x,self._y)
        b.bomberman(self._x-1,self._y)
        self._x = self._x-1

    def movedown(self,b):

        b.erase_man(self._x,self._y)
        b.bomberman(self._x+1,self._y)
        self._x = self._x+1

    def move(self,b,c):

        if( c == 'a' and b.left_cond(self._x,self._y) == 1):
            self.moveleft(b)

        if( c == 's' and b.down_cond(self._x,self._y) == 1):
            self.movedown(b)

        if( c == 'w' and b.up_cond(self._x,self._y) == 1):
            self.moveup(b)

        if( c == 'd' and b.right_cond(self._x,self._y) == 1):
            self.moveright(b)

        os.system("c")
        b.printboard()

    '''def timebomb(self,b):

        #print(self._e1,self._e2)
        b.erase_bomb(self._b1,self._b2)
        b.print_bombreaction(self._b1,self._b2)
        b.bomb_kills_enemy(self._e1,self._e2)
        t = threading.Timer(1.0,self.bomb_clear_debris,args=(b,))
        t.start()

    def bomb_dropping(self,b):

        b.bomb(self._x,self._y)
        self._b1 = self._x
        self._b2 = self._y

        os.system("c")
        #b.printboard()

    def bomb_clear_debris(self,b):

        b.erase_bombdebris(self._b1,self._b2)'''

    def moveright_e(self,b):

        b.erase_enemy(self._e1,self._e2)
        self._e2 = self._e2 +1
        b.enemy_print(self._e1,self._e2)

    def moveleft_e(self,b):

        b.erase_enemy(self._e1,self._e2)
        self._e2 = self._e2 -1
        b.enemy_print(self._e1,self._e2)

    def moveup_e(self,b):

        b.erase_enemy(self._e1,self._e2)
        self._e1 = self._e1 -1
        b.enemy_print(self._e1,self._e2)

    def movedown_e(self,b):

        b.erase_enemy(self._e1,self._e2)
        self._e1 = self._e1 +1
        b.enemy_print(self._e1,self._e2)

    def enemy_movement(self,b):

        if(b._flag == 1):

            b.erase_enemy(self._e1,self._e2)
            return
        flag = 1
        while(flag):
            chance = random.randrange(0,4)
            if( chance == 0 and b.right_cond(self._e1,self._e2) == 1):

                if(b.enemy_rt_cond(self._e1,self._e2)):
                    #print (2)
                    b.erase_enemy(self._e1,self._e2)
                    self._e1 = 30
                    self._e2 = 4

                else:
                    self.moveright_e(b)
                    #b.enemy_print(self._e1,self._e2)
                flag = 0

            elif( chance == 1 and b.left_cond(self._e1,self._e2) == 1):
                if(b.enemy_lt_cond(self._e1,self._e2)):
                    b.erase_enemy(self._e1,self._e2)
                    self._e1 = 30
                    self._e2 = 4

                else:
                    self.moveleft_e(b)
                flag = 0

            elif( chance == 2 and b.up_cond(self._e1,self._e2) == 1):

                if(b.enemy_up_cond(self._e1,self._e2)):
                    b.erase_enemy(self._e1,self._e2)
                    self._e1 = 30
                    self._e2 = 4
                else:
                    self.moveup_e(b)
                    #b.enemy_print(self._e1,self._e2)
                flag = 0
            elif( chance == 3 and b.down_cond(self._e1,self._e2) == 1):

                if(b.enemy_dn_cond(self._e1,self._e2)):
                    #print ("down")
                    b.erase_enemy(self._e1,self._e2)
                    self._e1 = 30
                    self._e2 = 4
                else:
                    self.movedown_e(b)
                    #b.enemy_print(self._e1,self._e2)
                flag = 0

            else:
                flag = 1

        os.system('c')
        b.printboard()

    def flag_value(self):

        self._f = 1
        return self._f-1

    def change_parameter_man(self,x,y):

        self._x = x
        self._y = y

    def change_parameter_enemy(self,x,y):

        self._e1 = x
        self._e2 = y

    def enemy_kills_man(self,b):

        if(b.enemy_kills(self._x,self._y,self._e1,self._e2)==1):
            b.erase_man(self._x,self._y)
            return 1
        else:
            return 0

    def get_man_x(self):
        return self._x

    def get_man_y(self):
        return self._y

    def get_enemy_x(self):
        return self._e1

    def get_enemy_y(self):
        return self._e2

''' def get_bomb_x(self):
        return self._b1

    def get_bomb_y(self):
        return self._b2 '''
