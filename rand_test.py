"""
Random Generate program V.1.4

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
    print('||        ノ )　　Lﾉ             ||')
    print('||        (_／                   ||')
    print('___________________________________')
    print()
    choice = input('Choose your way (num/custom): ')
    if choice.lower() == 'num':
        num = int(input('Enter your range: '))
        print('--------------------------->')
        ran = random.randrange(num)
        print("%s%d !!!" % ("Your lucky number is ", ran))
        print('   _   '*ran)
        print('__(.)= '*ran)
        print('\\___)  '*ran)
        print()
        print('Have a nice day !!')
    elif choice.lower() == 'custom':
        time = int(input("How many choice?: "))
        print()
        lst = [input("Your choice %d/%d: "%(i+1, time)) for i in range(time)]
        print('--------------------------->')
        ran2 = lst[random.randrange(time)]
        print('%s %s!!' %('Best choice is', ran2))
        print('   _')
        print('__(.)< << %s' % (ran2), ran2[-1], ran2[-1], ran2[-1])
        print('\\___)')
        print()
        print('Have a nice day !!')
    else:
        print("WTF are you enter!!")

    print('--------------------------->')

    ter = input('Play Again?(Y/N): ')
    if ter.lower() == 'y':
        rand()
rand()