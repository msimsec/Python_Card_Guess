from random import shuffle

def shuffle_list(list): #Liste Karistirılıyor
    shuffle(list)
    return list
def player_guess(): # Uzerinde M harfi bulunan kutu tahmin edilmeye calisiliyor.
    guess=''
    while guess not in ['0','1','2','3','4','5','6','7']:
        print("Pick a number:0,1,2,3,4,5,6,7")
        guess=input()
    return int(guess)
def check_guess(list,guess): #Karistirilan liste ve tahmin edilen index karsilastiriliyor ve Sonuc yazdiriliyor.
    if list[guess]=='M':
        print("Correct!")
        print(list)
    else:
        print("Wrong guess!")
        print(list)

list=[' ','M',' ',' ',' ',' ',' ',' ']

check_guess(shuffle_list(list),player_guess()) #Karistirma methodu ve tahmin methodları cagriliyor.
