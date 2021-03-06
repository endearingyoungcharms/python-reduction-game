from random import randint

startnum = randint(40, 60)


def main():
    print('Welcome to the game of reduction')
    print('You will have to try and reduce 1,2,3,4,5 or 6 from a mystery number')
    oneortwo = input('Do you want to play against another player or the computer?\n(a)notherplayer,(c)omputer,(q)uit ')
    if oneortwo in ('a', 'A', 'anotherplayer'):
        twoplayerstart()
    elif oneortwo in ('q', 'Q', 'quit'):
        quit()
    else:
        computer()


def computer():
    localnum = startnum
    print('The mystery number is', startnum)
    while localnum >= 0:
        sub = input('Do you want to substract 1,2,3,4,5 or 6?')
        if sub in ('1', '2', '3', '4', '5', '6'):
            localnum = localnum-int(sub)
            print('The number is now', localnum)
            if localnum <= 0:
                print('you lose')
                quit()
            if localnum in (1, 2, 3, 4, 5, 6, 7):
                if localnum == 5:
                    compc = 4
                elif localnum == 4:
                    compc = 3
                elif localnum == 3:
                    compc = 2
                elif localnum == 2:
                    compc = 1
                elif localnum == 1:
                    compc = 1
                elif localnum == 6:
                    compc = 5
                elif localnum == 7:
                    compc = 6
            else:
                compc = randint(1, 6)

            print('The computer is now making its choice')
            localnum = localnum - compc
            print('The number is now', localnum)
            if localnum <= 0:
                print('You win')
                quit()
        else:
            print('Please enter a number from 1 to 6')
            main()


def twoplayerstart():
    nplayer1 = input('What is your name, Player1?')
    nplayer2 = input('What is your name, Player2?')
    twoplayermain(nplayer1, nplayer2)


def twoplayermain(nplayer1, nplayer2):
    localnum = startnum
    print('The mystery number is', startnum)
    while localnum >= 0:
        print('Pass the device to', nplayer1)
        player1 = str(input('Do you want to substract 1,2,3,4,5 or 6?'))
        if player1 in ('1', '2', '3', '4', '5', '6'):
            localnum = localnum-int(player1)
            print('The number is now', localnum)
            if localnum <= 0:
                print(nplayer1, 'has lost the game')
                quit()
            else:
                print('pass the device to', nplayer2)
                player2 = input('Do you want to substract 1,2,3,4,5 or 6?')
                if player2 in ('1', '2', '3', '4', '5', '6'):
                    localnum = localnum-int(player2)
                    print('The number is now', localnum)
                    if localnum <= 0:
                        print(nplayer2, 'has lost the game')
                        quit()
                else:
                    print('Please enter a number from 1 to 6')
                    main()
        else:
            print('Please enter a number from 1 to 6')
            main()


if __name__ == "__main__":
    main()
