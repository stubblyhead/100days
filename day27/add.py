def add(*args):
    if len(args) == 1:
        return args[0]
    else:
        return args[0] + add(*args[1:])
    
print(add(*[ i for i in range(100) ]))