"""
Random Generate program V.1.7

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
    choice = input('Choose your way (<1>num | <2>custom | <3>YN): ')

    #Random number in range(int(input()))
    if choice.lower() == 'num' or choice == '1':
        num = int(input('Enter your range: '))
        print('--------------------------->')
        #Random number
        ran = random.randrange(num)
        print("%s%d !!!" % ("Your lucky number is ", ran))
        print('   _   '*ran)
        print('__(.)= '*ran)
        print('\\___)  '*ran)
        print()
        print('Have a nice day !!')

    #Random choice with (choice = list, random >> index)
    elif choice.lower() == 'custom' or choice == '2':
        #size of loop
        time = int(input("How many choice?: "))
        print()
        #input all choice with loop in <time> and add in list
        lst = [input("Your choice %d/%d: "%(i+1, time)) for i in range(time)]
        print('--------------------------->')
        #Random from index
        ran2 = lst[random.randrange(time)]
        print('%s %s!!' %('Best choice is', ran2))
        print('   _')
        print('__(.)< << %s' % (ran2), ran2[-1], ran2[-1], ran2[-1])
        print('\\___)')
        print()
        print('Have a nice day !!')

    #Random yes or no
    elif choice.lower() == 'yn' or choice == '3':
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
    
    else:
        print("WTF are you enter!!")

    print('--------------------------->')

    ter = input('Play Again?(Y/N): ')
    if ter.lower() == 'y':
        rand()
rand()
