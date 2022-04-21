
def concat (*args: str, rev = False, sep = ' ', end = '\n') -> str:
    if rev:
        for rev_words in reversed(args):
            print (rev_words, sep = sep, end = end)
    else:
        for words in args:
            print (words, sep = sep, end = end)

       
concat ('Hello', 'my', 'name', 'is', 'Alexandr', rev = True, sep = ' ', end = ' ' )


