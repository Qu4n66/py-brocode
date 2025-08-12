#case (switch): alternative for elif statement


def dow(day):
    if day == 1:
        return('It is sunday')
    elif day == 2:
        return('It is monday')
    elif day == 3:
        return('It is tuesday')
    else: 
        return('otherdays but iam too lazy to list them')


i = int(input('Enter numb:'))
print(dow(i))


def dow2(days):
    match days:
        case 4:
            return('It is wednesday')
        case 5:
            return('It is thursday')
        case 3:
            return('It is friday')
        case _:  #else
            return('otherdays but iam too lazy to list them')

print(dow2(4))

