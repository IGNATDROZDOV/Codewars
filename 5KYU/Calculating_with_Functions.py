def zero(operation = None): 
    if not operation: 
        return 0 
    else: return operation(0)

def one(operation = None):
    if not operation: 
        return 1 
    else: return  operation(1)

def two(operation = None):
    if not operation: 
        return 2 
    else: return operation(2)

def three(operation = None):
    if not operation: 
        return 3 
    else: return operation(3)

def four(operation = None):
    if not operation: 
        return 4 
    else: return operation(4)

def five(operation = None):
    if not operation: 
        return 5 
    else: return operation(5)

def six(operation = None):
    if not operation: 
        return 6 
    else: return operation(6)

def seven(operation = None):
    if not operation: 
        return 7 
    else: return operation(7)

def eight(operation = None):
    if not operation: 
        return 8 
    else: return operation(8)

def nine(operation = None): 
    if not operation: 
        return 9 
    else: return operation(9)

def plus(number): return lambda x: x+number
def minus(number): return lambda x: x-number
def times(number): return lambda  x: x*number
def divided_by(number): return lambda  x: x//number