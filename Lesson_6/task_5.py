# работа с декораторами

def decorate(funct):
    def wrapper():
        print('Wrapper')
        funct()
        print('Wrapper 2')
    return wrapper

@decorate
def test():
    print('Test')
test()
