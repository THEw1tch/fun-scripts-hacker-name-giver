


'''
                            Made by the w!tch herself

  Wanted to make all you cool cats take up the legend of the hackers listed here. 
  Each one has their back story from movies, tv shows, games, and most important 
  of all... real life. Yes, Most of these come from real life people who have 
  made theirmark on the world. Will you take up the mantle of their hacker names 
  and continue their legacy?

'''

import random as r
import time as t
import os, sys

# Hacker names to choose from.
hacker_Names = ['Neo','Trinity','Cipher',
                'Apoc','Mouse','Morpheus',
                'Kid','retr0','Hawt Sauce',
                'Sitara','Wrench','lenni',
                'Elon','T-Bug','BedBug',
                'Badboy17','Mobly','Trenton',
                'Dave_of_Spades','Phiber Optik','Kayla',
                'Tflow','ioerror','Dead Lord',
                'Kingpin','Romanpoet','Mendax',
                'weev','The Mentor','Red box Chili Pepper',
                'Captain Crunch','Phoenix','ESR',
                'hunter','Acidus','geohot',
                'Highrise Joe','hagbard','Lord Digital']

newName = r.choice(hacker_Names)
key = "y"

# Function that spits our your new name.
def newday():
    os.system('cls||clear')
    t.sleep(1)
    print("Hello, Friend")
    t.sleep(2)
    print("\nAre you ready to know your new name?: (y/n)\n")
    answer = input()
    if key == answer:
        t.sleep(1)
        print("\nOnce you know it... remember it.")
        t.sleep(5)
        os.system('cls||clear')
        t.sleep(1)
        print("\nWe won\'t remember for you")
        t.sleep(3)
        os.system('cls||clear')
        t.sleep(1)
        print("\nYour new name is now...\n\n")
        t.sleep(3)
        print("--------------------------------\n")
        print("           " + newName + "\n")
        print("--------------------------------\n\n")
        t.sleep(13)
        os.system('cls||clear')
    else:
        sys.exit(0)

newday()

# This print gives the full list.
#print(*hacker_Names, sep = "\n")




