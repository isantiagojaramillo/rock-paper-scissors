import random;


def play():
    user = input("Choose an option: Rock, Paper, Scissors \n").lower();

    computer = random.choice(['rock', 'paper', 'scissors']);

    if user == computer:
        return 'TIE!';
    
    if user_won(user, computer):
        return 'You Won!';

    return 'Game Over!';


def user_won(user, computer):
    if (
        (user == 'rock' and computer == 'scissors')
        or (user == 'scissors' and computer == 'paper')
        or (user == 'paper' and computer == 'rock')):
        return True;
    else:
        return False;


print(play());