"""
Random Generate program V.1.8

by @gtahriz@ZeroHX
"""
import random
def rand():
    print()
    print('===================================')
    print('|| Welcome to Random Program !!! ||')
    print('===================================')
    print('||                               ||')
    print('||        ⊂_ヽ                  ||')
    print('||           ＼＼ ^ ^            ||')
    print('||             ＼(\'w\')           ||')
    print('||               >　⌒ヽ         ||')
    print('||        　　　/ 　 へ＼        ||')
    print('||        　　 /　　/　＼＼      ||')
    print('||        　　 ﾚ　ノ　　 ヽ_つ   ||')
    print('||        　　/　/               ||')
    print('||        　 /　/|               ||')
    print('||        　(　(ヽ               ||')
    print('||        　|　|、＼             ||')
    print('||        　| 丿 ＼ ⌒)          ||')
    print('||        　| |　　) /           ||')
    print('||         ノ )　　Lﾉ            ||')
    print('||        (_／                   ||')
    print('___________________________________')
    print()
    print('This program can input alphabet(lower & upper) and number')
    print('___________________________________')
    choice = input('Choose your way\n1: Number \n2: Dice\n3: Yes/No\n4: Custom\nEnter your way >>> ')

    #Random number in range(int(input()))
    if choice.lower() in ['num', '1', 'number']:
        num = int(input('Enter your range: '))
        print('--------------------------->')
        #Random number
        ran = random.randrange(num)
        print("Your lucky number is %d !!!" % (ran))
        print('   _   '*ran)
        print('__(.)= '*ran)
        print('\\___)  '*ran)
        print()
        print('Have a nice day !!!')

    #Random Dice (1-6)
    elif choice.lower() in ['dice', '2']:
        ran2 = random.randrange(7)
        ht = [1, 2, 3, 4, 5, 6]
        print('***************************')
        #Dice one
        if ht[ran2] == 1:
            print('The dice is 1 !!!')
            print(' _________________')
            print('|                 |')
            print('|                 |')
            print('|        o        |')
            print('|                 |')
            print('|                 |')
            print(' _________________')
        #Dice two
        elif ht[ran2] == 2:
            print('The dice is 2 !!!')
            print(' _________________')
            print('|                 |')
            print('|                 |')
            print('|     o     o     |')
            print('|                 |')
            print('|                 |')
            print(' _________________')
        #Dice three
        elif ht[ran2] == 3:
            print('The dice is 3 !!!')
            print(' _________________')
            print('|                 |')
            print('|             o   |')
            print('|        o        |')
            print('|    o            |')
            print('|                 |')
            print(' _________________')
        #Dice four
        elif ht[ran2] == 4:
            print('The dice is 4 !!!')
            print(' _________________')
            print('|                 |')
            print('|    o        o   |')
            print('|                 |')
            print('|    o        o   |')
            print('|                 |')
            print(' _________________')
        #Dice five
        elif ht[ran2] == 5:
            print('The dice is 5 !!!')
            print(' _________________')
            print('|                 |')
            print('|    o        o   |')
            print('|        o        |')
            print('|    o        o   |')
            print('|                 |')
            print(' _________________')
        #Dice six
        elif ht[ran2] == 6:
            print('The dice is 6 !!!')
            print(' _________________')
            print('|                 |')
            print('|    o        o   |')
            print('|    o        o   |')
            print('|    o        o   |')
            print('|                 |')
            print(' _________________')
            print('Have a nice day !!')

    #Random yes or no
    elif choice.lower() in ['yn', '3', 'yes-no']:
        ran3 = random.randrange(2)
        yn = ['YES!', 'NO!']
        print(yn[ran3])
        if yn[ran3] == 'YES!':
            print('YYYYYYYY        YYYYYYYY    EEEEEEEEEEEEEEEEEE      SSSSSSSSSSS')
            print('YYYYYYYY        YYYYYYYY    EEEEEEEEEEEEEEEEEE     SSSSSSSSSSSSS')
            print('YYYYYYYY        YYYYYYYY    EEEEEEEEEEEEEEEEEE    SSSSSSSSSSSSSSS')
            print('YYYYYYYY        YYYYYYYY    EEEEEEEEEEEEEEEEEE    SSSSSSSS    SSS')
            print(' YYYYYYYY      YYYYYYYY     EEEEEEEE              SSSSSSSS')
            print('  YYYYYYYY    YYYYYYYY      EEEEEEEE              SSSSSSSS')
            print('   YYYYYYYY  YYYYYYYY       EEEEEEEEEEEEE          SSSSSSSS')
            print('    YYYYYYYYYYYYYYYY        EEEEEEEEEEEEE           SSSSSSSSSS')
            print('     YYYYYYYYYYYYYY         EEEEEEEEEEEEE            SSSSSSSSSS')
            print('      YYYYYYYYYYYY          EEEEEEEEEEEEE               SSSSSSSSS')
            print('       YYYYYYYYYY           EEEEEEEE                     SSSSSSSS')
            print('        YYYYYYYY            EEEEEEEE                     SSSSSSSS')
            print('        YYYYYYYY            EEEEEEEEEEEEEEEEE     SSS    SSSSSSSS')
            print('        YYYYYYYY            EEEEEEEEEEEEEEEEE     SSSSSSSSSSSSSSS')
            print('        YYYYYYYY            EEEEEEEEEEEEEEEEE      SSSSSSSSSSSSS')
            print('        YYYYYYYY            EEEEEEEEEEEEEEEEE       SSSSSSSSSSS')
        elif yn[ran3] == 'NO!':
            print('NNNNNNNNNNNNNN          NNNNNNN          OOOOOOOOOOOOOOOOOOOOOO')
            print('NNNNNNNNNNNNNNN         NNNNNNN          OOOOOOOOOOOOOOOOOOOOOO')
            print('NNNNNNNNNNNNNNNN        NNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNNNNNNNNNNNN       NNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN NNNNNNNNNN      NNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN  NNNNNNNNNN     NNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN   NNNNNNNNNN    NNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN    NNNNNNNNNN   NNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN     NNNNNNNNNN  NNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN      NNNNNNNNNN NNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN       NNNNNNNNNNNNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN        NNNNNNNNNNNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN         NNNNNNNNNNNNNNN          OOOOOO          OOOOOO')
            print('NNNNNNN          NNNNNNNNNNNNNN          OOOOOOOOOOOOOOOOOOOOOO')
            print('NNNNNNN           NNNNNNNNNNNNN          OOOOOOOOOOOOOOOOOOOOOO')
            print('Have a nice day !!')

    #Random choice with (choice = list, random >> index)
    elif choice.lower() == 'custom' or choice == '4':
        #size of loop
        time = int(input("How many choice?: "))
        print()
        #input all choice with loop in <time> and add in list
        lst = [input("Your choice %d/%d: "%(i+1, time)) for i in range(time)]
        print('--------------------------->')
        #Random from index
        ran4 = lst[random.randrange(time)]
        print('%s %s!!' %('Best choice is', ran4))
        print('   _')
        print('__(.)< << %s' % (ran4), ran4[-1], ran4[-1], ran4[-1])
        print('\\___)')
        print()
        print('Have a nice day !!')

    else:
        print("WTF are you enter!!")

    print('--------------------------->')

    ter = input('Play Again?(Y/N): ')
    if ter.lower() in ['y', '1', 'yes']:
        rand()
rand()