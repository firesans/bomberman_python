#!/usr/lib/python
from board import *
from person import *
from enemy import *
ene = enemy()


class bomb(person):

    def __init__(self):
        person.__init__(self)
        self._b1 = 2
        self._b2 = 4
        self._score = 0

    def bomb(self,b,x,y):

        b._bombmatrix[x][y] = '['
        b._bombmatrix[x][y+1] = '0'
        b._bombmatrix[x][y+2] = '0'
        b._bombmatrix[x][y+3] = ']'
        b._bombmatrix[x+1][y] = '['
        b._bombmatrix[x+1][y+1] = '0'
        b._bombmatrix[x+1][y+2] = '0'
        b._bombmatrix[x+1][y+3] = ']'

    def erase_bomb(self,b,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                b._bombmatrix[i][j] = ' '

    def up_cond_bomb(self,b,x,y):

        if(b._matrix[x-1][y] == '#' or b._matrix[x-1][y+1] == '#' or b._matrix[x-1][y+2] == '#' or b._matrix[x-1][y+3] == '#' ):
            return 0;
        else:
            #b._flag = 1
            return 1;

    def down_cond_bomb(self,b,x,y):

        if(b._matrix[x+2][y] == '#' or  b._matrix[x+2][y+1] == '#' or b._matrix[x+2][y+2] == '#' or b._matrix[x+2][y+3] == '#' and x+2<=33):
            return 0;
        else:
            #b._flag = 2
            return 1;

    def right_cond_bomb(self,b,x,y):
        if(b._matrix[x][y+4] == '#' or b._matrix[x+1][y+4] == '#'):
            return 0;

        else:
            #b._flag = 3
            return 1;

    def left_cond_bomb(self,b,x,y):

        if(b._matrix[x][y-1] == '#' or b._matrix[x+1][y-1] == '#'):
            return 0;
        else:
           # b._flag = 4
            return 1;


    def print_bombreaction(self,b,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                b._bombmatrix[i][j] = '^'

        for i in range(0,4):
            if(self.right_cond_bomb(b,x,y+i) == 1):
                b._bombmatrix[x][y+4+i] = '^'
                b._bombmatrix[x+1][y+4+i] = '^'
            else:
                break

        for i in range(1,5):
            if(self.left_cond_bomb(b,x,y-i) == 1):
                b._bombmatrix[x][y-i] = '^'
                b._bombmatrix[x+1][y-i] = '^'
            else:
                break

        for i in range(1,5):
            if(self.up_cond_bomb(b,x-i,y) == 1 and x >= 2):
                b._bombmatrix[x-i][y] = '^'
                b._bombmatrix[x-i][y+1] = '^'
                b._bombmatrix[x-i][y+2] = '^'
                b._bombmatrix[x-i][y+3] = '^'
            else:
                break

        for i in range(0,4):
            if(x == 30 and i == 2):
                break
            if(self.down_cond_bomb(b,x+i,y) == 1):
                b._bombmatrix[x+2+i][y] = '^'
                b._bombmatrix[x+2+i][y+1] = '^'
                b._bombmatrix[x+2+i][y+2] = '^'
                b._bombmatrix[x+2+i][y+3] = '^'
            else:
                break

    def erase_bombdebris(self,b,x,y):

        for i in range(x,x+2):
            for j in range(y,y+4):
                b._bombmatrix[i][j] = ' '

        for i in range(0,4):
            if(self.right_cond_bomb(b,x,y+i) == 1):
                b._bombmatrix[x][y+4+i] = ' '
                b._bombmatrix[x+1][y+4+i] = ' '

        for i in range(1,5):
            if(self.left_cond_bomb(b,x,y-i) == 1):
                b._bombmatrix[x][y-i] = ' '
                b._bombmatrix[x+1][y-i] = ' '

        for i in range(1,5):
            if(self.up_cond_bomb(b.x-i,y) == 1 and x >= 2):
                b._bombmatrix[x-i][y] = ' '
                b._bombmatrix[x-i][y+1] = ' '
                b._bombmatrix[x-i][y+2] = ' '
                b._bombmatrix[x-i][y+3] = ' '

        for i in range(0,4):
            if(self.down_cond_bomb(b,x+i,y) == 1 and x <= 30):
                b._bombmatrix[x+2+i][y] = ' '
                b._bombmatrix[x+2+i][y+1] = ' '
                b._bombmatrix[x+2+i][y+2] = ' '
                b._bombmatrix[x+2+i][y+3] = ' '

    def timebomb(self,b,ene):

        #print(self._e1,self._e2)
        self.erase_bomb(b,self._b1,self._b2)
        self.print_bombreaction(b,self._b1,self._b2)
        ene.bomb_kills_enemy1(b)
        ene.bomb_kills_enemy2(b)
        t = threading.Timer(1.0,self.bomb_clear_debris,args=(b,))
        t.start()

    def bomb_dropping(self,b,p):

        self.bomb(b,p.get_man_x(),p.get_man_y())
        self._b1 = p.get_man_x()
        self._b2 = p.get_man_y()

        os.system("c")
        #b.printboard()

    def bomb_clear_debris(self,b):

        b.erase_bombdebris(self._b1,self._b2)

    def bomb_rt_cond(self,b,x,y):

        for i in range(0,4):
            if(self.right_cond_bomb(b,x,y+i) == 1):
                if(b._bombmatrix[x][y+4+i] == '%' or b._bombmatrix[x+1][y+4+i] == '%'):
                    return True
        return False

    def bomb_lt_cond(self,b,x,y):

        for i in range(1,5):
            if(self.left_cond_bomb(b,x,y-i) == 1):
                if(b._bombmatrix[x][y-i] == '%' or b._bombmatrix[x+1][y-i] == '%'):
                    return True
        return False

    def bomb_up_cond(self,b,x,y):

        for i in range(1,5):
            if(self.up_cond_bomb(b,x-i,y) == 1):
                if(b._bombmatrix[x-i][y] == '%' or b._bombmatrix[x-i][y+1] == '%' or b._bombmatrix[x-i][y+2] == '%' or b._bombmatrix[x-i][y+3] == '%'):
                    return True
        return False

    def bomb_dn_cond(self,b,x,y):

        for i in range(0,4):
            if( x== 30 and i == 2):
                break
            if (x == 29 and i == 3):
                break
            if(self.down_cond_bomb(b,x+i,y) == 1):
                if(b._bombmatrix[x+2+i][y] == '%' or b._bombmatrix[x+2+i][y+1] == '%' or b._bombmatrix[x+2+i][y+2] == '%' or b._bombmatrix[x+2+i][y+3] == '%'):
                    return True
        return False

    def burst_walls(self,b):

        if self.bomb_up_cond(b,self._b1,self._b2) or self.bomb_dn_cond(b,self._b1,self._b2) or self.bomb_lt_cond(b,self._b1,self._b2) or self.bomb_rt_cond(b,self._b1,self._b2):
            self._score = self._score + 20
            return self._score
        else:
            return self._score
