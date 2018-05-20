from datetime import datetime

def pre_date(pre):
    def date(func):
        def wrapper():
            func()
            date = datetime.utcnow()
            print(pre + str(date))
        return wrapper
    return date

@pre_date('Today is :')
def alan():
    print ('alan speaking')
    
@pre_date('I am Tom :')
def tom():
    print ('tom speaking')
    
alan()
tom()


###########################################################
# Not define a function in decorator
# register run before funcitons
# e.g register router in web framework
registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


@register
def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
