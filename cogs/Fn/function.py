def fncheck(chorice):
        if chorice == 'True':
            chorice = False
        else :
            chorice = True
        return chorice

def fnmode(x):
    if x == 'osu':
        x = '0'
    elif x == 'taiko':
        x = '1'
    elif x == 'cbt':
        x = '2'
    elif x == 'mania':
        x = '3'
    else:
        '0'
    return x