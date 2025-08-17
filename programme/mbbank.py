def tien():
    print(f'So tien b dang co la: ${money:.2f}')

def rut():
    tienrut = float(input(f"Nhap so tien ban muon rut:"))

    if tienrut > money:
        print(f"ban deo du tien de rut")
        print('-------------Please chon again--------------')
        return 0
    elif tienrut < 0:
        print(f"tien rut m sao lol ha")
        print('-------------Please chon again--------------')
        return 0
    else: return tienrut


def nap():
    tienap = float(input(f'Nhap so tien b muon nap:'))

    if tienap < 0:
        print('Tien m sao lol ha thg ngu')
        print('-------------Please chon again--------------')
        return 0
    else: return tienap

def main():
    global money
    money = 0
    is_running = True

    while is_running:
        print("Nap Rut Tai Xiu")
        print("1.Xem Tien")
        print("2.Nap Tien")
        print("3.Rut Tien")
        print("4.exit sign")

        choice = int(input("Chon di thg ngu:"))

        match choice:
            case 1:
                tien()
            case 2:
                money += nap()
            case 3:
                money -= rut()
            case 4:
                is_running = False
            case _:
                print('Invalid choice')
                print('-------------Please chon again--------------')

    print('MB bank cam on')

if __name__ == '__main__':
    main()
