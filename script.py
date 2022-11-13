class Match:
    
                    
    def calculate_win(self, n, *T):
        global Winsum
        global WinTeamcount
        global ComparisonW
        #consecutive wins 
        for i in range (2,8-n):
            if T[i] == 0:
                i += 1
            if T[i] == 1:
                
                if T[i] == T[i+1]:
                    if ComparisonW == n-1:
                        
                        Winsum += T[1]
                        WinTeamcount += 1
                        print(T[0], "has", n ,"consecutive Win")
                        break
                    else:
                        ComparisonW += 1
                        
                        
    def calculate_loss(self, n, *T):
        global Losssum
        global LossTeamcount
        global ComparisonL
        #consecutive wins 
        for i in range (2,8-n):
            if T[i] == 0:
                i += 1
            if T[i] == 1:
                
                if T[i] == T[i+1]:
                    if ComparisonL == n-1:
                        
                        Losssum += T[1]
                        LossTeamcount += 1
                        print(T[0], "has", n ,"consecutive loss")
                        break
                    else:
                        ComparisonL += 1
                                           
                
                       
                        
            
n = int(input('Enter the number to find n consecutive Loss/Win: '))
Winsum=0
WinTeamcount=0
Losssum=0
LossTeamcount=0
ComparisonW=1
ComparisonL=1


T1 = ['GT', 20, 1, 1, 0, 0, 1]
Team1 = Match()
Team1.calculate_win(n, *T1)
Team1.calculate_loss(n, *T1)

T2 = ['LSG', 18, 1, 0, 0, 1, 1]
Team2 = Match()
Team2.calculate_win(n, *T2)
Team2.calculate_loss(n, *T2)

T3 = ['RR', 16, 1, 0, 1, 0, 0]
Team3 = Match()
Team3.calculate_win(n, *T3)
Team3.calculate_loss(n, *T3)


T4 = ['DC', 14, 1, 1, 0, 1, 0]
Team4 = Match()
Team4.calculate_win(n, *T4)
Team4.calculate_loss(n, *T4)


T5 = ['RCB', 14, 0, 1, 1, 0, 0]
Team5 = Match()
Team5.calculate_win(n, *T5)
Team5.calculate_loss(n, *T5)


T6 = ['KKR', 12, 0, 1, 1, 0, 1]
Team6 = Match()
Team6.calculate_win(n, *T6)
Team6.calculate_loss(n, *T6)


T7 = ['PBKS', 12, 0, 1, 0, 1, 0]
Team7 = Match()
Team7.calculate_win(n, *T7)
Team7.calculate_loss(n, *T7)


T8 = ['SRH', 12, 1, 0, 0, 0, 0]
Team8 = Match()
Team8.calculate_win(n, *T8)
Team8.calculate_loss(n, *T8)

T9 = ['CSK', 8, 0, 0, 1, 0, 1]
Team9 = Match()
Team9.calculate_win(n, *T9)
Team9.calculate_loss(n, *T9)

T10 = ['MI', 6, 0, 1, 0, 1, 1]
Team10 = Match()
Team10.calculate_win(n, *T10)
Team10.calculate_loss(n, *T10)


if WinTeamcount == 0:
    print ("No team has won", n ,"times consecutively")
else:
    WinAvg = Winsum/WinTeamcount
    print ("Average points of teams that have won", n ,"consecutive times is", WinAvg)  
if LossTeamcount == 0:
    print ("No team has lost", n ,"times consecutively")
    
else:
    LossAvg = Losssum/LossTeamcount
    print ("Average points of teams that have lost", n ,"consecutive times is", LossAvg)
