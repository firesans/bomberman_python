#!/usr/lib/python
from random import *
from board import *
from person import *
from bomb import *
from enemy import *

import sys

from termcolor import colored
import threading
from threading import Timer
import time
import os


def getchar():
    import tty
    import termios
    import sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():
    os.system("c")
    score = 0
    # clear command alias :: c
    b = board()
    # instance created
    b.initboard()
    # initialising the matrix
    # initial position of the bomber-man
    bomb_drop = bomb()
    enemy_attack = enemy()
    b.bomberman(2,4)
    enemy_attack.enemy_print(b,30,4)
    enemy_attack.enemy_print(b,2,60)
                                #b.enemy_print(30,60)
                                #putting balls in the game
    for i in range(15):
        b.walls_print()
                                # b.enemy_print(30,4)
                                # calling all the methods(for movement using person instance :p)
    p = person()
    b.printboard()              # printing the initial board :p
    in_x = 30
    in_y = 60
    level = 1
    lives = 3
    flag1 = 0
    flag2 = 0
    sco = 0

    # the function used for no parameters during blasting
    def reference():
        bomb_drop.timebomb(b,enemy_attack)

    while(lives > 0):

        #t_reaction = threading.Timer(3.0,reference)
        #t_cleaning = Timer(1.0,reference_clean)
        #score=sc.getScore()
        if(flag1 == 1):
            b.bomberman(2,4)
            p.change_parameter_man(2,4)
            flag1 = 0
            b.printboard()
        if(flag2 == 1):
            b.bomberman(2,4)
            p.change_parameter_man(2,4)
            flag2 = 0
            b.printboard()

        print "Level:"+str(level)
        print "Current score: "+str(enemy_attack.get_score()+sco)
        print "Enter your move (a/w/s/d/q):",
        flag = 0
        ch = getchar()

        enemy_attack.enemy1_movement(b)
        enemy_attack.enemy2_movement(b)

        if ch == 'q':

            os.system("")
            os.system("c")
            print "\nGame over!"
            print "Your final score is "+str(enemy_attack.get_score()+sco)+"\n"
            break

        elif ch == 'b':

            os.system('c')
            t_reaction = threading.Timer(3.0,reference)
            bomb_drop.bomb_dropping(b,p)
            b.printboard()
            os.system('c')
            sco = bomb_drop.burst_walls(b)
            t_reaction.start()
            b.printboard()

            #t_cleaning.start()

        else:
            p.move(b,ch)

        #t.cancel()
        #if(p.flag_value() == 0):
        #print("bomb killed")
        #b.enemy_print(30,4)
        #p.change_parameter_enemy(30,4)
        #os.system('c')
        #b.printboard()


        if(enemy_attack.enemy1_kills_man(b,p) == 1):
            flag1 = 1
        if(enemy_attack.enemy2_kills_man(b,p) == 1):
            flag2 = 1

        if flag1 == 1:
            os.system("c")
            lives = lives -1
            dead = 3-lives
            print "\nYOU LOST "+ str(dead) + " LIVEs!"
            #b.printboard()

        if flag2 == 1:
            os.system("c")
            lives = lives - 1
            dead = 3-lives
            print "\nYOU LOST "+str(dead) + "LIVEs!"

def main1():

    os.system('c')
    print colored('Welcome to BOMBERMAN\n','red',attrs=['bold'])
    print colored('PRESS','green'),colored('p','cyan',attrs=['bold']),colored('to play\n','green')
    print colored('click q to exit','red')

    print " "
    print colored('ENTER character(p/q):','cyan')
    c = getchar()
    #print colored(c,'blue',attrs=['bold'])

    if(c == 'p'):
        main()
    else:
        os.system('c')
        print colored('\nGame Over! and SCORE:0','blue',attrs=['bold'])


if __name__ == "__main__":

    # calling the main function
    main1()
