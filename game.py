from random import randint
import os


def menu():
    print 'Welcome!'
    print 'When playing do not type anything in caps!'
    begin = raw_input ('Type begin to begin playing!')

    if begin == 'begin':
        createPlayer()

    else:
        print "invalid option please type begin"
        menu()

def createPlayer():
    print "What would you like your players name to be?"
    name = raw_input()
    print "Welcome",name,"what class would you like to be?"
    print 'archer / knight / mage'
    clas = raw_input()

    gold = 0

    if clas == 'archer':
        hp = 20
        mp = 20
        print "HP =",hp
        print "MP =",mp


    elif clas == 'knight':
        hp = 30
        mp = 15
        print "HP =",hp
        print "MP =",mp


    elif clas == 'mage':
        hp = 20
        mp = 30
        print "HP =",hp
        print "MP =",mp

    else:
        print 'Try again'
        createPlayer()



def random_monster(diff):
    y = randint(1,10)
    return diff * y

def random_win(win):
    z = randint(5,15)
    return win * z

def play():
    global hp
    global mp
    global gold
    level = mp + hp
    print hp
    print mp
    print gold
    print 'Enter your dificulty for your first battle, the higher the number the harder it is and the more you receive from winning'
    diff = int(raw_input())
    dificulty = random_monster(diff)
    print' Your dificulty is',dificulty
    print'Lets begin with your first battle'

    if dificulty > level:
        winn = randint(5,10)
        winnn = random_win(winn)
        if winnn > dificulty:
            print 'You won!'
            goldwin
            hp = hp + 5
            mp = mp + 5
            gold = gold + 
            play()

        else:
            print 'You lost!'
            hp = hp - 5
            mp = mp - 5
            play()

menu()
play()
