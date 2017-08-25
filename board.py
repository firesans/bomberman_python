#!/usr/bin/python
import random
import sys

from termcolor import colored
import random
import threading
import time

class board(object):
    

    def __init__(self):
        
        self._flag = 0
        
        self._matrix = []
        for i in range(34):
            temp = []
            for j in range(68):
               temp.append(0)
            self._matrix.append(temp)


        self._bombmatrix = []
        for i in range(34):
                       
            temp = []
            for j in range(68):
                var = ' '
                temp.append(var)
            self._bombmatrix.append(temp)

        self._debrismatrix = []
        for i in range(34):

            temp = []
            for j in range(68):
                var = ' '
                temp.append(var)
            self._debrismatrix.append(temp)
        

    def initboard(self):

        t = 1
        for i in range(0,2):
            for j in range(0,68):
            #   print (i)
                self._matrix[i][j] = "#"

        for k in range(0,7):
            for i in range(t+1,t+3):
                for j in range(0,4):
                    self._matrix[i][j] = "#"

                for j in range(4,64):
                    self._matrix[i][j] = " "

                for j in range(64,68):
                    self._matrix[i][j] = "#"

            for i in range(t+3,t+5):
              #  print (i)
                for j in range(0,4):
                    self._matrix[i][j] = "#"

                for j in range(4,8):
                    self._matrix[i][j] = " "

                for j in range(8,12):
                    self._matrix[i][j] = "#"

                for j in range(12,16):
                    self._matrix[i][j] = " "

                for j in range(16,20):
                    self._matrix[i][j] = "#"

                for j in range(20,24):
                    self._matrix[i][j] = " "

                for j in range(24,28):
                    self._matrix[i][j] = "#"

                for j in range(28,32):
                    self._matrix[i][j] = " "

                for j in range(32,36):
                    self._matrix[i][j] = "#"

                for j in range(36,40):
                    self._matrix[i][j] = " "

                for j in range(40,44):
                    self._matrix[i][j] = "#"

                for j in range(44,48):
                    self._matrix[i][j] = " "

                for j in range(48,52):
                    self._matrix[i][j] = "#"

                for j in range(52,56):
                    self._matrix[i][j] = " "

                for j in range(56,60):
                    self._matrix[i][j] = "#"

                for j in range(60,64):
                    self._matrix[i][j] = " "

                for j in range(64,68):
                    self._matrix[i][j] = "#"

            t = t + 4

        for i in range(30,32):
            for j in range(0,4):
                self._matrix[i][j] = "#"

            for j in range(4,64):
                self._matrix[i][j] = " "

            for j in range(64,68):
                self._matrix[i][j] = "#"

        for i in range(32,34):
            for j in range(0,68):
                self._matrix[i][j] = "#"

    
    def erase_man(self,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                self._matrix[i][j] = ' '

    def erase_enemy(self,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                self._bombmatrix[i][j] = ' '

    def erase_enemy_reaction(self,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                self._bombmatrix[i][j] = 'b'

    def erase_bomb(self,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                self._bombmatrix[i][j] = ' '
        
        
    def bomberman(self,x,y):

        self._matrix[x][y] = colored('[','yellow',attrs=['bold'])
        self._matrix[x][y+1] = colored('^','green',attrs=['bold'])
        self._matrix[x][y+2] = colored('^','green',attrs=['bold'])
        self._matrix[x][y+3] = colored(']','yellow',attrs=['bold'])
        self._matrix[x+1][y] = colored(' ','yellow',attrs=['bold'])
        self._matrix[x+1][y+1] = colored(']','yellow',attrs=['bold'])
        self._matrix[x+1][y+2] = colored('[','yellow',attrs=['bold'])
        self._matrix[x+1][y+3] = colored(' ','yellow',attrs=['bold'])


    def up_cond(self,x,y):

        if(self._matrix[x-1][y] == '#' or self._matrix[x-1][y+1] == '#' or self._matrix[x-1][y+2] == '#' or self._matrix[x-1][y+3] == '#' or self._bombmatrix[x-1][y] == '%' or self._bombmatrix[x-1][y+1] == '%' or self._bombmatrix[x-1][y+2] == '%' or self._bombmatrix[x-1][y+3] == '%'):
            return 0;
        else:
            return 1;
        
    def down_cond(self,x,y):

        if(self._matrix[x+2][y] == '#' or  self._matrix[x+2][y+1] == '#' or self._matrix[x+2][y+2] == '#' or self._matrix[x+2][y+3] == '#' or self._bombmatrix[x+2][y] == '%' or self._bombmatrix[x+2][y+1] == '%' or self._bombmatrix[x+2][y+2] == '%' or self._bombmatrix[x+2][y+3] == '%'):
            return 0;

        else:
            return 1;

    def right_cond(self,x,y):

        if(self._matrix[x][y+4] == '#' or self._matrix[x+1][y+4] == '#' or self._bombmatrix[x][y+4] == '%' or self._bombmatrix[x+1][y+4] == '%'):
            return 0;

        else:
            return 1;

    def left_cond(self,x,y):

        if(self._matrix[x][y-1] == '#' or self._matrix[x+1][y-1] == '#' or self._bombmatrix[x][y-1] == '%' or self._bombmatrix[x+1][y-1] == '%'):
            return 0;

        else:
            return 1;


    def up_cond_bomb(self,x,y):

        if(self._matrix[x-1][y] == '#' or self._matrix[x-1][y+1] == '#' or self._matrix[x-1][y+2] == '#' or self._matrix[x-1][y+3] == '#' ):
            return 0;
        else:
            #self._flag = 1
            return 1;
        
    def down_cond_bomb(self,x,y):

        if(self._matrix[x+2][y] == '#' or  self._matrix[x+2][y+1] == '#' or self._matrix[x+2][y+2] == '#' or self._matrix[x+2][y+3] == '#' ):
            return 0;

        else:
            #self._flag = 2
            return 1;

    def right_cond_bomb(self,x,y):

        if(self._matrix[x][y+4] == '#' or self._matrix[x+1][y+4] == '#'):
            return 0;

        else:
            #self._flag = 3
            return 1;

    def left_cond_bomb(self,x,y):

        if(self._matrix[x][y-1] == '#' or self._matrix[x+1][y-1] == '#'):
            return 0;

        else:
           # self._flag = 4
            return 1;
          
    def printboard(self):
        
        for i in range(0,34):
            for j in range(0,68):
                if(self._matrix[i][j] != ' '):
                    print colored(self._matrix[i][j],'blue'),
                #elif(self._matrix[i][j] == 'E' and self._bombmatrix[i][j] == '^'):
                #    print (self._bombmatrix[i][j])
                else:
                    print colored(self._bombmatrix[i][j],'red'),
            print " "


    def print_leftover_debris(self):

        for i in range(0,34):
            for j in range(0,68):
                if(self._bombmatrix[i][j] == ' '):
                    print (self._matrix[i][j])
               # elif(self._bombmatrix[i][j] == '^' and self._matrix[i][j] == 'E'):
               #     print (self._bombmatrix[i][j])
                else:
                    print (self._bombmatrix[i][j])

    def bomb(self,x,y):

        self._bombmatrix[x][y] = '['
        self._bombmatrix[x][y+1] = '0'
        self._bombmatrix[x][y+2] = '0'
        self._bombmatrix[x][y+3] = ']'
        self._bombmatrix[x+1][y] = '['
        self._bombmatrix[x+1][y+1] = '0'
        self._bombmatrix[x+1][y+2] = '0'
        self._bombmatrix[x+1][y+3] = ']'

    def change_num_bomb(self,x,y):

        t = 3
        while(t >0):
            for i in range(0,2):
                for j in range(0,2):
                    self._bombmatrix[x+i][y+1+j] = t
            t = t-1
            os.system('c')
            self.printboard()

    def walls(self,x,y):

        for i in range(0,2):
            for j in range(0,4):
                self._bombmatrix[x+i][y+j] = '%'

    def print_bombreaction(self,x,y):
        for i in range(x,x+2):
            for j in range(y,y+4):
                self._bombmatrix[i][j] = '^'

        for i in range(0,4):
            if(self.right_cond_bomb(x,y+i) == 1):
                self._bombmatrix[x][y+4+i] = '^'
                self._bombmatrix[x+1][y+4+i] = '^'
            else:
                break

        for i in range(1,5):
            if(self.left_cond_bomb(x,y-i) == 1):
                self._bombmatrix[x][y-i] = '^'
                self._bombmatrix[x+1][y-i] = '^'
            else:
                break

        for i in range(1,5):
            if(self.up_cond_bomb(x-i,y) == 1 and x >= 2):
                self._bombmatrix[x-i][y] = '^'
                self._bombmatrix[x-i][y+1] = '^'
                self._bombmatrix[x-i][y+2] = '^'
                self._bombmatrix[x-i][y+3] = '^'
            else:
                break

        for i in range(0,4):
            if(self.down_cond_bomb(x+i,y) == 1 and x <= 30):
                self._bombmatrix[x+2+i][y] = '^'
                self._bombmatrix[x+2+i][y+1] = '^'
                self._bombmatrix[x+2+i][y+2] = '^'
                self._bombmatrix[x+2+i][y+3] = '^'
            else:
                break

    def erase_bombdebris(self,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                self._bombmatrix[i][j] = ' '

        for i in range(0,4):
            if(self.right_cond_bomb(x,y+i) == 1):
                self._bombmatrix[x][y+4+i] = ' '
                self._bombmatrix[x+1][y+4+i] = ' '

        for i in range(1,5):
            if(self.left_cond_bomb(x,y-i) == 1):
                self._bombmatrix[x][y-i] = ' '
                self._bombmatrix[x+1][y-i] = ' '

        for i in range(1,5):
            if(self.up_cond_bomb(x-i,y) == 1 and x >= 2):
                self._bombmatrix[x-i][y] = ' '
                self._bombmatrix[x-i][y+1] = ' '
                self._bombmatrix[x-i][y+2] = ' '
                self._bombmatrix[x-i][y+3] = ' '

        for i in range(0,4):
            if(self.down_cond_bomb(x+i,y) == 1 and x <= 30):
                self._bombmatrix[x+2+i][y] = ' '
                self._bombmatrix[x+2+i][y+1] = ' '
                self._bombmatrix[x+2+i][y+2] = ' '
                self._bombmatrix[x+2+i][y+3] = ' '

            

    def enemy_print(self,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                self._bombmatrix[i][j] = 'E'

                
    def walls_print(self):

        x = random.randrange(2,25,2)
        y = random.randrange(4,57,4)
        if (x%4 == 0 or y%8 == 0):
            self.walls(x+2,y+4)

            
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
            

    def bomb_rt_cond(self,x,y):
    
        for i in range(0,4):
            if(self.right_cond_bomb(x,y+i) == 1):
                if(self._bombmatrix[x][y+4+i] == 'E' or self._bombmatrix[x+1][y+4+i] == 'E'):
                    return True
        return False
            
    def bomb_lt_cond(self,x,y):
        
        for i in range(1,5):
            if(self.left_cond_bomb(x,y-i) == 1):
                if(self._bombmatrix[x][y-i] == 'E' or self._bombmatrix[x+1][y-i] == 'E'):
                    return True
        return False

    def bomb_up_cond(self,x,y):
        
        for i in range(1,5):
            if(self.up_cond_bomb(x-i,y) == 1):
                if(self._bombmatrix[x-i][y] == 'E' or self._bombmatrix[x-i][y+1] == 'E' or self._bombmatrix[x-i][y+2] == 'E' or self._bombmatrix[x-i][y+3] == 'E'):
                    return True
        return False

    def bomb_dn_cond(self,x,y):

        for i in range(0,4):
            if(self.down_cond_bomb(x+i,y) == 1):
                if(self._bombmatrix[x+2+i][y] == 'E' or self._bombmatrix[x+2+i][y+1] == 'E' or self._bombmatrix[x+2+i][y+2] == 'E' or self._bombmatrix[x+2+i][y+3] == 'E'):
                    return True
        return False

    def enemy_dn_cond(self,x,y):
        
        for i in range(0,4):
            if(self._bombmatrix[x+2][y+i] == '^'):
                return True
            else:
                return False

    def enemy_up_cond(self,x,y):

        for i in range(0,4):
            if(self._bombmatrix[x-1][y+i] == '^'):
                return True
            else:
                return False

    def enemy_rt_cond(self,x,y):

        for i in range(0,2):
            if(self._bombmatrix[x+i][y+4] == '^'):
                return True
            else:
                return False

    def enemy_lt_cond(self,x,y):

        for i in range(0,2):
            if(self._bombmatrix[x+i][y-1] == '^'):
                return True
            else:
                return False

    def bomb_kills_enemy(self,x,y):

        if self.enemy_rt_cond(x,y) or (self.enemy_lt_cond(x,y)) or (self.enemy_up_cond(x,y)) or self.enemy_dn_cond(x,y):
            self._flag = 1
            return 1
        else:
            return 0
     

    
