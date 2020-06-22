# Raad Barnett 1231583
class Team:
    def __init__(self):
        self.team_name = "none"
        self.team_wins = 0
        self.team_losses = 0
    def get_win_percentage(self):
        return self.team_wins/(self.team_wins+self.team_losses)
obj = Team()
obj.team_name = input()
obj.team_wins = int(input())
obj.team_looses = int(input())

if(obj.get_win_percentage() >= 0.5):
    print("Congratulations, Team {} has a winning average!".format(obj.team_name))
else:
    print("Team {} has a losing average.".format(obj.team_name))
