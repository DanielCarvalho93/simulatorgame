from tracemalloc import DomainFilter
import pygame
from pygame import mixer
import cmd
import textwrap
import sys
import os
import time
import random
import pandas as pd
from IPython.display import display
from random import choice
import playsound
from playsound import playsound



pygame.init()
soundObj = mixer.Sound(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\UEFA Champions League - Full Version.ogg')
soundObj.play()
pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\UEFA Champions League - Full Version.ogg')
pygame.mixer.music.play()
screen_width = 1000


## Generating Funtions ###
### TEXT DELAY ###
def waiting(t):
    time.sleep(t)
    print('.')
    print()
    time.sleep(t)
    print('.')
    print()
    time.sleep(t)
    print('.')
    print()

def talk_speed(dialog, speed):
    for character in dialog:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)

### Title Screen ###
def title_screen_selection():
    option = input('>   ')
    if option.lower() == ("play"):
        linebreak()
    elif option.lower() == ("quit"):
        sys.exit
    while option.lower() not in ["play", "quit"]:
        print("Please either enter the word play or the word quit")
        option = input('>   ')
        if option.lower() == ("play"):
            linebreak()
        elif option.lower() == ("quit"):
            sys.exit

def title_screen():
    os.system('clear')
    print()
    print()
    print()
    a = '***************************************\n'
    talk_speed(a, 0.02)
    b = '******** 5 VS 5 CHAMPIONS LEAGUE ******\n'
    talk_speed(b, 0.02)
    c = '***************************************\n'
    talk_speed(c, 0.02)
    d = '********  WHO WILL WIN TODAY... *******\n'
    talk_speed(d, 0.02)
    e = '                 -PLAY-                \n'
    talk_speed(e, 0.02)
    f = '                 -QUIT-                \n'
    talk_speed(f, 0.02)
    g = '       FOOTBALL MANAGER LIVE GAME      \n'
    talk_speed(g, 0.02)
    title_screen_selection()

def feelings(user):
    over_confidence = 0
    focused = 0
    choice3 = input('\n' + user + '\n'
        + """
                HOW ARE YOU FEELING?
                [0] MASSIVELY CONFIDENT
                [1] MORE THEN READY
                [2] NERVOUS
                [3] CONCENTRATED 
                """)
    if choice3 in ['0','1']:
        over_confidence -= 1
        return over_confidence
    else:
        focused += 1
        return focused


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

game_dict = {}

waiting(0.5)
title_screen()
line1 = 'Player 1, please input your name: '
talk_speed(line1, 0.02)
user_1 = input()
line2 = 'Player 2, please input your name: '
talk_speed(line2, 0.02)
user_2 = input()
print(user_1)
line3 = 'Please enter a name for your team: '
talk_speed(line3, 0.02)
team_name_1 = input()
print(user_2)
line4 = 'Please enter a name for your team: '
talk_speed(line4, 0.02)
team_name_2 = input()
feeling_1 = feelings(user_1)
feeling_2 = feelings(user_2)


game_dict[user_1] = team_name_1
game_dict[user_2] = team_name_2



