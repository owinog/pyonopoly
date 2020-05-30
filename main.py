#project started on 22 may 2020
import random
import time

game = True
end_turn = True
jail = False
doubles = 0
position = 0
posCounter = 0
actionKey = ''
dice1 = 0
dice2 = 0
rolled_total = 0
players = []
chosen_chances = []
chosen_chests = []

#--delay function--
def delayer():
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)

#----roll function---------
def roll():
    global dice1
    global dice2
    global rolled_total
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolled_total = dice1+dice2
    print('dice1:', dice1, 'dice2:', dice2, 'total:', rolled_total)

#---action function----
def call_action():
    global actionKey
    actionKey = input('')

#Generate random order of chance cards from the chance_cards.txt file
def random_chances():
    global chosen_chances
    chance_cards = open('chance_cards.txt', 'r')
    lines = chance_cards.readlines()
    while len(chosen_chances) != len(lines):
        the_choice = random.choice(lines).strip('\n')
        while the_choice not in chosen_chances:
            chosen_chances.append(the_choice)

#Generate random order of community chest cards from the chest_cards.txt file
def random_chests():
    global chosen_chests
    chest_cards = open('chest_cards.txt', 'r')
    lines = chest_cards.readlines()
    while len(chosen_chests) != len(lines):
        the_choice = random.choice(lines).strip('\n')
        while the_choice not in chosen_chests:
            chosen_chests.append(the_choice)

# creating player profiles
noOfPlayers = int(input('Enter the number of players... '))
for player in range(1, (noOfPlayers+1)):
    playername = input('Enter player '+str(player)+"'s name...")
    players.append(playername)
    globals()[playername] = {'position': 0,'balance': 1500, 'ownedProperties': [],'doubles':0,'jail':False,'jailKeys':0}

print('Welcome to monopoly.\n the Game has started')

while end_turn:

    # Changing the player
    for player in range(1, (noOfPlayers+1)):
        print(str(players[player-1])+"'s turn")

