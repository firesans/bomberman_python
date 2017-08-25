#!/usr/lib/python

from board import *
from person import *
p = person()


class enemy(person):

    def __init__(self):
        person.__init__(self)
        self._e1 = 30
        self._e2 = 4
        self._e3 = 2
        self._e4 = 60
        #self._e5 = 2
        #self._e6 = 60
        self._flagp = 0
        self._flagq = 0
        self._score = 0

    def enemy_print(self,b,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                b._bombmatrix[i][j] = 'E'

    def erase_enemy(self,b,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                b._bombmatrix[i][j] = ' '

    def enemy_kills(self,x,y,p,q):

        if(x == p and y == q):
            return 1;
        if(x == p and y+3 == q):
            return 1;
        if(x == p+1 and y == q):
            return 1;
        if(x == p and y-3 == q):
            return 1;
        if(x == p-1 and y == q):
            return 1;
        else:
            return 0;

    def enemy_dn_cond(self,b,x,y):

        for i in range(0,4):
            if(b._bombmatrix[x+2][y+i] == '^'):
                return True
            else:
                return False

    def enemy_up_cond(self,b,x,y):

        for i in range(0,4):
            if(b._bombmatrix[x-1][y+i] == '^'):
                return True
            else:
                return False

    def enemy_rt_cond(self,b,x,y):

        for i in range(0,2):
            if(b._bombmatrix[x+i][y+4] == '^'):
                return True
            else:
                return False

    def enemy_lt_cond(self,b,x,y):

        for i in range(0,2):
            if(b._bombmatrix[x+i][y-1] == '^'):
                return True
            else:
                return False

    def bomb_kills_enemy1(self,b):

        if self.enemy_rt_cond(b,self._e1,self._e2) or self.enemy_lt_cond(b,self._e1,self._e2) or self.enemy_up_cond(b,self._e1,self._e2) or self.enemy_dn_cond(b,self._e1,self._e2):
            self._flagq = 1
            self._score = self._score + 100
            return 1
        else:
            return 0

    def bomb_kills_enemy2(self,b):

        if self.enemy_rt_cond(b,self._e3,self._e4) or self.enemy_lt_cond(b,self._e3,self._e4) or self.enemy_up_cond(b,self._e3,self._e4) or self.enemy_dn_cond(b,self._e3,self._e4):
            self._flagp = 1
            self._score = self._score + 100
            return 1
        else:
            return 0

    def get_score(self):

        return self._score

    def moveright_e1(self,b):

        b.erase_enemy(self._e1,self._e2)
        self._e2 = self._e2 +1
        b.enemy_print(self._e1,self._e2)

    def moveleft_e1(self,b):

        b.erase_enemy(self._e1,self._e2)
        self._e2 = self._e2 -1
        b.enemy_print(self._e1,self._e2)

    def moveup_e1(self,b):

        b.erase_enemy(self._e1,self._e2)
        self._e1 = self._e1 -1
        b.enemy_print(self._e1,self._e2)

    def movedown_e1(self,b):

        b.erase_enemy(self._e1,self._e2)
        self._e1 = self._e1 +1
        b.enemy_print(self._e1,self._e2)

    def moveright_e2(self,b):

        b.erase_enemy(self._e3,self._e4)
        self._e4 = self._e4 +1
        b.enemy_print(self._e1,self._e2)

    def moveleft_e2(self,b):

        b.erase_enemy(self._e3,self._e4)
        self._e4 = self._e4 -1
        b.enemy_print(self._e3,self._e4)

    def moveup_e2(self,b):

        b.erase_enemy(self._e3,self._e4)
        self._e3 = self._e3 -1
        b.enemy_print(self._e3,self._e4)

    def movedown_e2(self,b):

        b.erase_enemy(self._e3,self._e4)
        self._e3 = self._e3 +1
        b.enemy_print(self._e3,self._e4)

    def enemy1_movement(self,b):

        if(self._flagq == 1):
            #self._flagq = 0
            b.erase_enemy(self._e1,self._e2)
            return

        flag1 = 1
        while(flag1):
            chance = random.randrange(0,4)
            if( chance == 0 and b.right_cond(self._e1,self._e2) == 1):
                if(self.enemy_rt_cond(b,self._e1,self._e2)):
                    #print (2)
                    self.erase_enemy(b,self._e1,self._e2)

                else:
                    self.moveright_e1(b)
                    #b.enemy_print(self._e1,self._e2)
                flag1 = 0

            elif( chance == 1 and b.left_cond(self._e1,self._e2) == 1):
                if(self.enemy_lt_cond(b,self._e1,self._e2)):
                    self.erase_enemy(b,self._e1,self._e2)

                else:
                    self.moveleft_e1(b)
                flag1 = 0

            elif( chance == 2 and b.up_cond(self._e1,self._e2) == 1):

                if(self.enemy_up_cond(b,self._e1,self._e2)):
                    self.erase_enemy(b,self._e1,self._e2)
                else:
                    self.moveup_e1(b)
                    #b.enemy_print(self._e1,self._e2)
                flag1 = 0

            elif( chance == 3 and b.down_cond(self._e1,self._e2) == 1):

                if(self.enemy_dn_cond(b,self._e1,self._e2)):
                   #print ("down")
                    self.erase_enemy(b,self._e1,self._e2)
                else:
                    self.movedown_e1(b)
                   #b.enemy_print(self._e1,self._e2)
                flag1 = 0
            else:
                flag1 = 1

            os.system('c')
            b.printboard()

    def enemy2_movement(self,b):

        if(self._flagp == 1):
        #    self._flag = 0
            b.erase_enemy(self._e3,self._e4)
            return

        flag1 = 1
        while(flag1):

            chance = random.randrange(0,4)
            if( chance == 0 and b.right_cond(self._e3,self._e4) == 1):
                if(self.enemy_rt_cond(b,self._e3,self._e4)):
                #print (2)
                    self.erase_enemy(b,self._e3,self._e4)
                else:
                    self.moveright_e2(b)
                                #b.enemy_print(self._e1,self._e2)
                flag1 = 0

            elif( chance == 1 and b.left_cond(self._e3,self._e4) == 1):
                if(self.enemy_lt_cond(b,self._e3,self._e4)):
                    self.erase_enemy(b,self._e3,self._e4)

                else:
                    self.moveleft_e2(b)

                flag1 = 0

            elif( chance == 2 and b.up_cond(self._e3,self._e4) == 1):
                if(self.enemy_up_cond(b,self._e3,self._e4)):
                    self.erase_enemy(b,self._e3,self._e4)
                else:
                    self.moveup_e2(b)
                                #b.enemy_print(self._e1,self._e2)
                flag1 = 0

            elif( chance == 3 and b.down_cond(self._e3,self._e4) == 1):
                if(self.enemy_dn_cond(b,self._e3,self._e4)):
                #print ("down")
                    self.erase_enemy(b,self._e3,self._e4)
                else:
                    self.movedown_e2(b)
                    #b.enemy_print(self._e1,self._e2)
                flag1 = 0

            else:
                flag1 = 1

            os.system('c')
            b.printboard()

    def enemy1_kills_man(self,b,p):

        if(b.enemy_kills(p.get_man_x(),p.get_man_y(),self._e1,self._e2)==1):
            b.erase_man(p.get_man_x(),p.get_man_y())
            return 1
        else:
            return 0


    def enemy2_kills_man(self,b,p):

        if(b.enemy_kills(p.get_man_x(),p.get_man_y(),self._e3,self._e4)==1):
            b.erase_man(p.get_man_x(),p.get_man_y())
            return 1
        else:
            return 0
