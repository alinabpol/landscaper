tools = [{
    'type': 'teeth',
    'profit': 1
}]

myTools = ''

money_earned = 0
account_balance = [0]

def purchase_teeth():
    global money_earned, account_balance, myTools
    print('Do you have your teeth? Let\'s start cutting a lawn and get a $1 per day! (yes/no)')
    for n in range (5):
        if account_balance[0]  < 5:
            money_earned += 1
            account_balance.insert(0, money_earned)
            myTools = tools[0]["type"]
            print(f"Congrats! You've earned ${account_balance[0]} cutting lawns with your teeth!")

purchase_teeth()

