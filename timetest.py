#LVXX
import time
from fibtest import fib

def timetest( f ):
    origtime = time.time()
    def inner( *arg ):
        return f( *arg )
    functime = time.time() - origtime
    print "Function runtime: " + str(functime)
    return inner

@timetest
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
