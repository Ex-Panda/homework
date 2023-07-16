def uppers(a):
    '''функция заглавных букв'''
    return a.upper()

def title(stroka):
    '''функция увеличения первых букв'''
    str_list = stroka.split(' ')
    list_2 = []
    for s in str_list:
        list_2.append(s.title())

    return ' '.join(list_2)
