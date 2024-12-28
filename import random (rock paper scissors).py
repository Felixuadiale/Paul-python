import random
def get_user_choice():
    user_choice=str(input("Enter your choice(Rock paper or scissors)")).lower()
    while user_choice not in ["rock","paper","scissors"]:
        print("Invalid choice.please enter rock , paper, scissors.")
        user_choice=input("Enter your choice"("rock,paper, scissors")).lower
        return user_choice
    def get_computer_choice():
        return random.choice( "rock","paper","scissors")
    def play_game():
        print("Welcome to rock, paper,scisors")
        user_choice = get_user_choice()
        computer_choice
