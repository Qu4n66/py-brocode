#expection = An event that interupts the flow of a program


try:
    number = int(input('Enter a number:'))
    print(1/number)
except ZeroDivisionError:
    print('You cannot divide by zero')
except ValueError:
    print('Enter numbers only')
except Exception:
    print('Somethings went wrong')
finally:
    print('Do some cleanup here')


