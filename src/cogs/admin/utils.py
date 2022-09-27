# File made to group basic full python functions

def time2sec(time):
    """
    Converts a given time all in seconds. (5m20s --> 320s)
    """
    # There is actually a library to make this whole thing easier, humanfriendly, but it would add a dependency.
    mult = {
        'ms': 0.001, 
        's': 1, 
        'm': 60, 
        'h': 3600, 
        'd': 86400, 
        'w': 604800, 
        'y': 31564000, 
    }

    nb = ''
    unit = ''
    for i in time:
        try: #This tries int(i), so it works if i is a number but goes into the except if it is a letter.
            int(i)
            nb += i
        except:
            unit += i
    ftime = float(int(nb)*mult[unit])
    return ftime 