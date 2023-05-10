tools = [
    {
        "type": "teeth",
        "profit": 1,
    },
    {
        "type": "scissors",
        "profit": 5,
    },
    {
        "type": "push lawnmover",
        "profit": 50,
    },
    {
        "type": "modern lawnmover",
        "profit": 100,
    },
    {
        "type": "starving students",
        "profit": 250,
    }
]

myTools = ''

money_earned = 0
account_balance = [0]

def purchase_teeth():
    global money_earned, account_balance, myTools
    print('Do you have your teeth? Let\'s start cutting a lawn and get a $1 per day! (yes/no)')
    for n in range (5): # loop through a range of values 0 to 4
        if account_balance[0]  < 5:
            money_earned += 1
            account_balance.insert(0, money_earned) # insert money_earned value at index 0
            myTools = tools[0]["type"] # find tools by index 0 and the key "type"
            print(f"Congrats! You've earned ${account_balance[0]} cutting lawns with your teeth!")
        else:
            purchase_rusty_scissors()

purchase_teeth()

def purchase_rusty_scissors():
    global money_earned, account_balance, myTools
    if account_balance[0] == 5:
        print(f"Start cutting lawns with {tools[1]['type']} and earn ${tools[1]['profit']}!")
        account_balance[0] -= 5
        print(f'You\'ve succesfully purchased a pair of rusty scissors. Now you have ${account_balance[0]} on your account')
        myTools = tools[1]["type"]
    elif account_balance[0] < 5:
        print(f'You have ${account_balance}. Keep working!')
    elif myTools == tools[1]["type"]:
        print('You can purchase rusty scissors only once!')

purchase_rusty_scissors()