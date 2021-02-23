from random import shuffle

def shuffle_list(list):
    shuffle(list)
    return list
def player_guess():
    guess=''
    while guess not in ['0','1','2','3','4','5','6','7']:
        print("Pick a number:0,1,2,3,4,5,6,7")
        guess=input()
    return int(guess)
def check_guess(list,guess):
    if list[guess]=='M':
        print("Correct!")
        print(list)
    else:
        print("Wrong guess!")
        print(list)

list=[' ','M',' ',' ',' ',' ',' ',' ']

check_guess(shuffle_list(list),player_guess())
