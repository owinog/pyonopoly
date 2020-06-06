#project started on 22 may 2020
import random
import time

#=======================================================================

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
chosen_chances = []
chosen_chests = []

players = []
#Bank
bank={'houses':32,'hotels':12}

#===== Custom Funcitons ===============================================

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

#defining the cost per house
'''def house_price(landColor):
    if landColor == 'brown' or landColor == 'l blue':
        bhouse_price = 50
    elif landColor == 'pink' or landColor == 'orange':
        bhouse_price = 100
    elif landColor == '''

#=======================================================================

#Get slots details
slots = open('slots.txt', 'r')
slots_list = slots.readlines()
slots.close()
#removing the '\n' from the list
slots_list = [s.rstrip() for s in slots_list]

#=======================================================================

# creating player profiles
noOfPlayers = int(input('Enter the number of players... '))
for player in range(1, (noOfPlayers+1)):
    playername = input('Enter player '+str(player)+"'s name...")
    players.append(playername)
    globals()[playername] = {'position': 0,'balance': 1500, 'ownedProperties': [],'doubles':0,'jail':False,'jailKeys':0}

print('Welcome to Pyonopoly.\n the Game has started')

#=======================================================================

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

 #=======================================================================     
      
            # defining the slots according to the positions
            current_property = slots_list[position-1]
            property_details = current_property.split(',')

            unbuyable = [0,2,4,7,10,17,20,22,30,33,36,38,40]

            slotType = property_details[1]
            if position not in unbuyable:
                name = property_details[2]
                rent = int(property_details[3])
                mortgage = int(property_details[4])

#========================================================================

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

#========================================================================

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

#========================================================================

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
