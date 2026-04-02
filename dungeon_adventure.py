import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        player = input("Enter your player name: ")
        print(f"Welcome {player}")

        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        player = {"name": player, "health": 10, "inventory": []}

        # TODO: Return the dictionary
        return player
    
    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        treasures = {
            "golden sceptor": 12,
            "coin": 5,
            "amethyst gemstone": 9,
            "blank scroll": 2,
            "candle": 2,
        }
        # TODO: Return the dictionary
        return treasures

    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        # TODO: Print the room number and the 4 menu options listed above
        # room = [1,2,3,4,5]
        print(f"You are currently in room {room_number}")
        print("Would you like to \n 1: Search for treasure,\n 2: Move to the next room,\n 3: Check your health and inventory\n 4: Quit the game?\n")
        room = {
            "1": "Search for Treasure",
            "2": "Move to next room",
            "3": "Check Health and Inventory Bag",
            "4": "End Game"
        }

        room_choice = input(f"Would you like to do? (Select 1, 2, 3, or 4)\n")
        # room_number = user_choice
        while room_choice not in room:
            print("please choose a valid option")
            room_choice = input(f"Would you like to do? (Select 1, 2, 3, or 4)\n")
        
        print(f"You have chosen option {room_choice}")
        # print("1: Search for treasure,\n 2: Move to the next room,\n 3:Check your health and inventory\n 4: Quit the game?\n")

        # while room_number not in room:
        #     room_number = input(f" Would you like to \n 1: Search for treasure,\n 2: Move to the next room,\n 3:Check your health and inventory\n 4: Quit the game?\n (Select 1, 2, 3, or 4)\n")
        #     if room_number in room:
        #         print(room.keys())
        return room_choice

    
        # print(f"You are in room {room_number}")
    
    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        outcome = random.choice(["treasure", "trap"])
        
        # TODO: Write an if/else to handle treasure vs trap outcomes
        if outcome == "trap":
            print("Trap! You lose 2 health")
            player["health"] -= 2
        else:
            r_t = random.choice(list(treasures.keys()))
            player["inventory"].append(r_t)
            print(f"You gained a {r_t}")
                
        # TODO: Update player dictionary accordingly
        # if outcome == "treasure":
        #     for t in treasures:
        #         t == treasures.pop(random.choice(list(treasures.keys())))
        #         t.append(player["inventory"])
        # TODO: Print messages describing what happened
        # search_room

    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health

        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”

        print(f'Your health is currently: {player["health"]}')

        if player["inventory"] == []:
            print("No items available")
        else:
            print(f'You currently have {player["inventory"]} on hand')


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing."

        # treasure_sum = player["inventory"]

        # count = 0
        # for eaches in treasures:
        #     eaches = treasures
        #     count += eaches

        # if player["inventory"] in treasures.keys():
        #     sum += treasures.values

        gold = 0
        for item in player["inventory"]:
            gold += treasures[item]

        # def sum_health():
        #     print(player["health"])
        #     return sum_health
    
        end_health = player["health"]
        end_inventory = player["inventory"]
        

        print(f'Game Over! You have {end_health} health, {end_inventory} summing in a total of {gold} gold')
        return

    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored

        for room_number in range(1, 6):
            while True:
                room_choice = display_options(room_number)
                # while room_number not in room:
                
                if room_choice == "1":
                    search_room(player, treasures)
                    if player["health"] < 1:
                        print("Your health is too low.")
                        end_game(player, treasures)
                        return
                elif room_choice == "2":
                    print("Move to the next room")
                    break
                elif room_choice == "3":
                    check_status(player)
                elif room_choice == "4":
                    print("Game over!")
                    end_game(player, treasures)
                    return
        end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)
    
if __name__ == "__main__":
    main()
