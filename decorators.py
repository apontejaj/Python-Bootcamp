# Decorators are functions that modify the funtionality of another funtion

# For example, we have function that needs a decorator

# remember, the decorator must have as argument another function

def my_decorator(func):
    print 'this will happen before executing the function'
    func('Amilcar')
    print 'this will happen after the function'

@my_decorator
def decorator_needed(x):
    print 'This function needs a decorator {}'.format(x)