players = pd.read_excel(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\Players.xlsx')


def total_points(plist):
    total=[]

    for el in plist:
        #players[players['Name'] == el].index[0]
        total.append(players.iloc[players[players['Name'] == el].index[0]]["Total Points"])
    return sum(total)



def home_advantage(lst):
    return total_points(lst) + 5



def player_pick_order(playerlist):
    player1_lst = []
    player2_lst = []
    poslist = ['GK', 'DEF', 'MID', 'WNG', 'ATK']
    for pos in poslist:
        posplayer = list(players[players['Position']== pos]['Name'])
        for i in range(2):
            print(playerlist[i] + ' Please choose your player ' + pos)
            for index,name in enumerate(posplayer):
                print(f"[{index}] {name}")
            chosen = int(input())
            
            if playerlist[i] == user_1:
                player1_lst.append(posplayer[chosen])
            else:
                player2_lst.append(posplayer[chosen])

            posplayer.pop(chosen)
    return player1_lst, player2_lst


def start_game(winning_name, winning_team,loosing_name,loosing_team):
    pass_text = [' passes it to ', ' crosses it in to ', 'puts up a wonderful pass to ', 'sends it through to ']
    shoot_text = [ 'With the header.. ' , ' Curls it towards the goal.. ' , ' Takes a shot.. ']
    goal = [' And its in!!!', 'Goooooooooooooooooooolaaaaaaaaaaaaaaaaaaaaçooooooooooo', 'And it hits the back of the net, what a goal!', 'Goal,goal,goal!', 'GOLOOOOO!']
    no_goal = [' Ahh just wide!!!', 'And he misses by a mile!!' , 'IT HITS THE POST AND BOUNCES BACK OUT!!', 'NO GOAL! HE SHOULD HAVE DONE BETTER..', 'UI,UI,UI, SO CLOSE!']

    
    my_team_score = 0
    opp_team_score = 0
    match_time = 0
    ref = "The ref blows the whistle and we're under way!\n"
    pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
    pygame.mixer.music.play()
    talk_speed(ref,0.02)
    while match_time < 8 :
        goal_or_not = random.random()
        whose_ball = random.random()
        if whose_ball < 0.50 :
            if goal_or_not < 0.2 :
                time.sleep(3)
                print("The ball is taken by {} {} {} {} ".format(random.choice(loosing_team[1:3]),random.choice(pass_text),random.choice(loosing_team[3:-1]),random.choice(shoot_text)))
                time.sleep(4)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play()
                print("{}".format(random.choice(goal)))
                opp_team_score += 1
                time.sleep(4)
                print(" It's {} {} ".format(str(my_team_score) , str(opp_team_score)))
                match_time += 1
            else :
                time.sleep(3)
                print("The ball is taken by {} {} {} {} ".format(random.choice(loosing_team[1:3]),random.choice(pass_text),random.choice(loosing_team[3:-1]),random.choice(shoot_text)))
                time.sleep(4)
                print("{}".format(random.choice(no_goal)))
                match_time += 1
        else :
            if goal_or_not >= 0.2 :
                    time.sleep(3)
                    print("{} {} {} {}".format(random.choice(winning_team[1:3]),random.choice(pass_text),random.choice(winning_team[3:-1]),random.choice(shoot_text)))
                    time.sleep(4)
                    pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                    pygame.mixer.music.play() 
                    print("{}".format(random.choice(goal)))
                    my_team_score += 1
                    time.sleep(4)
                    print(" it's {} {} ".format(str(my_team_score) , str(opp_team_score)))
                    match_time += 1
            else :
                    time.sleep(3)
                    print("{} {} {} {}".format(random.choice(winning_team[1:3]),random.choice(pass_text),random.choice(winning_team[3:-1]),random.choice(shoot_text)))
                    time.sleep(4)
                    print("{}".format(random.choice(no_goal)))
                    time.sleep(4)
                    match_time += 1




weather = [' Its raining so much today..\n ', ' Its clear skies today, not one cloud in sight..\n ', 'Its a sunny day today here in Lisbon..\n ', 'Can you belive it, it is snowing here in Manchester..\n']
talk_speed(random.choice(weather),0.02)
time.sleep(2)
coin_flip_users = random.choice([user_1,user_2])
flip_txt = 'Flipping a coin to see who picks first..\n '
talk_speed(flip_txt, 0.05)
time.sleep(3)

end = "The ref blows for the final whistle and the game is over!\n"



def home_away(chooser):
    if chooser == user_1:
        choice1 = input('\n' + user_1 + '\n'
        + """
                Would you like to play at home or have first pick?
                [0] Home Advantage
                [1] First Pick 
                """)
        if choice1 == '1':
            print(user_2 + ' has home advantage, ' + user_1 + ' get ready to pick')
            p1list , p2list = player_pick_order([user_1,user_2])
            p1score = total_points(p1list) + feeling_1
            p2score = home_advantage(p2list) + feeling_2
            if p1score > p2score:
                start_game(team_name_1,p1list,team_name_2,p2list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('Congratulations on winning the champions league!!')
            elif p2score > p1score:
                start_game(team_name_2,p2list,team_name_1,p1list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('Congratulations on winning the champions league!!')
            else:
                start_game(team_name_1,p1list,team_name_2,p2list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('GAME OVER!')
        else:
            print(user_1 + ' has home advantage,' + user_2 + ' get ready to pick')
            p2list , p1list = player_pick_order([user_2,user_1])
            p2score = total_points(p2list) + feeling_2
            p1score = home_advantage(p1list) + feeling_1
            if p1score > p2score:
                start_game(team_name_1,p1list,team_name_2,p2list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('Congratulations on winning the champions league!!')
            elif p2score > p1score:
                start_game(team_name_2,p2list,team_name_1,p1list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('Congratulations on winning the champions league!!')
            else:
                start_game(team_name_1,p1list,team_name_2,p2list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('GAME OVER! ')
    elif coin_flip_users == user_2:
        choice1 = input('\n'+ user_2 +'\n' 
         + """
                Would you like to play at home or have first pick?
                [0] Home Advantage
                [1] First Pick 
                """)
        if choice1 == '1':
            print(user_1 + ' has home advantage, ' + user_2 + ' get ready to pick')
            p2list , p1list = player_pick_order([user_2,user_1])
            p2score = total_points(p2list) + feeling_2
            p1score = home_advantage(p1list) + feeling_1
            if p1score > p2score:
                start_game(team_name_1,p1list,team_name_2,p2list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('Congratulations on winning the champions league!!')
            elif p2score > p1score:
                start_game(team_name_2,p2list,team_name_1,p1list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('Congratulations on winning the champions league!!')
            else:
                start_game(team_name_1,p1list,team_name_2,p2list)
                print('GAME OVER! ')
        else:
            print(user_2 + ' has home advantage,' + user_1 + ' get ready to pick')
            p1list , p2list = player_pick_order([user_1,user_2])
            p1score = total_points(p1list) + feeling_1
            p2score = home_advantage(p2list) + feeling_2
            if p1score > p2score:
                start_game(team_name_1,p1list,team_name_2,p2list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('Congratulations on winning the champions league!!')
            elif p2score > p1score:
                start_game(team_name_2,p2list,team_name_1,p1list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('Congratulations on winning the champions league!!')
            else:
                start_game(team_name_1,p1list,team_name_2,p2list)
                pygame.mixer.music.load(r'C:\Users\Daniel Carvalho\Desktop\DataAnalysis\WEEK6\Project 5\referee-blowing-whistle-sound-effect.mp3')
                pygame.mixer.music.play() 
                talk_speed(end,0.05)
                time.sleep(3)
                print('GAME OVER! ')
    return p1score, p2score







home_away(coin_flip_users)


