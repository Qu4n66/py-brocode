#concession stand game


menu = {'bbao' : 50,
        'bff': 30,
        'nigga': 20,
        'khi': 10,
        'suga': 10}
cart = []
total = 0
print('------------Menu-------------')
for key, value in menu.items():
    print(f'{key:10}: ${value:.2f}')
print('-----------------------------')

while True:
    people = input('Selec what u want:(q to quit)')
    if people.lower() == 'q':
        break
    elif menu.get(people) is not None:
        cart.append(people)
print('--------------ur order-------------')
for people in cart:
    total += menu.get(people)
    print(people, end = ' ')
print()
print(f'tong cong la: ${total}')
print('-----------------------------------')