# the dictionary of the current player ---> globals()[players[player-1]]
        current_player = globals()[players[player-1]]
        
        #resetting the actionKey
        actionKey = ''

        #shifting players jail status
        jail = current_player['jail']
        if not(jail):

            # rolling the dice
            print('rolling...')
            delayer()
            roll()
            
            #shifting the position value for each player
            posCounter = current_player['position']
            posCounter += rolled_total
            current_player['position'] = posCounter
            
            #-----paying 200 for passing GO------
            if posCounter >= 40:
                posCounter -= 40
                print('You passed go and obtained 200')
                balance = current_player['balance']
                print('adding 200')
                balance += 200
                current_player['balance'] = balance
                print('balance is',current_player['balance'])
            
            position = posCounter

            # Slots in positions
            if position == 1:
                slotType = 'Property'
                landColor = 'brown'
                value = 60
                deed = {'name':'Old Kent Road','rent':2,}

            if position == 2:
                slotType = 'Community Chest'

            if position == 3:
                slotType = 'Property'
                landColor = 'brown'
                value = 60
                deed = {'name':'Whitechapel Road','rent':}

            if position == 4:
                slotType = 'Tax'

            if position == 5:
                slotType = 'Railroad'
                value = 200

            if position == 6:
                slotType = 'Property'
                landColor = 'l blue'
                value = 100
                deed = {'name':'The Angel Islington','rent':}

            if position == 7:
                slotType = 'Chance'

            if position == 8:
                slotType = 'Property'
                landColor = 'l blue'
                value = 100
                deed = {'name': 'Euton Road', 'rent':}

            if position == 9:
                slotType = 'Property'
                landColor = 'l blue'
                value = 120
                deed = {'name': 'Pentonville Road', 'rent':}

            if position == 10:
                slotType = 'Just Visiting Jail '

            if position == 11:
                slotType = 'Property'
                landColor = 'purple'
                value = 140
                deed = {'name':'Pall Mall','rent':}

            if position == 12:
                slotType = 'Eleectricity Board'
                value = 150

            if position == 13:
                slotType = 'Property'
                landColor = 'purple'
                value = 140
                deed = {'name':'Whitehall','rent':}

            if position == 14:
                slotType = 'Property'
                landColor = 'purple'
                value = 160
                deed = {'name':'Northumberland Avenue','rent':}

            if position == 15:
                slotType = 'Railroad'
                value = 200

            if position == 16:
                slotType = 'Property'
                landColor = 'orange'
                value = 180
                deed = {'name':'Bow Street','rent':}

            if position == 17:
                slotType = 'Community Chest'

            if position == 18:
                slotType = 'Property'
                landColor = 'orange'
                value = 180
                deed = {'name':'Malborough Street','rent':}

            if position == 19:
                slotType = 'Property'
                landColor = 'orange'
                value = 200
                deed = {'name':'Vine Street','rent':}

            if position == 20:
                slotType = 'Free Parking'

            if position == 21:
                slotType = 'Property'
                landColor = 'red'
                value = 220
                deed = {'name':'Strand','rent':}

            if position == 22:
                slotType = 'Chance'

            if position == 23:
                slotType = 'Property'
                landColor = 'red'
                value = 220
                deed = {'name':'Fleet Street','rent':}

            if position == 24:
                slotType = 'Property'
                landColor = 'red'
                value = 240
                deed = {'name':'Trafalgar Square','rent':}

            if position == 25:
                slotType = 'Railroad'
                value = 200

            if position == 26:
                slotType = 'Property'
                landColor = 'yellow'
                value = 260
                deed = {'name':'Leicester Square','rent':}

            if position == 27:
                slotType = 'Property'
                landColor = 'yellow'
                value = 260
                deed = {'name':'Conventry Street','rent':}

            if position == 28:
                slotType = 'Water Works'
                value = 150

            if position == 29:
                slotType = 'Property'
                landColor = 'yellow'
                value = 280
                deed = {'name':'Piccadilly','rent':}

            if position == 30:
                slotType = 'Go to Jail'

            if position == 31:
                slotType = 'Property'
                landColor = 'green'
                value = 300
                deed = {'name':'Regent Street','rent':}

            if position == 32:
                slotType = 'Property'
                landColor = 'green'
                value = 300
                deed = {'name':'Oxford Street','rent':}

            if position == 33:
                slotType = 'Community Chest'

            if position == 34:
                slotType = 'Property'
                landColor = 'green'
                value = 320
                deed = {'name':'Bond Street','rent':}

            if position == 35:
                slotType = 'Railroad'
                value = 200

            if position == 36:
                slotType = 'Chance'

            if position == 37:
                slotType = 'Property'
                landColor = 'd blue'
                value = 350
                deed = {'name':'Park Lane','rent':}

            if position == 38:
                slotType = 'Tax'

            if position == 39:
                slotType = 'Property'
                landColor = 'd blue'
                value = 400
                deed = {'name':'Mayfair','rent':}

            if position == 40:
                slotType = 'Go'

            # showing details of the landed slot and calling actions
            print('You landed on the slot', position)
            print('Slot type: ', slotType)

            # Calling for action till the turn end
            '''
            actions...
            End turn - e

            '''
            while actionKey != 'e':

                #for properties
                if slotType == 'Property':
                    print('Do you want to see the deed?(y/n)')
                    call_action()
                    if actionKey == 'y':
                        # show deed
                        pass

                
                #for community chests
                if slotType == 'Community Chest':
                    if len(chosen_chests)==0:
                        random_chests()
                    print(chosen_chests[0])
                    chosen_chests.pop(0)

                #for Chances
                if slotType == 'Chance':
                    if len(chosen_chances) == 0:
                        random_chances()
                    print(chosen_chances[0])
                    chosen_chances.pop(0)

                #for railroads
                if slotType == 'Railroad':
                    call_action()

                #stopped at taxes
                if slotType == 'Tax':
                    if position == 4:
                        current_player['balance'] = current_player['balance']-200
                    else:
                        current_player['balance'] = current_player['balance']-100
                    
                    #display the remaining balance
                    print('you paid the Tax.. the balance is',current_player['balance'])

                #stopped at water works
                if slotType == 'Water Works':
                    call_action()

                #stopped at electricity board
                if slotType == 'Electicity Board':
                    call_action()

                #stopped at go to jail
                if slotType == 'Go to Jail':
                    jail = True
                    break
                
            #------if a player rolls a double---------
            #shifting players no of doubles
            doubles = current_player['doubles']
            if dice1 == dice2:
                delayer()
                print('You landed a Double')
                doubles+=1
            else:
                doubles=0

            if doubles == 3:
                jail = True
                print('You landed 3 doubles in a row') 

            current_player['doubles'] = doubles

        #-----send to jail--------
        if jail:
            position = 10
            print('Go to jail')
            actionKey = input('Do you want to try for a Double or bail out by paying 50?(d/b)')
            if actionKey == 'd':
                print('rolling...')
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                if dice1 == dice2:
                    jail = False
                else:
                    print("You couldn't land a double, your turns ends.")
                
        current_player['jail'] = jail
