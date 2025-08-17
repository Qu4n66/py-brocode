#Decorator = A function that extened the behavior of another function
#            without modifying the base function
#            pass the base function as an argument to decorator

#           @add_sprinkles ( some people will like)
#           get_ice_scream('Vanilla)


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you add sprinkles")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
def get_ice_cream(flavor):
    print(f'Here is your {flavor} ice cream')

get_ice_cream('Chocolate')

