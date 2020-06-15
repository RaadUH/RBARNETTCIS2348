def exact_change(user_total):
    if(user_total==0):
        print('no change')
    else:
        num_dollars = num_quarters = num_dimes = num_nickels = num_pennies = 0
        if(user_total//100!=0):
            a = user_total//100
            user_total -= a*100
            num_dollars += a
            if(num_dollars>1):
                print(num_dollars,'dollars')
            else:
                print(num_dollars,'dollar')
        if(user_total//25!=0):
            a = user_total//25
            user_total -= a*25
            num_quarters += a
            if(num_quarters>1):
                print(num_quarters,'quarters')
            else:
                print(num_quarters,'quarter')
        if(user_total//10!=0):
            a = user_total//10
            user_total -= a*10
            num_dimes += a
            if(num_dimes>1):
                print(num_dimes,'dimes')
            else:
                print(num_dimes,'dime')
        if(user_total//5!=0):
            a = user_total//5
            user_total -= a*5
            num_nickels += a
            if(num_nickels>1):
                print(num_nickels,'nickels')
            else:
                print(num_nickels,'nickel')
        if(user_total//1!=0):
            num_pennies += user_total
            if(num_pennies>1):
                print(num_pennies,'pennies')
            else:
                print(num_pennies,'penny')

user_total = int(input())
exact_change(user_total)
