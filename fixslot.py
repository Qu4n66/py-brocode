
import random
import time
def spin_row():
    symbols = ['🐶', '😺', '🐄', '🦖', '🐯']
    result = []


    for symbol in range(3):
        result.append(random.choice(symbols))
    return result

def print_row(dog):
    print('************')
    print(' | '.join(dog))
    print('************')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case '🐶':
                return bet * 3
            case '😺':
                return bet * 3
            case '🐄':
                return bet * 5
            case '🦖':
                return bet * 10
            case '🐯':
                return bet * 4
    return 0
            





def main():
    tien = 100
    print('------------------------')
    print('Welcome to 777 game')
    print('Symbol: 🐶 😺 🐄 🦖 🐯 ')
    print('***********************')

    while tien > 0:
        print(f'Current balance: ${tien:.2f}')
        bet = input('Enter your bet:')

        if not bet.isdigit():
            print('*******ERROR*******')
            print('Please enter a valid number')
            continue

        bet = int(bet)

        if bet > tien:
            print('Deo du tien')
            print('----------Dat lai------------')
            continue

        if bet <= 0:
            print('Thang oc cho dat 0 tien')
            print('----------Dat lai------------')
            continue
        tien -= bet
        row = spin_row()
        print('Dag suc....\n')
        time.sleep(0.5)

        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
            print(f'You Won ${payout}')
        else:
            print('Sorry you lost this round')
        tien += payout

        play_again = input('Chs tiep  0 thg ngu?(y/n):')
        if play_again.lower() != 'y':
            break

        
    print(f'Tien cua m la: ${tien}')

if __name__ == '__main__':
    main()




