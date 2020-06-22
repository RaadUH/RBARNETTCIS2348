dict1 = dict()
for i in range(5):
    print("Enter player {}'s jersey number:".format(i+1))
    jersey_no = int(input())
    print("Enter player {}'s rating:".format(i+1))
    jersey_rating = int(input())
    dict1[jersey_no] = jersey_rating
    print()
print('ROSTER')
for k in sorted(dict1.keys()):
    print("Jersey number: {}, Rating: {}".format(k,dict1[k]))
menu = "MENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n"
choice=''
while(choice!='q'):
    print()
    print(menu)
    print("Choose an option:")
    choice = input()
    if(choice=='a'):
        print("\Enter a new player's jersey number:")
        jersey_no = int(input())
        print("Enter the player's rating:")
        jersey_rating = int(input())
        dict1[jersey_no] = jersey_rating
    elif(choice=='d'):
        print("Enter a jersey number:")
        j_number = int(input())
        del dict1[j_number]
    elif(choice=='u'):
        print("\Enter a jersey number:")
        jersey_no = int(input())
        print("Enter a new rating for player:")
        jersey_rating = int(input())
        dict1.update({jersey_no:jersey_rating})
    elif(choice=='r'):
        print("Enter a rating:")
        rate = int(input())
        print("ABOVE {}".format(rate))
        dict2 = {}
        for k,v in dict1.items():
            if(v>rate):
                dict2[k] = v
        for k in sorted(dict2.keys()):
            print("Jersey number: {}, Rating: {}".format(k,dict2[k]))
    elif(choice=='o'):
        print('ROSTER')
        for k in sorted(dict1.keys()):
            print("Jersey number: {}, Rating: {}".format(k,dict1[k]))
