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

my_tools = ''

money_earned = 0
account_balance = [0]

def purchase_teeth():
    global money_earned, account_balance, my_tools
    print('Do you have your teeth? Let\'s start cutting a lawn and get a $1 per day! (yes/no)')
    for n in range (5): # loop through a range of values 0 to 4
        if account_balance[0]  < 5:
            money_earned += 1
            account_balance.insert(0, money_earned) # insert money_earned value at index 0
            my_tools = tools[0]["type"] # find tools by index 0 and the key "type"
            print(f"Congrats! You've earned ${account_balance[0]} cutting lawns with your teeth!")
        else:
            purchase_rusty_scissors()

purchase_teeth()

def purchase_rusty_scissors():
    global money_earned, account_balance, my_tools
    if account_balance[0] == 5:
        print(f'Congrats, you\'ve earned ${account_balance[0]}, and now you can buy a pair of rusty scissors! Press "Ok" to proceed with the purchase.')
        account_balance[0] -= 5
        print(f'You\'ve succesfully purchased a pair of rusty scissors. Now you have ${account_balance[0]} on your account')
        my_tools = tools[1]["type"]
    elif account_balance[0] < 5:
        print(f'You have ${account_balance}. Keep working!')
    elif my_tools == tools[1]["type"]:
        print('You can purchase rusty scissors only once!')

purchase_rusty_scissors()

def use_scissors():
        global money_earned, account_balance, my_tools
        print(f"Start cutting lawns with {tools[1]['type']} and earn ${tools[1]['profit']}!")
        for b in range(5):
            if account_balance[0] < 25 and my_tools == tools[1]["type"]:
                money_earned += 5
                account_balance.insert(0, money_earned)
                print(f'You\'ve earned ${account_balance[0]} cutting lawns with scissors!')
            else:
                print('You can buy more tools, check it out!')
          
use_scissors()

def purchase_lawnmover():
    global money_earned, account_balance, my_tools
    if account_balance[0] == 25:
        print(f'Congrats, you\'ve earned ${account_balance[0]}, and now you can buy a {tools[2]["type"]}! Press "Ok" to proceed with the purchase.')
        account_balance[0] -= 25
        money_earned -=25
        print(f'You\'ve succesfully purchased a {tools[2]["type"]}. Now you have ${account_balance[0]} on your account')
        my_tools = tools[2]["type"]
    elif account_balance[0] < 25:
        print(f'You have ${account_balance}. Keep working!')
    elif my_tools == tools[2]["type"]:
        print(f'You can purchase {tools[2]["type"]} only once!')

purchase_lawnmover()

def use_lanmower():
        global money_earned, account_balance, my_tools
        print(f"Start cutting lawns with {tools[2]['type']} and earn ${tools[2]['profit']}!")
        for b in range(5):
            if account_balance[0] < 250 and my_tools == tools[2]["type"]:
                money_earned += 50
                account_balance.insert(0, money_earned)
                print(f"You've earned ${account_balance[0]} cutting lawns with {tools[2]['type']}!")
            else:
                print('You can buy more tools, check it out!')
          
use_lanmower()

def purchase_modern_lawnmover():
    global money_earned, account_balance, my_tools
    if account_balance[0] == 250:
        print(f'Congrats, you\'ve earned ${account_balance[0]}, and now you can buy a {tools[3]["type"]}! Press "Ok" to proceed with the purchase.')
        account_balance[0] -= 250
        money_earned -= 250
        print(f'You\'ve succesfully purchased a {tools[3]["type"]}. Now you have ${account_balance[0]} on your account')
        my_tools = tools[3]["type"]
    elif account_balance[0] < 250:
        print(f'You have ${account_balance}. Keep working!')
    elif my_tools == tools[3]["type"]:
        print(f'You can purchase {tools[3]["type"]} only once!')

purchase_modern_lawnmover()

def use_modern_lanmower():
        global money_earned, account_balance, my_tools
        print(f"Start cutting lawns with {tools[3]['type']} and earn ${tools[3]['profit']}!")
        for b in range(5):
            if account_balance[0] < 500 and my_tools == tools[3]["type"]:
                money_earned += 100
                account_balance.insert(0, money_earned)
                print(f"You've earned ${account_balance[0]} cutting lawns with {tools[3]['type']}!")
            else:
                print('You can buy more tools, check it out!')
          
use_modern_lanmower()

def hire_students():
    global money_earned, account_balance, my_tools
    if account_balance[0] == 500:
        print(f'Congrats, you\'ve earned ${account_balance[0]}, and now you can hire {tools[4]["type"]}! Press "Ok" to proceed with the purchase.')
        account_balance[0] -= 500
        money_earned -= 500
        print(f'You\'ve succesfully hired {tools[4]["type"]}. Now you have ${account_balance[0]} on your account')
        my_tools = tools[4]["type"]
    elif account_balance[0] < 500:
        print(f'You have ${account_balance}. Keep working!')
    elif my_tools == tools[4]["type"]:
        print(f'You can purchase {tools[4]["type"]} only once!')

hire_students()

def work_with_students():
        global money_earned, account_balance, my_tools
        print(f"Start cutting lawns with {tools[4]['type']} and earn ${tools[4]['profit']}!")
        for b in range(5):
            if account_balance[0] < 1000 and my_tools == tools[4]["type"]:
                money_earned += 250
                account_balance.insert(0, money_earned)
                print(f"You've earned ${account_balance[0]} cutting lawns with {tools[4]['type']}!")
            else:
                print(f'Congrats, you\'ve earned ${account_balance[0]} and you won this game!! Whoo!')
          
work_with_students()