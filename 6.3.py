import inspect

def inspect(f):
    def wrap(*args, **kwargs):
        print (f'ARGS: {args} \nKWARGS: {kwargs}')
        retvalue = [ret for ret in args]
        ret = (' '.join(retvalue))
        print (f"RetValue: '{ret}'")
        return f(*args, **kwargs)
    return wrap    


@inspect
def concat (*args: str, revers = False) -> str:
    if revers:
        for rev_words in reversed(args):
            print (rev_words, end = ' ')
    else:
        for words in args:
            print (words, end = ' ')

concat ('Hello', 'my', 'name', 'is', 'Alexandr', revers= True)