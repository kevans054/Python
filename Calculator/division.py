def divide(thislist):
    answer = thislist[0]
    for x in (thislist[1:]):
        x = int(x)
        answer //= x
    return(answer)