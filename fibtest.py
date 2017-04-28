from timetest import timetest

#LVXX

def argtest( f ):
    def inner( *args, **kwargs ):
        print f.func_name + str(args)
        return f(*args, **kwargs )
    return inner

@argtest
def fib(n):
    
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n-1)+fib(n-2)

print 'result: ', fib(3)
