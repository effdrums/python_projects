class MenuArtillery3: 
    
    initial_message = "WELCOME TO ARTILLERY3:"
    num_players_message = "How many players are going to play? (1 to 3)"
    start_game_message = "Well!! So let's start the Game!!"
    error_players_message = "Oooops! the number of players is not OK, try again or quit."
    num_players = 0
    num_max_tanks = 3
    start_game = False

    def run(self):
        print(self.initial_message)
        

        while not self.start_game:
            num_players = input(self.num_players_message)
           
            try:    
                if int(num_players) >= 1 and int(self.num_players) <= self.num_max_tanks:
                    print(self.start_game_message)
                    self.start_game = True
                    self.num_players = num_players
                else:
                    print(self.error_players_message)

            except ValueError:
                print(self.error_players_message)
                